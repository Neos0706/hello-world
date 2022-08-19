JSON_AS_ASCII = False


# 数据库配置
USERNAME = "root"
PASSWORD = ''
HOSTNAME = "127.0.0.1"
PORT = '3306'
DATABASE = 'python3'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "lxlxixlxxadddfs"

# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = "******@qq.com"
MAIL_PASSWORD = "******"
MAIL_DEFAULT_SENDER = "******@qq.com"


# 暂时测试session 过期事件
