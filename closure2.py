#la nested function esta recordando una variable de un scope superiordef main():
def main():
    a = 1

    def nested():
        print(a)
    return nested

my_func = main()
my_func()

del(main)
my_func()

#respuesta
# PS C:\Users\matejada\py\cur-pro-python> py .\closure2.py
# 1
# 1