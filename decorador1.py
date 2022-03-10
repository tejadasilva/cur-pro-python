def decorardor(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()
    return envoltura

def saludo():
    print('Hola!')
saludo = decorardor(saludo)

saludo()

#resultado
# (venv) PS C:\Users\matejada\py\cur-pro-python> py .\decorador.py
# Esto se añade a mi función original
# Hola!