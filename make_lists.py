from __future__ import print_function
import pandas as pd
import re
import os
from datetime import date
import list_writers as lw
import json

config = json.load(open('config.json'))

input_data = config["database"]

df = pd.read_csv(input_data)

# Sanitizde 
colnames = df.columns.values.tolist()
for col in colnames:
    if re.search("Unnamed", col):
        df = df.drop(col, axis=1)
df.birthdate = pd.to_datetime(df.birthdate, dayfirst = True, format = 'mixed')

# Create groups 
groups = []
group_data = json.load(open('groups.json'))
for g_name, g_data in group_data:
    groups.append(lw.group(g_name, g_data["responsable"], g_data["contacto"]))

for g in groups:
    g.create_group(df)

try:
    os.mkdir("Listas")
except:
    pass


# Write lists
template = "template_list.docx"
template_full = "template_list_full.docx"
for g in groups:
    if g.center == 'Todos':
        lw.make_lists(g, template_full, "Listas")
        continue
    lw.make_lists(g, template, "Listas")   

template = "template_list_cats.docx"
lw.make_cat_list(groups, template, "Listas")