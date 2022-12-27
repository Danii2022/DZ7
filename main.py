result = []

try:
    def divider(a, b):
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        return a / b
except ValueError:
    print('Ошибка')
except IndexError:
    print('Ошибка')

try:
    data = {10, 2, 2, 5, 123, 4, 18, 0, 15, 8, 4}
    for key in data:
        res = divider(key, data[res])
        result.append(res)
except NameError:
    print('Ошибка названия')
finally:
    print(data)

print(result)
