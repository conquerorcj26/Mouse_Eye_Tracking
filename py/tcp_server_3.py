import cv2
import pyautogui
import mediapipe as mp
import socket
import time

# Host and port to listen on
host = '0.0.0.0'  # Listen on all available interfaces
port = 12345      # Choose a port number above 1024

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the address and port
server_socket.bind((host, port))
# Listen for incoming connections
server_socket.listen(1)
print("Server is listening on", host, "port", port)

# Accept incoming connection
client_socket, client_address = server_socket.accept()

print("Connection established with", client_address)


cam = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

while True:
    _, frame = cam.read()
    frame_h, frame_w, _ = frame.shape
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    if landmark_points:
        landmarks = landmark_points[0].landmark
        left = [landmarks[145], landmarks[159]]
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                processed_data = str(screen_x)+" "+str(screen_y)+" "+str(left[0].y)+" "+str(left[1].y)
                print(processed_data)
                # Send data to client
                client_socket.sendall(processed_data.encode())
                time.sleep(0.1)
    cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()

# Close the connection
client_socket.close()
server_socket.close()