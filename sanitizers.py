import re
from datetime import date

date_encuentro = date(2023, 11, 24)

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

def sanitize(word):
    return word.strip().lower().capitalize()

def sanitize_name(name):
    names = name.split()
    return " ".join(list(map(sanitize, names)))

def sanitize_surname(surname):
    dsurname = surname.split()
    if dsurname[0].strip() == 'de':
        return 'de ' + sanitize(dsurname[1])
    else:
        return sanitize(dsurname[0])
    
des = ['de', 'del', 'la', 'las', 'los', 'y']
def sanitize_surnames(surnames):
    dsurnames = surnames.split()
    s_surnames = [sanitize(s) if s not in des else s.lower() for s in dsurnames]
    return " ".join(s_surnames)

def check_image_rights(image_rights):
    return image_rights == "AUTORIZO a Juventudes Marianas Vicencianas España a publicar fotos y vídeos en los que aparezca durante la actividad."

def check_alone(alone, birthdate):
    age = calculateAge(birthdate) 
    auth = age >= 14 
    return (alone == "AUTORIZO a Juventudes Marianas Vicencianas España a permitir que mi hijo/a se vaya solo al finalizar la actividad.") and auth

def sanitize_relationship(relationship):
    return relationship.lower()

def check_allergies(allergies):
    return allergies == "Sí"

def check_relationship(relationship):
    if relationship == "madre o tutora legal":
        return "Doña"
    else:
        return "Don"
    
DNI_REGEX = r"(\d{8})([-]?)([A-Z]{1})"
NIE_REGEX = r"([X-Z]{1})([-]?)(\d{7})([-]?)([A-Z]{1})"
def sanitize_id(id):
    id = "".join(id.split()).upper()
    if re.match(DNI_REGEX, id):
        return id, "DNI"
    elif re.match(NIE_REGEX, id):
        return id, "NIE"
    else:
        return id, "pasaporte"
    

def sanitize_phone(phone):
    return "".join(phone.split())
