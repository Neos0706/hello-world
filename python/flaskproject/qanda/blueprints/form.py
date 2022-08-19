import wtforms
from wtforms.validators import length,email,EqualTo,InputRequired
from models import EmailCpatchaModel, UserModel


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[email()])
    password = wtforms.StringField(validators=[length(min=6, max=20)])

class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3,max=20)])
    email = wtforms.StringField(validators=[email()])
    password = wtforms.StringField(validators=[length(min=6,max=20)])
    password_confirm = wtforms.StringField(validators=[EqualTo('password')])
    captcha = wtforms.StringField(validators=[length(min=4, max=4)])

    # 验证码校验
    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCpatchaModel.query.filter_by(email=email).first()
        if not captcha_model or captcha.lower() != captcha_model.captcha.lower():
            raise wtforms.ValidationError("邮箱验证吗错误")

    # 验证邮箱是否存在
    def validate_email(self, field):
        email = field.data
        user_model = UserModel.query.filter_by(email=email).first()
        if user_model:
            raise wtforms.ValidationError("邮箱已经存在！")


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[length(min=3, max=100)])
    content = wtforms.StringField(validators=[length(min=5)])


class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[InputRequired()])