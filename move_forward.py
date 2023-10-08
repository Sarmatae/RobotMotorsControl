# script move forward
import RPi.GPIO
import time

GPIO.setmode(GPIO.BCM)

motor_pin1 = 17 # Пин для управления направлением движения двигателя
motor_pin2 = 18 # Пин для управления скоростью двигателя

GPIO.setup(motor_pin1, GPIO.OUT)
GPIO.setup(motor_pin2, GPIO.OUT)

def forward(speed):
    GPIO.output(motor_pin1, GPIO.HIGH)
    GPIO.output(motor_pin2, speed)

def stop():
    GPIO.output(motor_pin1, GPIO.HIGH)
    GPIO.output(motor_pin2, 0)

# Движение вперед со скоростью 50%
forward(50)
# Ждем 2 секунды
time.sleep(2)
# Остановка двигателя
stop()

# Очистка пинов GPIO
GPIO.cleanup()

