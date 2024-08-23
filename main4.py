import cv2
import threading
import pytesseract
from ultralytics import YOLO  # Assuming YOLO model is defined in yolomodel.py
pytesseract.pytesseract.tesseract_cmd='C:\Program Files\Tesseract-OCR\\tesseract.exe'
# Function to run YOLO model
import serial.tools.list_ports




ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portsList = []

for one in ports:
    portsList.append(str(one))
    print(str(one))

com = 5

for i in range(len(portsList)):
    if portsList[i].startswith("COM" + str(com)):
        use = "COM" + str(com)
        print(use)

serialInst.baudrate = 9600
serialInst.port = use
serialInst.open()

def run_yolo_model(model, frame):
    results = model.predict(frame)
    if len(results[0].boxes) != 0:
             print('fireeeeeeeeeeeeeeeeeee')
             command = "ON\n" 
             print(command.encode('utf-8'))
             serialInst.write(command.encode('utf-8'))

# Function to run pytesseract
def run_pytesseract(frame):
    text = pytesseract.image_to_string(frame).lower().rstrip()
    if text == "field a":
        command = "a\n" 
        print(command.encode('utf-8'))
        serialInst.write(command.encode('utf-8'))

        # Perform action for command A
    elif text == "field b":
        command = "b\n" 
        print(command.encode('utf-8'))
        serialInst.write(command.encode('utf-8'))


model = YOLO('best2.pt')

cap = cv2.VideoCapture(0)


def process_frames():
    while cap.isOpened():
        success, frame = cap.read()
        cv2.imshow('frame', frame)
        if success:
            # Create threads for YOLO model and pytesseract
            yolo_thread = threading.Thread(target=run_yolo_model, args=(model, frame))
            pytesseract_thread = threading.Thread(target=run_pytesseract, args=(frame,))
            
            # Start the threads
            yolo_thread.start()
            pytesseract_thread.start()

            # Join the threads to wait for them to finish
            yolo_thread.join()
            pytesseract_thread.join()

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

# Start processing frames
process_frames()
