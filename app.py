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
    return render_template('example.html')