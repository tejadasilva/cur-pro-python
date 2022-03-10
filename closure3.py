def make_multiplier(x):
    
    def multiplier(n):
        return x * n

    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))

# Respuesta
# PS C:\Users\matejada\py\cur-pro-python> py .\closure3.py
# 30
# 20
# 80