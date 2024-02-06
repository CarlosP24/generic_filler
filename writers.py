import email_aux as em
def write_form_dict(row):
    form_dict = {}
    form_dict['center_name'] = row['center_name']
    form_dict['full_name'] = f"{row['name']} {row['surnames']}"
    form_dict['treat'] = row['treat']
    form_dict['guardian_full_name'] = f"{row['guardian_name']} {row['guardian_surnames']}"
    form_dict['ID_type'] = row['ID_type']
    if row['ID_type'] == 'pasaporte':
        form_dict['guardian_ID'] = f"{row['guardian_ID']}, de nacionalidad {row['guardian_nationality']}"
    else:
        form_dict['guardian_ID'] = row['guardian_ID']
    form_dict['relationship'] = row['relationship']
    form_dict['image_rights'] = 'AUTORIZO' if row['image_rights'] else 'NO AUTORIZO'
    form_dict['alone'] = 'AUTORIZO' if row['alone'] else 'NO AUTORIZO'
    form_dict['sex'] = 'hijo' if row['sex'] == 'Masculino' else 'hija'
    form_dict['soloa'] = 'solo' if row['sex'] == 'Masculino' else 'sola'
    form_dict['alergies'] = 'no presenta ninguna alergia, intolerancia o condición médica que deba ser tenida en cuenta por la organización' if not row['allergies'] else f"presenta las siguientes alergias, intolerancias o condiciones médicas: {row['allergies_detail']}"
    form_dict['guardian_phone'] = row['guardian_phone']
    return form_dict

def write_auth(row, document, output_dir):
    output_file = f"{output_dir}/{row['surnames']}_{row['name']}.docx"
    form_dict = write_form_dict(row)
    document.merge(**form_dict)
    document.write(output_file)
    return output_file

def write_email(row, cat):
    subject = f"Inscripción Prepascua 2024 de {row['name']} {row['surnames']}"
    text = em.write_text(row['name'], row['guardian_name'], cat)
    return subject, text
