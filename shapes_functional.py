import math

shapes = [
    ('rectangle', 5, 6),
    ('square', 7),
    ('circle', 2),
    ('ellipse', 4, 5),
    ('rectangle', 4, 7)
]

area = 0
for s in shapes:
    shape_name = s[0]
    if shape_name == 'rectangle':
        a_s = s[1] * s[2]
        print(f'Rectangle with a={s[1]} and b={s[2]}, area: {a_s}')
    elif shape_name == 'square':
        a_s = s[1]**2
        print(f'Square with a={s[1]}, area: {a_s}')
    elif shape_name == 'circle':
        a_s = s[1]**2*math.pi
        print(f'Circle with r={s[1]}, area: {a_s}')
    elif shape_name == 'ellipse':
        a_s = s[1] * s[2] * math.pi
        print(f'Ellipse with a={s[1]} and b={s[2]}, area: {a_s}')

    area += a_s

print(f'Full area: {area}')

