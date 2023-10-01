from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def start():
    return redirect ('/menu', code=302)
@app.route('/lab1')
def lab1():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Кривошеев/Гавра</title>
</head>
<body>
    <header>
        Кривошеев Гавра, ФБИ-11, 3 курс
    </header>

    <main> 
        Flask — фреймворк для создания веб-приложений на языке
программирования Python, использующий набор инструментов
Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
называемых микрофреймворков — минималистичных каркасов

веб-приложений, сознательно предоставляющих лишь самые ба-
зовые возможности.
        <h1><a href='/lab1/dub'>Дуб</h1>
    </main>

    <footer>
        Кривошеев Гавра, ФБИ-11, 3 курс
    </footer>
</body>
</html>
'''
@app.route('/menu')
def menu():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Кривошеев/Гавра</title>
</head>
<body>
    <header>
        Кривошеев Гавра, ФБИ-11, 3 курс
    </header>

    <main> 
        <h1><a href='/lab1'>Лаба 1</h1>
    </main>

    <footer>
        Кривошеев Гавра, ФБИ-11, 3 курс
    </footer>
</body>
</html>
'''
@app.route('/lab2/example')
def example():
    name = "Кривошеев М.С. и Гавра В.А."
    lab_num = "Лабораторная работа №2"
    course = '3 курс'
    group = 'ФБИ-11'
    books = [ {'name': 'Убийство в Восточном экспрессе', 'year': 1934},
        {'name': 'Тайна трех актрис', 'year': 1956},
        {'name': 'Маленькие убийства Агаты Кристи', 'year': 1954},
        {'name': 'Смерть на Ниле', 'year': 1937},
        {'name': '10 негритят', 'year': 1939},        
        {'name': 'Потерянное сокровище', 'year': 1925},
        {'name': 'Потерянное в Месопотамии', 'year': 1936},
        {'name': 'Загадка Эндхауза', 'year': 1946},
        {'name': 'Сеанс', 'year': 1920},
        {'name': 'Убийство Роджера Экройда', 'year': 1926},]
    fruits = [
        {'name': 'апельсины', 'price': 100},
        {'name': 'яблоки', 'price': 200},
        {'name': 'манго', 'price': 300},
        {'name': 'мандарины', 'price': 400},
        {'name': 'лимон', 'price': 500},

    ]
    return render_template('example.html', lab_num=lab_num, course=course, group=group, name=name, fruits=fruits, books=books)