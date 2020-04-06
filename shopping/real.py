from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    option_receive = request.form['option_give']
    add_receive = request.form['add_give']
    tel_receive = request.form['tel_give']

    order = {
        'name': name_receive,
        'option': option_receive,
        'add': add_receive,
        'tel': tel_receive
    }

    db.order_get.insert_one(order)
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 되었습니다.'})


@app.route('/orders', methods=['GET'])
def get_order():
    orders = list(db.order_get.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'order_get': orders})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)

# from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
