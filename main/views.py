'''Управление страницами и логикой игры'''
from django.shortcuts import render, redirect
from .models import Task


def index(request):
    '''Отображает главную страницу'''
    return render(request, 'main/index.html')


def about(request):
    '''Отображает страницу с информацией о проекте'''
    return render(request, 'main/about.html')


def registration(request):
    '''Управляет регистрацией'''
    if request.method == "GET":
        request.session.flush()

    if request.method == "POST":
        request.session['first_name'] = request.POST.get('first_name')
        request.session['last_name'] = request.POST.get('last_name')
        request.session['step'] = 0
        request.session['score'] = 0
        return redirect('game')

    return render(request, 'main/registration.html')


def game(request):
    '''Логика игры'''
    tasks = Task.objects.all()

    if 'first_name' not in request.session:
        return redirect('registration')

    if not tasks.exists():
        return render(request, 'main/game.html', {'error': 'Добавьте вопросы!'})

    step = request.session.get('step', 0)

    if step >= tasks.count():
        result_data = {
            'score': request.session.get('score'),
            'total': tasks.count(),
            'first_name': request.session.get('first_name'),
            'last_name': request.session.get('last_name'),
        }

        request.session['step'] = 0
        request.session['score'] = 0
        return render(request, 'main/result.html', result_data)

    current_task = tasks[step]

    if request.method == "POST":
        answer = request.POST.get('answer')
        if answer == current_task.correct:
            request.session['score'] = request.session.get('score', 0) + 1
        request.session['step'] = step + 1
        return redirect('game')

    context = {
        'question': current_task,
        'current_number': step + 1,
        'total_count': tasks.count()
    }
    return render(request, 'main/game.html', context)


def contacts(request):
    '''Обработка формы обратной связи'''
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Новое сообщение! Имя: {name}, Email: {email}, Текст: {message}")
        return render(request, 'main/contacts.html', {'success': True})

    return render(request, 'main/contacts.html')