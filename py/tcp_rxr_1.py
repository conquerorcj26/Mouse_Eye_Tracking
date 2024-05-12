import cv2
import socket
import pyautogui

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.40', 12345))  # Connect to Raspberry Pi's IP address on port 5000

# Receive data from server
while True:
    data = client_socket.recv(1024)  # Receive data (adjust buffer size as needed)
    input_data = data.decode()
    x=input_data.split()
    print(x)
    screen_x, screen_y = float(x[0]),float(x[1])
    #pyautogui.sleep(1)
    pyautogui.moveTo(screen_x, screen_y)
    

# Close socket
client_socket.close()