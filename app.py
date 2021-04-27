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
import imutils
from imutils.video import VideoStream

# * ---------- Create App --------- *
app = Flask(__name__)
CORS(app, support_credentials=True)

* ---------- Get home information ---------- *
@app.route('/', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_message():
    return jsonify("RTSP Feed Streaming"), 200


rtsp_url = "rtsp://<camera_name>:<some_uuid>@<some_ip>/live"

vs = VideoStream(rtsp_url).start()


def gen_frames():
    while True:
        frame = vs.read()
        if frame is None:
            continue
        else:
            frame, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/rtsp_feed_raw')
@cross_origin(supports_credentials=True)
def rtsp_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# * ---------- Get home information ---------- *


@app.route('/rtsp_feed', methods=['GET'])
@cross_origin(supports_credentials=True)
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
