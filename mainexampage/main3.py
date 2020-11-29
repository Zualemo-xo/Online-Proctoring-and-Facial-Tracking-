from flask import Flask, render_template,redirect, request, Response
from camera import VideoCamera
import os
from gevent.pywsgi import WSGIServer
import mysql.connector
#import pyrebase
app = Flask(__name__)
#app.secret_key=os.urandom(24)
conn=mysql.connector.connect(host="remotemysql.com",user="",password="",database="")
#enter valid credentials from onlinemysql
cursor=conn.cursor()

@app.route('/faculty')
def homez():
    return render_template('sss.html')

@app.route('/home')
def home():
    return render_template('index1.html')

@app.route('/features')
def features():
    return render_template('Features.html')

@app.route('/contact',methods=['GET', 'POST'])
#@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/exam')
def exam():
    return render_template('newindex.html')

@app.route('/marks',methods=['POST','GET'])
def marks():
    marks=request.form.get('marks')
    email=request.form.get('email')

    cursor.execute("""INSERT INTO `faculty` (`email`,'marks') VALUES 
    ('{}','{}')""".format(email,marks))
    conn.commit()
    return "Marks registered successfully"

@app.route('/login_validation',methods=['POST','GET'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    cursor.execute("""SELECT * FROM `login` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password)) 
    login=cursor.fetchall()
    
    if len(login)>0:
        return render_template('newindex.html')
    else:
        return render_template('login.html')

  
    
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    http_server = WSGIServer(('0.0.0.0', port), app)
    http_server.serve_forever()
    #app.run(host='0.0.0.0', port=8000, debug=True)
