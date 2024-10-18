import time
from robot_hat import Ultrasonic, Pin

sonar = Ultrasonic(Pin("D2"), Pin("D3"))

while True:
    distance = sonar.read()
    print(f"Distance: {distance}")
    time.sleep(1)
