from flask import Flask, render_template, request, redirect
import data.db_session as session
from data.user import User
from data.result import Result
from data.rating import Rating
from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, EmailField, SearchField, SelectField, IntegerField, \
    SelectFieldBase, DateTimeField, SelectMultipleField, StringField
from wtforms.validators import DataRequired
from flask_login import LoginManager, logout_user, login_required, login_user
from flask_restful import abort, Api
from data.users_resourse import ResListResource
from data.res_resourse import RatListResource

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)

login_manager = LoginManager()
login_manager.init_app(app)


class RatingForm(FlaskForm):
    jobs = []


class LoginForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])

    email = EmailField('Email', validators=[DataRequired()])

    submit = SubmitField('Log in')


@login_manager.user_loader
def load_user(user_id):
    db_sess = session.create_session()
    return db_sess.query(User).get(user_id)


class RegistrationForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Password again', validators=[DataRequired()])

    email = EmailField('Email', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])

    submit = SubmitField('Sign up')


@app.route('/', methods=['POST', 'GET'])
@app.route('/registration', methods=['POST', 'GET'])
def astronaut_selection():
    form = RegistrationForm()
    db_session = session.create_session()
    if request.method == 'GET':
        return render_template('astronaut_selection.html', title='Регистрация', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if form.password.data != form.password_again.data:
                return render_template('astronaut_selection.html', title='Registration', form=form,
                                       message="Passwords are not the same")

            if db_session.query(User).filter(User.email == form.email.data).first():
                return render_template('astronaut_selection.html', title='Registration', form=form,
                                       message="Opps, the current email is already used")

            user = User(
                email=form.email.data,
                nickname=form.name.data,
            )
            user.set_password(form.password.data)
            user.password = user.hashed_password
            db_session.add(user)
            db_session.commit()
        return redirect('/result')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    db_session = session.create_session()
    if form.validate_on_submit():
        user = db_session.query(User).filter(User.email == form.email.data).first()
        if not user:
            return render_template("login.html",
                                   message="Неправильный логин или пароль",
                                   form=form)
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/result")
        return render_template("login.html",
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template("login.html", title="Авторизация", form=form)


@app.route('/rating', methods=['GET'])
@login_required
def rating():
    form = RatingForm
    db_sess = session.create_session()
    form.jobs = db_sess.query(Result.nickname, Result.result).order_by(Result.result).all()
    form.jobs.reverse()
    return render_template('rating.html', form=form)


@app.route('/result', methods=['GET'])
@login_required
def rating1():
    form = RatingForm
    db_sess = session.create_session()
    form.jobs = db_sess.query(Rating.nickname, Rating.result).all()
    form.jobs.reverse()
    return render_template('result.html', form=form)


if __name__ == '__main__':
    session.global_init("db/blogs.db")
    api.add_resource(ResListResource, '/post')
    api.add_resource(RatListResource, '/post1')
    app.run(port=8000, host='127.0.0.1')
