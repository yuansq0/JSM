from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# 用户名和加密后的密码（安全存储密码）
VALID_USERNAME = "sqy"
VALID_PASSWORD_HASH = generate_password_hash("qq")  # 加密存储密码

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # 验证用户名和密码
    if username == VALID_USERNAME and check_password_hash(VALID_PASSWORD_HASH, password):
        return f"Welcome, {username}!"
    else:
        flash('Invalid username or password!')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
