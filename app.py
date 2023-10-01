from flask import Flask
app = Flask(__name__)
@app.route('/')
def start():
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

    </main>

    <footer>
        Кривошеев Гавра, ФБИ-11, 3 курс
    </footer>
</body>
</html>
'''