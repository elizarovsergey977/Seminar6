# Семинар 5 задача 1 - Удаление слова в тексте по фрагменту
# str = input('Введите строку').split()
# fragment = input('Введите фрагмент')
# str1 = ' '.join(list(filter(lambda x: (fragment not in x), str)))
# print(str1)

# Семинар  2 Задайте список из четных элементов
# data = [x for x in range(10)]
# res = list(filter(lambda x: not x%2, data))
# print(res)

# Семинар 2. Задайте список из N элементов, заполненных числами из
# промежутка [-N, N].
# num = int(input('Введите число '))
# lst = [i for i in range(-num, num+1)]
# sum = 1
# with open('text') as text:
#     index = list(map(int, text.readlines()))
# for i in range(len(index)):
#     sum *= lst[index[i]]
# print(lst)
# print(sum)


ln_in = input('Введите выражение: ').split()

print(ln_in)


def aka_eval(args):
    while len(args) != 1:
        while '*' in args or '/' in args:
            try:
                prod_index = args.index('*')
            except:
                prod_index = 100
            try:
                div_index = args.index('/')
            except:
                div_index = 100

            if prod_index < div_index:
                args[prod_index - 1] = int(args[prod_index - 1]) * int(args[prod_index + 1])
                args.pop(prod_index + 1)
                args.pop(prod_index)
            else:
                args[div_index - 1] = int(args[div_index - 1]) / int(args[div_index + 1])
                args.pop(div_index + 1)
                args.pop(div_index)

        while '+' in args or '-' in args:
            try:
                sum_index = args.index('+')
            except:
                sum_index = 100
            try:
                deg_index = args.index('-')
            except:
                deg_index = 100

            if sum_index < deg_index:
                args[sum_index - 1] = int(args[sum_index - 1]) + int(args[sum_index + 1])
                args.pop(sum_index + 1)
                args.pop(sum_index)
            else:
                args[deg_index - 1] = int(args[deg_index - 1]) - int(args[deg_index + 1])
                args.pop(deg_index + 1)
                args.pop(deg_index)
    return args[0]


while '(' in ln_in:
    close_bracket = ln_in.index(')')
    for i in range(close_bracket):
        if ln_in[i] == '(':
            open_bracket = i
    inside_ln_in = ln_in[open_bracket + 1:close_bracket]
    number = aka_eval(inside_ln_in)
    ln_in[open_bracket:close_bracket + 1] = str(number)
aka_eval(ln_in)

print(f'Результат вычисления: {ln_in[0]}')