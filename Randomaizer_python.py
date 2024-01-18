# Функции для рандомного разделения на команды
from random import randint

lst_people = []
def randomaizer(lst: list):
    inp_count_command =  int(input('Ведите кол-во участников в одной команде: '))
    command_result = []
    command_adding = []
    if inp_count_command > len(lst):
        return 'Мало участников'

    while len(lst) > 0:
        r = randint(0, len(lst)-1)
        if lst[r] not in command_adding:
            command_adding.append(lst[r])
            lst.pop(r)
        else:
            lst.pop(r)

        if len(command_adding) == inp_count_command or len(lst) == 0:
            command_result.append(command_adding)
            command_adding = []

    return command_result

while True:
    inp_start_or_stop = input('1) Добавить участника\n2) Далее\nВыберите вариант: ')
    if inp_start_or_stop == '1':
        inp_name = input("\nВведите имя участника: ")
        if inp_name in lst_people:
            print('Имя участника занято!\n')
        else:
            lst_people.append(inp_name)
    elif inp_start_or_stop == '2':
        print(randomaizer(lst_people))
        break
    else:
        pass