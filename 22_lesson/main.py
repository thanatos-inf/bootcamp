from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('base.html', title='Главная страница')


@app.route('/listofsomething')
def second():
    
    name = ['Укроп', 'Марина', 'Колесо', 'Боярышник', 'BitCoin']
    return render_template('listofsomething.html', name=name,
                             title='Произвольный список')


@app.route('/portfolio')
def third():
    return render_template('portfolio.html', title='Контактные данные')
    
@app.route('/warning')
def fourth():
    return render_template('warning.html', title='ЗАЧЕМ?!')



if __name__ == '__main__':
    app.run()


