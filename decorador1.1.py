def decorardor(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()
    return envoltura

@decorardor
def saludo():
    print('Hola!')

saludo()

