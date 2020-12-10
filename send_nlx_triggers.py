import pygame
import logging
import serial
import numpy as np
import time
import datetime
import pyxid

#get a list of all attached XID devices
devices = pyxid.get_xid_devices()

dev = devices[0] # get the first device to use
dev.reset_base_timer()
dev.reset_rt_timer()

if dev.is_response_device():
    while not dev.has_response():
        dev.poll_for_response()

    response = dev.get_next_response()
    dev.clear_response_queue()

up_b = 0 , 1
right_b = 1 , 0
down_b = 0 , -1
left_b = -1 , 0

ts = time.time()
d = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S-%d.%m.%Y')

logging.basicConfig(filename=('log_{}.txt'.format(d)), level=logging.DEBUG, format='%(asctime)s: %(message)s')
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYAXISMOTION:
                logging.info((event.dict, event.joy, event.axis, event.value))
            elif event.type == pygame.JOYBALLMOTION:
                logging.info((event.dict, event.joy, event.ball, event.rel))
            elif event.type == pygame.JOYBUTTONDOWN:
                logging.info((event.dict, event.joy, event.button, 'pressed'))
                if j.get_button(1):
                    logging.info('X button was pressed')
                    dev.set_pulse_duration(2)
                    for bm in range(0, 1):
                        mask = 2 ** bm
                        dev.activate_line(bitmask=mask)
                elif j.get_button(0):
                    logging.info('Square button was pressed')
                    dev.set_pulse_duration(5)
                    for bm in range(0, 1):
                        mask = 2 ** bm
                        dev.activate_line(bitmask=mask)
                elif j.get_button(2):
                    logging.info('Circle button was pressed')
                    dev.set_pulse_duration(7)
                    for bm in range(0, 1):
                        mask = 2 ** bm
                        dev.activate_line(bitmask=mask)
                elif j.get_button(3):
                    logging.info('Triangle button was pressed')
                    dev.set_pulse_duration(11)
                    for bm in range(0, 1):
                        mask = 2 ** bm
                        dev.activate_line(bitmask=mask)
                elif j.get_button(5):
                    logging.info('R1 button was pressed')
                    dev.set_pulse_duration(13)
                    for bm in range(0, 1):
                        mask = 2 ** bm
                        dev.activate_line(bitmask=mask)
                elif j.get_button(7):
                    logging.info('R2 button was pressed')
                    dev.set_pulse_duration(17)
                    for bm in range(0, 1):
                        mask = 2 ** bm
                        dev.activate_line(bitmask=mask)
                elif j.get_button(4):
                    logging.info('L1 button was pressed')
                    dev.set_pulse_duration(19)
                    for bm in range(0, 1):
                        mask = 2 ** bm
                        dev.activate_line(bitmask=mask)
                elif j.get_button(6):
                    dev.set_pulse_duration(23)
                    for bm in range(0, 1):
                        mask = 2 ** bm
                        dev.activate_line(bitmask=mask)
            elif event.type == pygame.JOYBUTTONUP:
                logging.info((event.dict, event.joy, event.button, 'released'))
            elif event.type == pygame.JOYHATMOTION:
                logging.info((event.dict, event.joy, event.hat, event.value))
                if event.value == up_b:
                    logging.info('Up button was pressed')
                    dev.set_pulse_duration(29)
                    for bm in range(0, 1):
                        mask = 2 ** bm
                        dev.activate_line(bitmask=mask)
                if event.value == right_b:
                    logging.info('Right button was pressed')
                    dev.set_pulse_duration(31)
                    for bm in range(0, 1):
                        mask = 2 ** bm
                        dev.activate_line(bitmask=mask)
                if event.value == down_b:
                    logging.info('Down button was pressed')
                    dev.set_pulse_duration(37)
                    for bm in range(0, 1):
                        mask = 2 ** bm
                        dev.activate_line(bitmask=mask)
                if event.value == left_b:
                    logging.info('Left button was pressed')
                    dev.set_pulse_duration(41)
                    for bm in range(0, 1):
                        mask = 2 ** bm
                        dev.activate_line(bitmask=mask)
except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
