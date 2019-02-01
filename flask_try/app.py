from flask import Flask, render_template, request
from faker import Faker
import random
import csv

app = Flask(__name__
fake = Faker('ko_KR')
babos = {}

# fish = [["john","ashley"],["chris","mandy"]]

# '/' : 사용자의 이름을 입력 받습니다.
@app.route('/junsaeng')
def index():
    return render_template('junsaeng.html')
    
# '/pastlife' : 사용자의 (랜덤으로 생성된) 전생/직업을 보여준다.

@app.route('/pastlife')
def pastlife():
    username = request.args.get('username')
    if username in babos:
       fake_job = babos[username]
    else:
        fake_job = fake.job() 
        babos[username] = fake_job
    
    #fake_name = fake.name()
    #fake_address = fake.address()
    #fake_text = fake.text()
    return render_template('pastlife.html', username = username, fake_job = fake_job)


@app.route('/')
def landing():
    #두 사람의 이름을 입력받는다.
    return render_template('index.html')
    
@app.route('/match')
def match():
    me = request.args.get('me')
    you = request.args.get('you')
    rate = random.randint(50,100)
    #fish.append([me, you])
    
    #CSV파일을 통한 데이터 영구저장
    # f = open('fish.csv', 'a', encoding="utf-8")
    # fish = csv.writer(f)
    # fish.writerow([me, you])
    # f.close()
    with open('fish.csv', 'a', encoding="utf-8") as f: #파일 닫을 필요가 없어진다 끝나고 종료해줌, with = 오픈한 파일을 임시적으로 제어하고, 제어가 끝나면 자동으로 닫아줌
        fish = csv.writer(f)
        fish.writerow([me, you])
    
    if me in babos:
        score = babos[me]
    else:
        score = random.randint(0,100)
        babos[me] = score
        
    #1. fake궁합 알려주고,
    #2. 우리만 알 수 있게 저장한다.
    #   -fish라고 하는 리스트에 append 통해 저장한다.
    #3. match.html에는 두 사람의 이름과 random으로 생성된 50~100사이의 수를 함께 보여준다.
    #   ex) XX님과 YY의 궁합은 88%입니다.
    return render_template('match.html', me = me, you = you, rate = rate)
    
@app.route('/admin')
def admin():
    #낚인 사람들의 명단
    #   -template에서 반복(for)을 써서, fish에 들어가 있는 데이터를 모두 보여준다.
    # f = open('fish.csv', 'r', encoding='utf-8')
    # fish = csv.reader(f)
    # for row in fish:
    #     for d in row:
    #         print(d)
    # f.close()
    data = []
    
    # with open('fish.csv', 'r', encoding="utf-8") as f:
    #     fish_list = csv.reader(f)
    #         for fish in fish_list:
    #             data.append(fish)    
    
    with open('fish.csv', 'r', encoding="utf-8") as f:
        for fish in f:
            data.append(fish)    

    return render_template('admin.html',  fish = data)
    
    
    
