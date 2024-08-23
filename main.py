from ultralytics import YOLO



model = YOLO('best2.pt')

results=model.predict(source=0,conf=0.6, show=True)

print(results)

