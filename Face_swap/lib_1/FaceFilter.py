# import dlib
# import numpy as np
import face_recognition
# import face_recognition_models

class FaceFilter():
    def __init__(self, reference_file_path, threshold = 0.6):
        image = face_recognition.load_image_file(reference_file_path)
        self.encoding = face_recognition.face_encodings(image)[0] # Note: we take only first face, so the reference file should only contain one face. We could also keep all faces found and filter against multiple faces
        self.threshold = threshold
    
    def check(self, detected_face):
        print("check")
        encodings = face_recognition.face_encodings(detected_face.image)[0] # we could use detected landmarks, but I did not manage to do so
        score = face_recognition.face_distance([self.encoding], encodings)
        print(score)
        return score <= self.threshold


# # Copy/Paste (mostly) from private method in face_recognition
# face_recognition_model = face_recognition_models.face_recognition_model_location()
# face_encoder = dlib.face_recognition_model_v1(face_recognition_model)

# def convert(detected_face):
#     return np.array(face_encoder.compute_face_descriptor(detected_face.image, detected_face.landmarks, 1))
# # end of Copy/Paste
