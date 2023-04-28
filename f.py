from flask import Flask, render_template, request, redirect
import data.db_session as session
from data.user import User
from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, EmailField, SearchField, SelectField, IntegerField, \
    SelectFieldBase, DateTimeField, SelectMultipleField, StringField
from wtforms.validators import DataRequired
from flask_login import LoginManager, logout_user, login_required, login_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
session.global_init("db/blogs.db")
db_session = session.create_session()
class LoginForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])

    email = EmailField('Email', validators=[DataRequired()])

    submit = SubmitField('Sign up')


@login_manager.user_loader
def load_user(user_id):
    return db_session.query(User).get(user_id)


class RegistrationForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Password again', validators=[DataRequired()])

    email = EmailField('Email', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])

    submit = SubmitField('Sign up')


@app.route('/refistration', methods=['POST', 'GET'])
def astronaut_selection():
    form = RegistrationForm()
    db_session = session.create_session()
    if request.method == 'GET':
        return render_template('astronaut_selection.html', title='Регистрация', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if form.password.data != form.password_again.data:
                return render_template('signup.html', title='Registration', form=form,
                                       message="Passwords are not the same")

            if db_session.query(User).filter(User.email == form.email.data).first():
                return render_template('signup.html', title='Registration', form=form,
                                       message="Opps, the current email is already used")

            user = User(
                email=form.email.data,
                nickname=form.name.data,
            )
            user.set_password(form.password.data)
            user.password = user.hashed_password
            db_session.add(user)
            db_session.commit()
        select = {}
        select['education'] = request.form['education']
        select['prof1'] = request.form['prof1']
        select['prof2'] = request.form['prof2']
        select['prof3'] = request.form['prof2']
        select['sex'] = request.form['sex']
        select['about'] = request.form['about']
        select['accept'] = request.form['accept']
        return render_template('success.html', data=select, title="Успешно")


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    db_session = session.create_session()
    if form.validate_on_submit():
        user = db_session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        return render_template("login.html",
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template("login.html", title="Авторизация", form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
