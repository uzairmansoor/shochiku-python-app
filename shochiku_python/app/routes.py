from flask import request

from utils.open_ai import get_keywords
from utils.hugging_face import get_image_from_text, get_image_from_image

from app import app


@app.route('/text-to-image', methods=['GET', 'POST'])
def text_to_image():
    """
    Generate an image from text
    :return: a json response containing the image url
    """

    data = request.get_json()
    response = get_image_from_text(data)
    return response


@app.route('/image-to-image', methods=['GET', 'POST'])
def image_to_image():
    """
    Generate an image from image
    :return: a json response containing the image url
    """

    data = request.get_json()
    response = get_image_from_image(data)
    return response


@app.route('/get-keywords', methods=['GET', 'POST'])
def keywords():
    req = request.get_json()
    res = get_keywords(req)
    return res


@app.route('/')
@app.route('/ping', methods=['GET'])
def ping():
    return 'pong!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
