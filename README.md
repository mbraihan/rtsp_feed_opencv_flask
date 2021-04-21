# RTSP Feed via OpenCV and Flask

A Flask based web-app to strea live CCTV feed

### To test with webcam use

`cv2.VideoCapture(0)`

### Use Ip Camera/CCTV/RTSP Link

`cv2.VideoCapture('rtsp://username:password@camera_ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp') `

### Example RTSP Link

`cv2.VideoCapture('rtsp://mamun:123456@101.134.16.117:554/user=mamun_password=123456_channel=0_stream=0.sdp')`

### Change Channel Number to Change the Camera

`cv2.VideoCapture('rtsp://mamun:123456@101.134.16.117:554/user=mamun_password=123456_channel=1_stream=0.sdp')`

### Display the resulting frame in browser

`cv2.imencode('.jpg', frame)[1].tobytes()`

### Or this one

```
net , buffer = cv2.imencode('.jpg', frame)
buffer.tobytes()
```
