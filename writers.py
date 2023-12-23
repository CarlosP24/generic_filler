import email_aux as em
def write_form_dict(row):
    form_dict = {}
    form_dict['center_name'] = row['center_name']
    form_dict['full_name'] = f"{row['name']} {row['surnames']}"
    form_dict['treat'] = row['treat']
    form_dict['guardian_full_name'] = f"{row['guardian_name']} {row['guardian_surnames']}"
    form_dict['guardian_ID'] = row['guardian_ID']
    form_dict['ID_type'] = row['ID_type']
    form_dict['relationship'] = row['relationship']
    form_dict['image_rights'] = 'AUTORIZO' if row['image_rights'] else 'NO AUTORIZO'
    form_dict['alone'] = 'AUTORIZO' if row['alone'] else 'NO AUTORIZO'
    return form_dict

def write_auth(row, document, auth_dir):
    output_file = f"{auth_dir}/{row['surnames']}_{row['name']}.docx"
    form_dict = write_form_dict(row)
    document.merge(**form_dict)
    document.write(output_file)
    return output_file

def write_email(row):
    subject = f"Inscripción Vigilia de la Milagrosa (24 de noviembre) de {row['name']} {row['surnames']}"
    text = em.write_text(row['name'], row['guardian_name'])
    return subject, text
