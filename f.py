from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return render_template('astronaut_selection.html', title='Регистрация')
    elif request.method == 'POST':
        select = {}
        select['surname'] = request.form['surname']
        select['name'] = request.form['name']
        select['email'] = request.form['email']
        select['education'] = request.form['education']
        select['prof1'] = request.form['prof1']
        select['prof2'] = request.form['prof2']
        select['prof3'] = request.form['prof2']
        select['sex'] = request.form['sex']
        select['about'] = request.form['about']
        select['accept'] = request.form['accept']
        return render_template('success.html', data=select, title="Успешно")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
