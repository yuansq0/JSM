from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # 用于闪存消息

# 预定义用户名和密码
VALID_USERNAME = "nngf1"
VALID_PASSWORD = "nngf2"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return f"Welcome, {username}!"
    else:
        flash('Invalid username or password!')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
