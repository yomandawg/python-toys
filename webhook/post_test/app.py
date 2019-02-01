from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET']) ## methods 아무것도 안쓰면 GET인줄 앎
def index():
    return render_template('index.html')
    
@app.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    password = request.form.get('password')
    
    adminEmail = "qwer@qwer.com"
    adminPassword = "12341234"
    
    #만약에 회원가입한 회원이 admin일경우(관리자의 email and password),
    #   "관리자님 환영합니다.""
    #아닐경우
    #   "꺼지셈"
    if email == adminEmail and password == adminPassword:
        msg = "관리자님 환영합니다."
    else:
        if email == adminEmail:
            msg = "관리자님 비번이 틀렸어요"
        else: 
            msg = "꺼지셈"
    
    print(email, password)
    return render_template('signup.html', email = email, password = password, msg=msg)