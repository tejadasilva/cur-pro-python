# CLOSURE
# Cuando una variable que esta en un scope superior es recordada en un scope inferior

def main():
    a = 1

    def nested():
        print(a)
    return nested

my_func = main()
my_func()

# Respuesta:
# (venv) PS C:\Users\matejada\py\cur-pro-python> py .\closure.py
# 1
# Lo que se devuelve es la funcion nested

