#!/usr/bin/env python3

import gpiozero
import controller
import sensor
import time
speed_RB = 0.4
speed_LF = 0.4

right_speed = 0.5
left_speed = 0.5

def follow_wall():
    while True:
        wall_drive()

def wall_right():
    max_distance = 60
    min_distance = 35
    side_distance = sensor.get_distance_side()
    while True:
        if side_distance >= min_distance:
            controller.smooth_right(right_speed, left_speed)
            side_distance = sensor.get_distance_side()
        elif side_distance <= min_distance:
            controller.smooth_left(right_speed, left_speed)
            side_distance = sensor.get_distance_side()
wall_right()