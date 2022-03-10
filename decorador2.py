def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

print(mensaje('Cesar'))

# resultado
# (venv) PS C:\Users\matejada\py\cur-pro-python> py .\decorador2.py  
# CESAR, RECIBISTE UN MENSAJE