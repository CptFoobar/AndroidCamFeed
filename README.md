## DroidCam

A cute little utility to use in conjunction with [IP WebCam](https://play.google.com/store/apps/details?id=com.pas.webcam) android application.

### Description

Webcams come in handy when we are using OpenCV for real-time Image Processing. But often we don't have access to one (or the one we have is too crappy). So, here is a nice utility to use your mobile phone/tablet's camera for processing in OpenCV.

### Usage

AndroidCamFeed provides a `cv2.VideoCapture` like interface. Super-easy to use. A usage example can be found in the [Example.py](https://github.com/TigerKid001/AndroidCamFeed/Example.py).

Run this example from terminal as:

`python acf.py 192.168.1.2:8080`

Simply replace the IP and the port with the one for your device.

### Requisites

This module works with [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam) android application.

_____

Code adopted from [this stackoverflow question](http://stackoverflow.com/questions/21702477/how-to-parse-mjpeg-http-stream-from-ip-camera)
 and [this Gist](https://gist.github.com/shihyuan/4d834d429763e953a40c).
