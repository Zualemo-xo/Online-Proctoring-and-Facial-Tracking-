
from flask import Flask, render_template, Response
from camera import VideoCamera
import webbrowser
import sys
import time



app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')



def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



def main():
    #sites=r"website.txt"
    #sites="http://0.0.0.0:5000/"
    #browser ="chrome"
    chrome_path=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chrome_path))
    web = webbrowser.get("chrome")
    webbrowser.open_new_tab("http://localhost:5000/")
    '''with open(sites) as fobj:
        try:
            for num,url in enumerate(fobj):
                web.open_new_tab(url.strip())
                time.sleep(1)
        except Exception as e:
            print(e)'''


if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0')
