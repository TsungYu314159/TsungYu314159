import cv2
import os
import numpy as np
from PIL import Image
import pytesseract
from image_cut import image_cut
dir_path = 'C:/Users/asus/Desktop/message_image/'
black_store_path = 'C:/Users/asus/Desktop/black_message/'
white_store_path = 'C:/Users/asus/Desktop/white_message/'
black_threshold = 35
white_threshold = 242
black_iteration = 15
white_iteration = 8

image_cut(dir_path, black_store_path, black_threshold, black_iteration, "black")

