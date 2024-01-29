from __future__ import print_function
import json
import pandas as pd
from mailmerge import MailMerge
import os
import sys
import email_aux as em
import yagmail
import re
import sanitizers as sn
from renamer import renamer, names, surnames
import writers as wr

OS = sys.argv[1]

if OS == "linux":
    pdf_writer = "libreoffice "
elif OS == "macos":
    pdf_writer = "soffice"
else:
    print("Please select an OS (linux or macos)")
    raise SystemExit

config = json.load(open('config.json'))

if not os.path.isdir(config["auth_dir"]):
    os.mkdir(config["auth_dir"])

# Import data 
df_old = pd.read_csv(config["input_data"], dtype = object)
if df_old.empty:
    print("No hay datos nuevos.")
    raise SystemExit
df_old.rename(columns=renamer, inplace=True)
df_old.timestamp = pd.to_datetime(df_old.timestamp, dayfirst = True)
for col in df_old.columns:
    if col == "birthdate":
        df_old[col] = df_old[col].fillna("01/01/1900")
    else:
        df_old[col] = df_old[col].fillna("")


# Check last_time
last_time = pd.to_datetime(config["last_time"], format = "%Y-%m-%d %H:%M:%S")
df = df_old[df_old.timestamp > last_time]

#sanitation
df.timestamp = pd.to_datetime(df.timestamp, dayfirst = True)
[df.update(df[n].apply(sn.sanitize_name)) for n in names]
[df.update(df[s].apply(sn.sanitize_surnames)) for s in surnames]
[df.update(df[p].apply(sn.sanitize_phone)) for p in ['phone_cat', 'guardian_phone']]
#df.guardian_phone = df.guardian_phone.astype('Float64')
#df.guardian_phone = df.guardian_phone.astype('Int64')
df.birthdate = pd.to_datetime(df.birthdate, dayfirst = True)
df.data_protection = True
df.update(df.image_rights.apply(sn.check_image_rights))
df.update(df.relationship.apply(sn.sanitize_relationship))
df.update(df.allergies.apply(sn.check_allergies))
df.insert(11, 'ID_type', "Unknown")
df.guardian_ID, df.ID_type = zip(*df.guardian_ID.apply(sn.sanitize_id))
df.insert(8, 'treat', "Unknown")
df.treat = df.relationship.apply(sn.check_relationship)

df.insert(12, 'alone', False)
for rowi, row in df.iterrows():
    df.at[rowi, 'alone'] = sn.check_alone(row['palone'], row['birthdate'])

# Initialize auth and email
account, oauth2_file, banner, signature, notice_f = [config["email"].get(key) for key in config["email"].keys()]
yag = yagmail.SMTP(account, oauth2_file=oauth2_file)
with open(notice_f) as f:
    notice = f.read()

for index, row in df.iterrows():
    if row.category == "Responsable":
        continue
    document = MailMerge(config['auth_template'])
    print(f"Inscripción de {row['name']} {row['surnames']}.")
    auth_file = wr.write_auth(row, document, config["auth_dir"])
    os.system(f"{pdf_writer} --convert-to pdf --outdir {config['auth_dir']} '{auth_file}'")
    auth_file = auth_file.replace('docx', 'pdf')
    subject, text = wr.write_email(row,)
    yag.send(to=row['guardian_email'], subject=subject, contents=[yagmail.inline(banner), text, yagmail.inline(signature), notice], attachments=[auth_file])
    print(f"Inscripción finalizada. Email enviado con éxito a {row.guardian_email}.")

#Update last_time
new_last = df.timestamp.max()
config["last_time"] =  new_last.strftime("%Y-%m-%d %H:%M:%S")
with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=4)

# Save data
df_curernt = pd.read_csv(config["database"])
frames = [df_curernt, df]
df_new = pd.concat(frames)
for col in df.columns.values.tolist():
    if re.search("Unnamed", col):
        df_new = df_new.drop(col, axis=1)
df_new.to_csv(config["database"])