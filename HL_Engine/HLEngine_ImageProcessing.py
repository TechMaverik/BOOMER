#author:Akhil P Jacob
#HLDynamic-Integrations
import cv2
from PIL import Image
#import face_recognition
import numpy
from vidgear.gears.stabilizer import Stabilizer
from vidgear.gears import WriteGear


def camSnap(location,frameName,cam):
    try:
        camera = cv2.VideoCapture(cam)
        while True:
            return_value, image = camera.read()
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imshow(frameName, gray)
            if cv2.waitKey(1) & 0xFF == ord('x'):
                cv2.imwrite(location, gray)
                break
        camera.release()
        cv2.destroyAllWindows()
    except:
        return ("HLEngine:Camera not connected")


def showImage(location,frameName):
    img = cv2.imread(location)
    cv2.imshow(frameName, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()






def liveCam_filter(filter,cam,frameName):
    try:
        cap = cv2.VideoCapture(cam)

        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier(filter)
        framer=frameName
        while (True):

            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            net = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
                # flags = cv2.CV_HAAR_SCALE_IMAGE
            )

            #print(format(len(net)))
            # print (len(faces))
            if (len(net) >= 2):
                return (True)



            # Draw a rectangle around the faces
            for (x, y, w, h) in net:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow(framer, frame)
            if cv2.waitKey(1) & 0xFF == ord('x'):
                break


        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
    except:
        return ("HLEngine: An issue with camera or params")




def stabilization_cam(cam):
    stream = cv2.VideoCapture(cam) 

    #initiate stabilizer object with default parameters
    stab = Stabilizer()

    # loop over
    while True:

        # read frames from stream
        (grabbed, frame) = stream.read()

        # check for frame if not grabbed
        if not grabbed:
            break

        # send current frame to stabilizer for processing
        stabilized_frame = stab.stabilize(frame)
        
        # wait for stabilizer which still be initializing
        if stabilized_frame is None:
            continue 


        # {do something with the frame here}
        

        # Show output window
        cv2.imshow("Stabilized Frame", stabilized_frame)

        # check for 'q' key if pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord("x"):
            break

    
    

    #clear stabilizer resources
    stab.clean()

    # safely close video stream
    stream.release()




def stream_stabilization(video_path,video_saving_path):
    # Open suitable video stream
    stream = cv2.VideoCapture(video_path) 

    #initiate stabilizer object with default parameters
    stab = Stabilizer()

    # Define writer with default parameters and suitable output filename for e.g. `Output.mp4`
    writer = WriteGear(output_filename = video_saving_path) 

    # loop over
    while True:

        # read frames from stream
        (grabbed, frame) = stream.read()

        # check for frame if not grabbed
        if not grabbed:
            break

        # send current frame to stabilizer for processing
        stabilized_frame = stab.stabilize(frame)
        
        # wait for stabilizer which still be initializing
        if stabilized_frame is None:
            print("HLEngine: no stabilization needed")
            continue 


        # {do something with the frame here}


        # write stabilized frame to writer
        writer.write(stabilized_frame)
        
        # Show output window
        cv2.imshow("Stabilized Frame", stabilized_frame)

        # check for 'q' key if pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    # close output window
    cv2.destroyAllWindows()

    #clear stabilizer resources
    stab.clean()

    # safely close video stream
    stream.release()

    # safely close writer
    writer.close()


    




def videoObjectDetection(cascade,video_source,frameName,objectName):
    try:
        cap = cv2.VideoCapture(video_source)

        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier(cascade)
        framer=frameName
        font = cv2.FONT_HERSHEY_PLAIN
        while (True):

            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            net = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
                # flags = cv2.CV_HAAR_SCALE_IMAGEHL_Engine/HLEngine_camSnap.py:40
            )

            #print(format(len(net)))
            # print (len(faces))
            if (len(net) >= 1):
                #return ("found 2 eyes")
                cv2.putText(frame, str(objectName), (50, 50), font, 2,
                            (0, 0, 255), 3)



            # Draw a rectangle around the faces
            for (x, y, w, h) in net:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow(framer, frame)
            if cv2.waitKey(1) & 0xFF == ord('x'):
                break


        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
    except:
        return ("HLEngine: An issue with video_source or params")



def overlay(dress_png,person_png,finalName_png):
    try:
        img = Image.open(dress_png)

        #print(img.size)

        background = Image.open(person_png)

        #print(background.size)

        # resize the image
        size = (2000,2000)
        background = background.resize(size,Image.ANTIALIAS)

        background.paste(img, (-350, -950), img)
        background.save(finalName_png,"PNG")
        return ('done')

    except:
        return('HLEngine:An issue with the camera or params passed')



'''def faceIdentification(location_of_face):
    video = cv2.VideoCapture(0)

    deep_image = face_recognition.load_image_file(location_of_face)
    deep_face_encoding = face_recognition.face_encodings(deep_image)
    print("System Start working!")

    while True:
        rit, frame = video.read()
        small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
        rgb_small_frame = small_frame[:, :, :: -1]
        face_locations = face_recognition.face_locations(rgb_small_frame, )
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(deep_face_encoding, face_encoding)
            if True in matches:
                return('detected')


            else:
                print("Waiting for master!")

    video.release()
    cv2.destroyAllWindows()'''

