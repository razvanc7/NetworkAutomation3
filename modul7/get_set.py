class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

t = Triangle(1, 1, 1)

change = input('Provide len for new side ex: (a: 2)').strip('( )').strip(':')
key, value  = list(map(lambda _: int(_.strip()) if _.strip().isdigit() else _.strip(),  change.split(':')))
print(type(key), type(value))

# if key == 'a':
#     t.a = 2

setattr(t, key, value)
print(getattr(t, key))