from flask import Flask, jsonify
import time

app = Flask(__name__)

page_data = {
    "index": {
        "title": "Index API",
        "description": "This is a test page.",
        "keywords": "test, page, website"
    },
    "blog": {
        "title": "Blog API",
        "description": "This is a blog page.",
        "keywords": "blog, page, website"
    },
}


@app.route('/api/<page_name>', methods=['GET'])
def get_page_data(page_name):
    time.sleep(1)

    data = page_data.get(page_name, {})
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=5000)
