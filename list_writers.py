from mailmerge import MailMerge
from datetime import date
import os

def write_form_dict(row):
    form_dict = {}
    form_dict['center_name'] = row['center_name']
    form_dict['full_name'] = row['name'] + " " + row['surname1'] + " " + row['surname2']
    form_dict['treat'] = row['treat']
    form_dict['guardian_full_name'] = row['guardian_name'] + " " + row['guardian_surname1'] + " " + row['guardian_surname2']
    form_dict['guardian_ID'] = row['guardian_ID']
    form_dict['ID_type'] = row['ID_type']
    form_dict['relationship'] = row['relationship']
    form_dict['image_rights'] = 'AUTORIZO' if row['image_rights'] else 'NO AUTORIZO'
    return form_dict

class group:
    def __init__(self, center = "", responsible = "", responsible_phone = ""):
        self.center = center
        self.responsible = responsible
        self.responsible_phone = responsible_phone
        self.size = 0
        self.boys = 0
        self.girls = 0
    
    def __str__(self):
        return f"Centro: {self.center}. Responsable: {self.responsible}. Participantes: {self.size}"
    
    def get_basic_info(self):
        bdict = {
            "center": self.center,
            "responsible": self.responsible,
            "responsible_phone": self.responsible_phone,
            "num_center" : str(self.size),
            "num_girls" : str(self.girls),
            "num_boys" : str(self.boys),
            "last_up" : str(date.today()),
        }
        return bdict
    
    def create_group(self, df):
        if self.center == "Todos":
            group_df = df
        else:
            group_df = df[df.center_name == self.center]
        group_df = group_df.sort_values(by=['surnames', 'name'])
        group_df['year'] = group_df.birthdate.dt.year
        group_df['obs'] = ""
        comments = 0
        comments_dict = {}
        for ind in group_df.index:
            if group_df.loc[ind, 'allergies']:
                comments += 1
                group_df.loc[ind, 'obs'] = comments
                comments_dict[comments] = "ATENCIÓN:" +  group_df.loc[ind, 'allergies_detail'] + ". "
        
        self.group_df = group_df
        self.size = len(group_df)
        count_sex = group_df.sex.value_counts()
        self.boys = count_sex.get('Masculino', 0)
        self.girls = count_sex.get('Femenino', 0)
        self.comments_dict = comments_dict
    
    def list_dicts(self):
        #lf = self.group_df.loc[self.group_df.category == 'Participante']
        lf = self.group_df
        list_dicts = []
        for ind in lf.index:
            list_dict = {
                'name' : lf.at[ind, 'name'],
                'surnames' : lf.at[ind, 'surnames'],
                'year' : str(lf.at[ind, 'year']),
                'phone' : f"{lf.at[ind, 'guardian_phone']}".rstrip('.0'),
                'pics' : 'Sí' if lf.at[ind, 'image_rights'] else 'No',
                'alone' : 'Sí' if lf.at[ind, 'alone'] else 'No',
                'obs' : str(lf.at[ind, 'obs']),
                'center_name' : lf.at[ind, 'center_name']
            }
            list_dicts.append(list_dict)
        return list_dicts 
    
    def list_dicts_cats(self):
        lf = self.group_df.loc[self.group_df.category == 'Responsable']
        list_dicts = []
        for ind in lf.index:
            list_dict = {
                'name' : lf.at[ind, 'name_cat'],
                'surnames' : lf.at[ind, 'surnames_cat'],
                'center_cat' : lf.at[ind, 'center_name_cat'],
                'phone' : f"{lf.at[ind, 'phone_cat']}".rstrip('.0')
            }
            list_dicts.append(list_dict)
        return list_dicts
    
    def list_comments(self):
        list_comments = []
        for key, val in self.comments_dict.items():
            list_comment = {
                'num' : str(key),
                'obs_text' : val
            }
            list_comments.append(list_comment)
        if not list_comments:
            list_comments = [{'num' : '', 'obs_text' : 'No hay observaciones.'}]
        return list_comments


def make_cat_list(groups, template, output_dir):
    output = f"{output_dir}/catequistas.docx"
    group = groups[-1]
    document = MailMerge(template)
    document.merge(**group.get_basic_info())
    document.merge_rows('name', group.list_dicts_cats())
    document.write(output)
    os.system(f"soffice --convert-to pdf --outdir {output_dir} '{output}'")

def make_lists(group, template, output_dir):
    output = f"{output_dir}/{group.center}.docx"
    document = MailMerge(template)
    document.merge(**group.get_basic_info())
    document.merge_rows('name', group.list_dicts())
    document.merge_rows('num', group.list_comments())
    document.write(output)
    os.system(f"soffice --convert-to pdf --outdir {output_dir} '{output}'")