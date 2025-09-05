# Face Recognition Security System

#### Video Demo:  <https://youtu.be/svjGIUoibZQ>

#### Description: 
This Python project is a simple yet effective face recognition security system that uses the DeepFace, OpenCV, and pyttsx3 libraries to detect, recognize, and respond to faces captured through a webcam. The system is designed to be lightweight, easy to use, and entirely terminal-based, making it suitable for learning Python programming, understanding face recognition technologies, and building practical security applications for doors, computers, or other restricted areas.

The program works by continuously capturing frames from a connected webcam using OpenCV. Each frame is analyzed to determine whether a human face is present. If a face is detected, the program uses DeepFace to compare it against a pre-existing database of authorized individuals. This database can contain images of family members, employees, or any person whose access is allowed. By leveraging DeepFace’s advanced facial recognition algorithms, the program ensures accurate identification even in varying lighting conditions or angles.

When the detected face matches an authorized individual, the program waits for a short delay—typically around five seconds—and then uses pyttsx3, a text-to-speech Python library, to greet the person with a personalized voice message. For example, if the recognized person is Mohammad Hosein, the system will say, “Welcome Mohammad Hosein.” This feature not only enhances security but also provides a friendly and interactive user experience, making the system feel more engaging and human-like.

On the other hand, if the face does not match anyone in the database or if no face is detected at all, the program treats the situation as a potential security alert. It saves the current frame in an unauthorized_faces folder, naming each file with the current date and time. This allows the administrator to later review all attempts of unauthorized access and take necessary actions if required. Simultaneously, the system announces an alert via text-to-speech, saying “Unauthorized access,” providing immediate feedback and discouraging potential intruders.

Because the program runs entirely in the terminal, it avoids heavy graphical interfaces, which keeps it simple, fast, and compatible with low-resource systems. The printed messages, combined with voice alerts, create an intuitive interaction flow where the user can immediately understand the system’s status. The modular design of the program also makes it easy to expand. For example, developers can integrate it with door locks, computer login systems, or network security applications.

In addition to being a practical security solution, this project serves as an educational tool. It introduces learners to core concepts of computer vision, facial recognition, and Python programming in a real-world context. By examining and modifying the code, users can explore how OpenCV captures images, how DeepFace performs recognition, and how pyttsx3 converts text into speech, providing a comprehensive learning experience.

Overall, this Python-based face recognition security system is a compact yet powerful project that demonstrates how machine learning and AI can be applied to practical everyday problems while remaining accessible for beginners and intermediate programmers alike.
