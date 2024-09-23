import math

def triangle_rectangle(a, b, c):
    if math.isclose(a**2 + b**2, c**2):
        return 'Triangle Rectangle'
    else:
        return 'Triangle pas Rectangle'

# Longeur des cotés
a = 18* math.sqrt(2)
b = 23 * math.sqrt(2)
c = 14 * math.sqrt(10)

# Verifier si triangle rectaangle
result = triangle_rectangle(a, b, c)
print(result)
