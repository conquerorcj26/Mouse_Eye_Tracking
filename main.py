import socket
import pyautogui

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client_socket.connect(('192.168.1.52', 12345))  # Connect to Raspberry Pi's IP address on port 12345 using arp-a and stufffrom notepad
client_socket.connect(('192.168.201.254', 12345))
# Receive data from server
while True:
    try:
        data = client_socket.recv(1024)  # Receive data (adjust buffer size as needed)
        input_data = data.decode()
        x=input_data.split()
    
        #print(x)
        screen_x, screen_y,left_1,left_2 = float(x[0]),float(x[1]),float(x[2]),float(x[3])
        pyautogui.moveTo(screen_x, screen_y)
        if (left_1-left_2) < 0.03:
            pyautogui.click()
            #pyautogui.sleep(1)  
    except:
        continue
# Close socket
client_socket.close()