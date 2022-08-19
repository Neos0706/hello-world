from flask import Blueprint, render_template, request, redirect,url_for, jsonify, session, flash
from exts import mail, db
from flask_mail import Message
from models import EmailCpatchaModel, UserModel
import string
import random
from datetime import datetime
from.form import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
import random


bp = Blueprint('user', __name__, url_prefix="/user")


@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                # 这里的session为啥不随会话结束过期
                session['user_id'] = user.id
                # session.permanent = True
                # print(dir(session))
                # session['random'] = random.random()
                # print(session['random'])
                return redirect("/")
            else:
                flash("邮箱或者密码错误")
                return redirect(url_for("user.login"))
        else:
            flash("邮箱或者密码格式不对")
            return redirect(url_for("user.login"))


# @bp.route("/random")
# def check_random():
#     return str(session['random'])

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("user.login"))


@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            # 加密
            hash_password = generate_password_hash(password)
            user = UserModel(email=email, username=username, password=hash_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            return redirect(url_for("user.register"))


@bp.route("/captcha", methods=["POST"])
def get_captcha():
    email = request.form.get("email")
    # print(request.args)
    print(email)
    sample_pool = string.ascii_letters + string.digits
    captcha = ''.join(random.sample(sample_pool, 4))
    print(captcha)
    if email:
        messgae = Message(
            subject='测试邮件主题',
            recipients=[email],
            body=f"[知了问答] 你的注册验证吗：{captcha}"
        )
        mail.send(messgae)
        captcha_model = EmailCpatchaModel.query.filter_by(email=email).first()
        if captcha_model:
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.now()
            db.session.commit()
        else:
            captcha_model = EmailCpatchaModel(email=email, captcha=captcha)
            db.session.add(captcha_model)
            db.session.commit()
        return jsonify({'code': 200})
    else:
        return jsonify({'code': 400, 'message': '请检查邮箱'})