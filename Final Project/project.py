from deepface import DeepFace
import cv2
import pyttsx3
import time
from datetime import datetime
import os

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1)

# Known faces database
database = {
    "Aref Tavasoli": "known_faces/Aref.jpg",
    "David J Malen": "known_faces/David.jpg",
}

# Folder to save unauthorized faces
unauthorized_folder = "unauthorized_faces"
os.makedirs(unauthorized_folder, exist_ok=True)

def save_unauthorized_face(frame):
    """Save unauthorized face to folder."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{unauthorized_folder}/unauthorized_{timestamp}.jpg"
    cv2.imwrite(filename, frame)
    print(f"Unauthorized face saved as {filename}")
    engine.say("Unauthorized access")
    engine.runAndWait()
    return filename

def recognize_face(frame, database):
    """Try to recognize a face from the frame."""
    for name, img_path in database.items():
        try:
            cv2.imwrite("current_frame.jpg", frame)
            result = DeepFace.verify(img_path, "current_frame.jpg", model_name="Facenet", enforce_detection=True)
            if result["verified"]:
                return True, name
        except Exception:
            pass
    return False, ""

def greet_user(name):
    """Greet recognized user with TTS."""
    print(f"Face recognized: {name}")
    time.sleep(2)
    print(f"Welcome {name} 🌹")
    engine.say(f"Welcome {name}")
    engine.runAndWait()

def main():
    cap = cv2.VideoCapture(0)
    recognized = False
    recognized_name = ""

    print("Looking for a face... 👀")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        recognized, recognized_name = recognize_face(frame, database)

        if recognized:
            greet_user(recognized_name)
            break
        else:
            # If face is detected but not recognized, save it
            filename = save_unauthorized_face(frame)
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
