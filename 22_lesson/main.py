from flask import Flask # Вытащил объект


app = Flask(__name__)


@app.route('/<x>/<y>') # Создание главной страницы
def main(x, y):
    return str(int(x) + int(y)) # Convert.ToInt32("54");


app.run(port=8080)
