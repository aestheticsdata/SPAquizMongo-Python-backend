from flask import Flask, jsonify, request, abort
from flask.ext.pymongo import PyMongo
from flask_cors import CORS

import math
import random


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'quiz'
app.config['MONGO_HOST'] = '1990computer.com'

CORS(app)

mongo = PyMongo(app)


@app.route('/login', methods=['POST'])
def get_questions_after_login():

    request_json = request.get_json()

    print(request_json)

    if not (request_json['username'] == '<put the user here in prod>' and
            request_json['password'] == '<put the password here in prod>'):
        abort(401)
    else:
        questions = mongo.db.questions

        output = []

        for q in questions.find():
            output.append({'question': q['question'],
                           'choices': q['choices'],
                           'correctAnswer': q['correctAnswer']})

        shuffle(output)

    return jsonify(result=output)


def shuffle(a):
    for i in range(len(a)):
        j = math.floor(random.random()*i)
        tmp = a[i-1]
        a[i-1] = a[j]
        a[j] = tmp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
