from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
db = SQLAlchemy(app)

news = [
    {
        'id': 1,
        'title': '',
        'image': '',
        'pud_date': '',
        'parsed_at': ''
    },
]


@app.route('/metro-news/api/v1.0/news', methods=['GET'])
def get_news():
    return jsonify({'news': news})


if __name__ == '__main__':
    app.run(debug=True)
