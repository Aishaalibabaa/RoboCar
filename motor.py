from gpiozero import Motor

left_motor = Motor(13, 19)
right_motor = Motor(21, 20)

def move_forward():
	left_motor.forward()
	right_motor.forward()

def move_backward():
	left_motor.backward()
	right_motor.backward()

def move_left():
	right_motor.forward()

def move_right():
	left_motor.forward()

