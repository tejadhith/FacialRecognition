import face_recognition
import os

def compare(known_image_path, unknown_image_path) :
    known_image = face_recognition.load_image_file(known_image_path)
    unknown_image = face_recognition.load_image_file(unknown_image_path)

    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    return face_recognition.compare_faces([known_encoding], unknown_encoding)[0]