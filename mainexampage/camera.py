import cv2
from gaze_tracking import GazeTracking
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
ds_factor=0.6

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        '''success, image = self.video.read()
        image=cv2.resize(image,None,fx=ds_factor,fy=ds_factor,interpolation=cv2.INTER_AREA)
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        face_rects=face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in face_rects:
        	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        	break
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()'''
        gaze = GazeTracking()
        webcam = cv2.VideoCapture(0)
        
        while True:
            # We get a new frame from the webcam
            _, frame = webcam.read()
        
            # We send this frame to GazeTracking to analyze it
            gaze.refresh(frame)
        
            frame = gaze.annotated_frame()
            text = ""
        
            if gaze.is_blinking():
                text = "Blinking"
            elif gaze.is_right():
                text = "Looking right,please look at the screen"
            elif gaze.is_left():
                text = "Looking left,please look at the screen"
            elif gaze.is_center():
                text = "Looking center"
        
            cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
        
            left_pupil = gaze.pupil_left_coords()
            right_pupil = gaze.pupil_right_coords()
            cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
            cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        
            '''cv2.imshow("Demo", frame)
            if cv2.waitKey(1) == 27:
                break'''
            #comment lower part and decomment upper part for unique tab
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
        

