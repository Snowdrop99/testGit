
from flask import Flask,g,request,render_template
from utils import login_log,login_ip

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login/',methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        g.username = username
        g.ip = password
        login_log()
        login_ip()
        return u'恭喜登录成功！'

if __name__ == '__main__':
    app.run()