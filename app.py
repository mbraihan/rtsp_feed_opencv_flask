from flask import Flask, render_template, Response
from flask_cors import CORS, cross_origin
import urllib
import os
import helper
import re
from urllib.request import urlopen
import json
# from flask_swagger_ui import get_swagger_ui_blueprint
import cv2

# * ---------- Create App --------- *
app = Flask(__name__)
CORS(app, support_credentials=True)

# * ---------- Get home information ---------- *
# @app.route('/', methods=['GET'])
# @cross_origin(supports_credentials=True)
# def get_message():
#     return jsonify("RTSP Feed Streaming"), 200


camera = cv2.VideoCapture(
    'rtsp://admin:Experts@2021!@@24.186.96.191:554/ch01/0')


def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/rtsp_feed')
@cross_origin(supports_credentials=True)
def rtsp_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# * ---------- Get home information ---------- *


@app.route('/', methods=['GET'])
@cross_origin(supports_credentials=True)
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
