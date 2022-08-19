import datetime
import logging
from flask import Flask,render_template, g,session
import config
from blueprints import qa_bp, user_bp
from exts import db, mail
from flask_migrate import Migrate
from models import UserModel




app = Flask(__name__)
app.config.from_object(config)
# 注册蓝图
app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)
# app.permanent_session_lifetime = datetime.timedelta(seconds=10)

db.init_app(app)
mail.init_app(app)

# 创建数据迁移对象

migrate = Migrate(app, db)

@app.before_request
def before_request():
    # print("检查cookie里的session")
    user_id = session.get("user_id")
    # print(session.permanent)
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            g.user = user
        except:
            g.user = None


# 请求来了 -》 before_request ->  视图函数 -> 视图函数中返回模板 -> context_processor

@app.context_processor
def context_processor():
    if hasattr(g, "user"):
        return {"user": g.user}
    else:
        return {}



if __name__ == '__main__':
    app.run()
