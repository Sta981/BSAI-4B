import cv2

class ObjectDetection:
    def __init__(self):
        weights_path = "dnn_model/frozen_inference_graph.pb"
        config_path = "dnn_model/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
        self.model = cv2.dnn_DetectionModel(weights_path, config_path)
        self.model.setInputParams(size=(320, 320), scale=1.0/127.5, mean=(127.5, 127.5, 127.5), swapRB=True)

    def detect(self, frame):
        class_ids, scores, boxes = self.model.detect(frame, confThreshold=0.5, nmsThreshold=0.4)
        return class_ids, scores, boxes