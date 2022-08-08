import cv2
import os
import numpy as np
from PIL import Image
import pytesseract
#dir_path = r'C:\Users\asus\Desktop\message_image'

def image_cut(path, store_path, threshold, iteration, bw):  ### (threshlod, iteration): black image=(35, 15), white image = (242, 8)
    file_list = os.listdir(path)
    for i in file_list:
        origin_pic = cv2.imread(path+i)

        x = origin_pic.shape[0]
        y = origin_pic.shape[1]
        rate_x=x/512.0
        rate_y=y/512.0

        origin_pic = cv2.resize(origin_pic, (512,512), interpolation=cv2.INTER_AREA)
        origin_pic = origin_pic[75:440,0:512]

        gray_pic = cv2.cvtColor(origin_pic, cv2.COLOR_BGR2GRAY)
        if bw =="white":
            ret, thresh = cv2.threshold(gray_pic, threshold, 255, cv2.THRESH_BINARY_INV)
        elif bw =="black":
            ret, thresh = cv2.threshold(gray_pic, threshold, 255, cv2.THRESH_BINARY)
        else:
            print("It is not black or white image, stop the program!")
            exit()

        kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(4,4))
        closed=cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        closed=cv2.erode(closed, None, iterations=iteration)
        closed=cv2.dilate(closed, None, iterations=iteration)

        (cnts, hierarchy)=cv2.findContours(closed.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        clone=origin_pic.copy()
        cv2.drawContours(clone,cnts,-1,(0,255,0),2)
        for j in range(0,len(cnts)):
            x, y, w, h = cv2.boundingRect(cnts[j])
            cv2.rectangle(origin_pic, (x,y), (x+w, y+h), (153,153,0), 2)
            newimage=origin_pic[y+2:y+h-2, x+2:x+w-2]
            new_x=newimage.shape[0]
            new_y=newimage.shape[1]
            newimage=cv2.resize(newimage, (round(new_y*rate_y), round(new_x*rate_x)), interpolation=cv2.INTER_AREA)

            cv2.imwrite(store_path+i[:-4]+str(j)+".jpg", newimage)


#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#img = Image.open(r'C:\Users\asus\Downloads\cut_img\0.jpg')
#text = pytesseract.image_to_string(img, lang="chi_tra+eng")
#print(text)
