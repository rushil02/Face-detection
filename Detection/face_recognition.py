#cv2 is for opencv
#os is for working with path of training data
import cv2, os
#numpy is important because images will be stored as a numpy array: faster and opencv can't read all image formats
import numpy as np
#PIL(pillow) is for working with images
from PIL import Image
import sys
sys.path.append("D:\Rushil\Workspace\Semester Project\Face detection")
from Next import cam_next
from Next import edge

images = None
labels = None
cam_id = 0
video_capture = None

path = None
#realtive path to the haar cascade classifier
classifierPath = "D:\Rushil\Workspace\Semester Project\Face detection\Detection\lbpcascade.xml"
#cascade classifier object
faceCascade = cv2.CascadeClassifier(classifierPath)


# create a local binary patters histogram face recognizer object
recognizer = cv2.createLBPHFaceRecognizer()

#edge.set_frame(mx,my)

#this function takes the absolute path to the training set, and then it extracts the 
#faces and labels and stores them in a tuple of 2 lists
def get_images_and_labels():
    global path
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.sad')]
    images = []
    labels = []
    for image_path in image_paths:
        image_pil = Image.open(image_path).convert('L')
        image = np.array(image_pil, 'uint8')
        nbr = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
        faces = faceCascade.detectMultiScale(
            image, 
            scaleFactor=1.1
            )
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(nbr)
            cv2.imshow("Preparing training data", image[y: y + h, x: x + w])
            cv2.waitKey(50)
    return images, labels

# path of training data
def pathpass(pathpass):
    global path
    path = pathpass
    print path
    train()

#call the function defined above and store faces and labels
def train():
    global images, labels, recognizer
    images, labels = get_images_and_labels()
    #destroy the windows that show up while preparing the dataset
    cv2.destroyAllWindows()
    #train the face recgonizer with appropriate arguments
    recognizer.train(images, np.array(labels))

def start():    
    video_cap()


    

#take video feed from webcam and perform the recognizer prediction on each frame
#draw rectangle around the detected face
#and label the rectangle if confidence is high
# p.s: the recognizer predicts with a certain confidence value
def video_cap():
    global labels, cam_id, video_capture
    label_comparer = list(set(labels))
    video_capture = cv2.VideoCapture(cam_id)
    while True:
        # capture frame
        ret, frame = video_capture.read()
        predict_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            predict_image,
            scaleFactor=1.3,
            minSize=(100, 100)
        	)
        for (x, y, w, h) in faces:
            nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
            if (nbr_predicted in label_comparer):
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.rectangle(predict_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                if conf<50:
                    cv2.putText(predict_image,'%s'%nbr_predicted ,(x+w,y+h), font,1,(255,255,255),1)
                cv2.imshow("face recognition", predict_image) #predict_image[y: y + h, x: x + w]
                print conf
                edge.last_obj_pos(x, y, w, h)
            else:
                cv2.imshow("face recognition", predict_image) #predict_image[y: y + h, x: x + w]
                searchnext()
                stop()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break        

    stop()
    

    #cam_id = cam_next.cam_next(cam_id,edge)
def searchnext():
    global cam_id
    edge = edge.set_side()
    cam_id = cam_next.cam_next(cam_id,edge)

#close all windows and stuff
def stop():
    global video_capture
    if video_capture is not None:
        video_capture.release()
    cv2.destroyAllWindows()