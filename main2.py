import cv2
from ultralytics import YOLO
import serial.tools.list_ports


ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portsList = []

for one in ports:
    portsList.append(str(one))
    print(str(one))

com = 4

for i in range(len(portsList)):
    if portsList[i].startswith("COM" + str(com)):
        use = "COM" + str(com)
        print(use)

serialInst.baudrate = 9600
serialInst.port = use
serialInst.open()




model = YOLO('best2.pt')


cap = cv2.VideoCapture(0)


while cap.isOpened():
    
    success, frame = cap.read()
    
    if success:     
        results = model.predict(frame)
       
        if len(results[0].boxes)!=0:
            print('fireeeeeeeeeeeeeeeeeee')
            command = "ON\n" 
            print(command.encode('utf-8'))
            serialInst.write(command.encode('utf-8'))

          
        
        annotated_frame = results[0].plot()       
        cv2.imshow("YOLOv8 Inference", annotated_frame)

       
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break



cap.release()
cv2.destroyAllWindows()