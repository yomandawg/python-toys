from flask import Flask, render_template, request, redirect

app = Flask(__name__) # hey flask, make an app for me



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/session", methods=['POST'])
def session():
    email = request.form.get('email')
    password = request.form.get('password')

    # 유저 1명 뿐: asdf@asdf.com & 12341234
    username = "asdf@asdf.com"
    userkey = "12341234"

    # 로그인 판별
    if email == username and password == userkey:
        msg = "로그인이 되었습니다."
        # return render_template('index.html', msg=msg)
        # what's the difference?
        return redirect("/") # using redirection
    else:
        msg = "로그인이 되지 않았습니다."
        return render_template('session.html', msg=msg)

    return render_template('session.html', msg=msg) # login fail=go back

# Flask server 껐다켰다 귀찮을 때 자동갱신 기능
if __name__ == "__main__":
    app.run(debug=True)