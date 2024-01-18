from django.shortcuts import render, redirect
from random import randint

def randomizer(request):
    if request.method == 'POST':
        inp_count_command = int(request.POST['inp_count_command'])
        inp_names = request.POST.getlist('inp_name[]')

        if len(inp_names) < inp_count_command:
            return render(request, 'error.html', {'message': 'Мало участников'})

        command_result = []
        command_adding = []

        while len(inp_names) > 0:
            r = randint(0, len(inp_names) - 1)
            if inp_names[r] not in command_adding:
                command_adding.append(inp_names[r])
                inp_names.pop(r)
            else:
                inp_names.pop(r)

            if len(command_adding) == inp_count_command or len(inp_names) == 0:
                command_result.append(command_adding)
                command_adding = []

        # Сохраняем результат в сессии
        request.session['command_result'] = command_result

        return redirect('result')  # Переходим на страницу с результатами

    return render(request, 'randomizer.html', {'names_entered': 0})


def result(request):
    command_result = request.session.get('command_result', [])

    if not command_result:
        return redirect('randomizer')  # Если результаты не определены, перенаправляем на страницу с формой

    return render(request, 'result.html', {'command_result': command_result})
