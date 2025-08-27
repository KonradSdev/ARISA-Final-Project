from ultralytics import YOLO
import os
import shutil

model = YOLO('yolov5nu.pt')

# Train the model with use of data augmentation
results = model.train("detect",data='/configs/data.yaml', epochs=100, imgsz=640, device=0, freeze = 24)

# Create "my_model" folder to store model weights and train results
os.mkdir('/models/my_model')
shutil.copyfile("'runs/detect/train4/weights/best.pt", '/models/my_model/ARISA.pt')

# Export model to ncnn version so it can be used by Raspberry Pi
model = YOLO("/models/my_model/ARISA.pt")
model.export(format="ncnn")