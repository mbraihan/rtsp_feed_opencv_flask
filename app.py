from flask import Flask, render_template, Response
from flask_cors import CORS, cross_origin
import urllib
import os
# import helper
import re
from urllib.request import urlopen
from flask import jsonify
import cv2
import imutils
from imutils.video import VideoStream

# * ---------- Create App --------- *
app = Flask(__name__)
# CORS(app)


# rtsp_url = "rtsp://admin:Experts@2021!@@24.186.96.191:554/ch01/0"
# rtsp_url2 = "rtsp://admin:Experts@2021!@@10.10.10.115:554/ch01/0"

u = "admin"
p = "Experts@2021!@"
i = "24.186.96.191"
po = "554"
c = "ch01"
s = "0"

rtsp = "rtsp://" + u + ":" + p + "@" + i + ":" + po + "/" + c + "/" + s
print(rtsp)

# rtsp_url = "rtsp://<camera_name>:<some_uuid>@<some_ip>/live"
rtsp_url = rtsp

vs = VideoStream(rtsp_url).start()
# vs2 = VideoStream(rtsp_url2).start()


def gen_frames():
    while True:
        frame = vs.read()
        if frame is None:
            continue
        else:
            frame, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/rtsp_feed', methods=['GET'])
# @cross_origin(supports_credentials=True)
def rtsp_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


# * ---------- Get home information ---------- *

@app.route('/', methods=['GET'])
# @cross_origin(supports_credentials=True)
def index():
    return render_template('index.html')

@app.route('/products-training', methods=['GET'])
# @cross_origin(supports_credentials=True)
def productsTraining():
    return render_template('productsTraining.html')

@app.route('/new-station', methods=['GET'])
# @cross_origin(supports_credentials=True)
def newStation():
    return render_template('newStation.html')

@app.route('/my-account', methods=['GET'])
# @cross_origin(supports_credentials=True)
def myAccount():
    return render_template('myAccount.html')


if __name__ == '__main__':
#     app.run(host = '0.0.0.0', port = 8889, debug=True, ssl_context='adhoc')
    app.run(host = '0.0.0.0', port = 8889, debug=True)
