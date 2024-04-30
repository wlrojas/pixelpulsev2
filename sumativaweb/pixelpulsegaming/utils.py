import requests


def obtener_tasa_de_cambio(base='CLP', target='CLP'):
    if base == target:
        return 1
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    response = requests.get(url)
    data = response.json()
    tasa = data['rates'].get(target, 1)
    return tasa


def obtener_clima():
    url = 'https://wttr.in/Santiago?format=%l:+%t+%C'
    response = requests.get(url)
    clima = response.text if response.status_code == 200 else "No se pudo obtener el clima."
    return clima
