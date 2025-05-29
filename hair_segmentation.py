import cv2
import mediapipe as mp
import numpy as np

mp_hair_segmentation = mp.solutions.selfie_segmentation
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
with mp_hair_segmentation.SelfieSegmentation(model_selection=1) as hair_segmentation:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hair_segmentation.process(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        mask = results.segmentation_mask
        condition = np.stack((mask,) * 3, axis=-1) > 0.5
        output = np.where(condition, frame, np.zeros_like(frame))
        cv2.imshow('Hair Segmentation', output)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()