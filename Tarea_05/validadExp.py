import re

def validaCorreo(cadena):
    patronCorreo = ("(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])")
    banderaCorreo = re.search(patronCorreo,cadena)
    if (banderaCorreo is None):
        return False
    else:
        return True

def validaTel(cadena):
    patronesTel = ('\(\d{3}\)\d{7}', '\(\d{3}\) \d{3} \d{4}', '\(\d{3}\)-\d{3}-\d{4}')
    for i in patronesTel:
        if re.match(i, cadena) is not None:
            return True
        else:
            return False

def validaCURP(cadena):
    patronCURP = "[a-zA-Z]{4}\d{6}[HMhm][a-zA-Z0-9]\d"
    banderaCURP = re.match(patronCURP, cadena)
    if (banderaCURP is None):
        return True
    else:
        return False