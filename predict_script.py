from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("yolov8best.pt")
# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam
# results = model.predict(source="0")
# results = model.predict(source="folder", show=True) # Display preds. Accepts all YOLO predict arguments

# from PIL
im1 = Image.open("2.jpg")
results = model.predict(source=im1, save=True,save_crop=True,project="meniscus_predictions")  # save plotted images

# from ndarray
# im2 = cv2.imread("2.jpg")
# results = model.predict(source=im2, save=True, save_txt=True)  # save predictions as labels
