import os
import cv2
import numpy as np
from project import save_unauthorized_face, recognize_face, greet_user, database

# -----------------------------
# Test 1: save_unauthorized_face
# -----------------------------
def test_function_1():
    print("Testing save_unauthorized_face...")

    dummy_frame = np.zeros((100, 100, 3), dtype=np.uint8)
    saved_filename = save_unauthorized_face(dummy_frame)

    if os.path.exists(saved_filename):
        print("Test save_unauthorized_face: PASS")
    else:
        print("Test save_unauthorized_face: FAIL")

# -----------------------------
# Test 2: recognize_face
# -----------------------------
def test_function_2():
    print("\nTesting recognize_face...")

    dummy_frame = cv2.imread("known_faces/Aref.jpg")
    recognized, name = recognize_face(dummy_frame, database)

    if recognized and name == "Aref Tavasoli":
        print("Test recognize_face: PASS")
    else:
        print("Test recognize_face: FAIL", recognized, name)

# -----------------------------
# Test 3: greet_user
# -----------------------------
def test_function_3():
    print("\nTesting greet_user...")
    greet_user("Test User")  
    print("Test greet_user: DONE")

# -----------------------------

if __name__ == "__main__":
    test_function_1()
    test_function_2()
    test_function_3()
