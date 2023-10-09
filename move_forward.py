# script move forward
# and move backward
import RPi.GPIO
import time

# Установка режима нумерации пинов на Raspberry Pi
GPIO.setmode(GPIO.BCM)

motor1_pin1 = 17 # Пин для управления направлением движения первого двигателя
motor1_pin2 = 18 # Пин для управления скоростью первого двигателя
motor2_pin1 = 22 # Пин для управления направлением движения второго двигателя
motor2_pin2 = 23 # Пин для управления скоростью второго двигателя

# Настройка пинов как выходы
GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)
GPIO.setup(motor2_pin1, GPIO.OUT)
GPIO.setup(motor2_pin2, GPIO.OUT)

#  движения вперед
def forward(speed):
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, speed)
    GPIO.output(motor2_pin2, speed)

# движение назад
def backward(speed):
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, speed)
    GPIO.output(motor2_pin2, speed)

# остановка двигателей
def stop():
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, 0)
    GPIO.output(motor2_pin2, 0)

# Движение вперед со скоростью 50%
forward(50)

time.sleep(2)
# Остановка двигателей
stop()

# Движение назад со скоростью 50%
backward(50)

time.sleep(1)
# Остановка двигателей
stop()

GPIO.cleanup()
