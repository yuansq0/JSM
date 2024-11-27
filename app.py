from flask import Flask, render_template, request

app = Flask(__name__)

# 预定义用户名和密码
VALID_USERNAME = "sqy"
VALID_PASSWORD = "qq"

@app.route('/')
def home():
    # 渲染登录页面
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # 获取表单数据
    username = request.form.get('username')
    password = request.form.get('password')

    # 验证用户名和密码
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return f"<h1>Welcome, {username}!</h1>"
    else:
        # 提供错误信息并返回登录页面
        return render_template('index.html', error="Invalid username or password!")

if __name__ == '__main__':
    app.run(debug=True)
