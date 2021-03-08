import pygame
import logging
import serial
import numpy as np
import time
import datetime
import simpleaudio as sa

fs = 44100  # 44100 samples per second
seconds = 1  # Generate a note duration of 1 second to be embedded in the video

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * fs, False)

# Generate a X Hz sine wave
note1 = np.sin(262 * t * 2 * np.pi)
note2 = np.sin(294 * t * 2 * np.pi)
note3 = np.sin(330 * t * 2 * np.pi)
note4 = np.sin(370 * t * 2 * np.pi)
note5 = np.sin(415 * t * 2 * np.pi)
note6 = np.sin(466 * t * 2 * np.pi)
note7 = np.sin(523 * t * 2 * np.pi)
note8 = np.sin(587 * t * 2 * np.pi)
note9 = np.sin(659 * t * 2 * np.pi)
note10 = np.sin(740 * t * 2 * np.pi)
note11 = np.sin(831 * t * 2 * np.pi)
note12 = np.sin(932 * t * 2 * np.pi)

audio1 = note1 * (2**15 - 1) / np.max(np.abs(note1))
audio2 = note2 * (2**15 - 1) / np.max(np.abs(note2))
audio3 = note3 * (2**15 - 1) / np.max(np.abs(note3))
audio4 = note4 * (2**15 - 1) / np.max(np.abs(note4))
audio5 = note5 * (2**15 - 1) / np.max(np.abs(note5))
audio6 = note6 * (2**15 - 1) / np.max(np.abs(note6))
audio7 = note7 * (2**15 - 1) / np.max(np.abs(note7))
audio8 = note8 * (2**15 - 1) / np.max(np.abs(note8))
audio9 = note9 * (2**15 - 1) / np.max(np.abs(note9))
audio10 = note10 * (2**15 - 1) / np.max(np.abs(note10))
audio11 = note11 * (2**15 - 1) / np.max(np.abs(note11))
audio12 = note12 * (2**15 - 1) / np.max(np.abs(note12))

audio1 = audio1.astype(np.int16)
audio2 = audio2.astype(np.int16)
audio3 = audio3.astype(np.int16)
audio4 = audio4.astype(np.int16)
audio5 = audio5.astype(np.int16)
audio6 = audio6.astype(np.int16)
audio7 = audio7.astype(np.int16)
audio8 = audio8.astype(np.int16)
audio9 = audio9.astype(np.int16)
audio10 = audio10.astype(np.int16)
audio11 = audio11.astype(np.int16)
audio12 = audio12.astype(np.int16)

#define arrow keys
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
            if event.type == pygame.JOYBUTTONDOWN:
                logging.info((event.dict, event.joy, event.button, 'pressed'))
                if j.get_button(1):
                    logging.info('X button was pressed')
                    play_obj = sa.play_buffer(audio1, 1, 2, fs)
                elif j.get_button(0):
                    logging.info('Square button was pressed')
                    play_obj = sa.play_buffer(audio2, 1, 2, fs)
                elif j.get_button(2):
                    logging.info('Circle button was pressed')
                    play_obj = sa.play_buffer(audio3, 1, 2, fs)
                elif j.get_button(3):
                    logging.info('Triangle button was pressed')
                    play_obj = sa.play_buffer(audio4, 1, 2, fs)
                elif j.get_button(5):
                    logging.info('R1 button was pressed')
                    play_obj = sa.play_buffer(audio5, 1, 2, fs)
                elif j.get_button(7):
                    logging.info('R2 button was pressed')
                    play_obj = sa.play_buffer(audio6, 1, 2, fs)
                elif j.get_button(4):
                    logging.info('L1 button was pressed')
                    play_obj = sa.play_buffer(audio7, 1, 2, fs)
                elif j.get_button(6):
                    logging.info('L2 button was pressed')
                    play_obj = sa.play_buffer(audio8, 1, 2, fs)
            elif event.type == pygame.JOYBUTTONUP:
                logging.info((event.dict, event.joy, event.button, 'released'))
                if j.get_button(1):
                    logging.info('X button was released')
                elif j.get_button(0):
                    logging.info('Square button was released')
                elif j.get_button(2):
                    logging.info('Circle button was released')
                elif j.get_button(3):
                    logging.info('Triangle button was released')
                elif j.get_button(5):
                    logging.info('R1 button was released')
                elif j.get_button(7):
                    logging.info('R2 button was released')
                elif j.get_button(4):
                    logging.info('L1 button was released')
                elif j.get_button(6):
                    logging.info('L2 button was released')
            elif event.type == pygame.JOYHATMOTION:
                logging.info((event.dict, event.joy, event.hat, event.value))
                if event.value == up_b:
                    logging.info('Up button was pressed')
                    play_obj = sa.play_buffer(audio9, 1, 2, fs)
                if event.value == right_b:
                    logging.info('Right button was pressed')
                    play_obj = sa.play_buffer(audio10, 1, 2, fs)
                if event.value == down_b:
                    logging.info('Down button was pressed')
                    play_obj = sa.play_buffer(audio11, 1, 2, fs)
                if event.value == left_b:
                    logging.info('Left button was pressed')
                    play_obj = sa.play_buffer(audio12, 1, 2, fs)
            elif event.type == pygame.JOYAXISMOTION:
                logging.info((event.dict, event.joy, event.axis, event.value))
            elif event.type == pygame.JOYBALLMOTION:
                logging.info((event.dict, event.joy, event.ball, event.rel))

except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
