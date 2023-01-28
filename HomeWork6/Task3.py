# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in  "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out  {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

def catalog(*args):
    names_word = {}
    for i in sorted(args):
        letter = i[0]
        if letter not in names_word:
            names_word[letter] = [i]
        else:
            names_word[letter] += [i]

    return names_word

print(catalog("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка"))

