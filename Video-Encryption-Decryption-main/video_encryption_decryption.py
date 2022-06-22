# Video Encryption Decryption

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import numpy as np
import random
import os
from cv2 import *
from moviepy.editor import *
from skimage.io import *

# Main Window & Configuration
window = tk.Tk() # created a tkinter gui window frame
window.title("Video Encryption Decryption") # title given is "DICTIONARY"
window.geometry('1000x700')

# top label
start1 = tk.Label(text = "VIDEO  ENCRYPTION\nDECRYPTION", font=("Arial", 55,"underline"), fg="magenta") # same way bg
start1.place(x = 120, y = 10)

def start_fun():
    window.destroy()

# start button created
startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =150 , y =580 )

# image on the main window
path = "D:/6th sem/cns project and docs/Video-Encryption-Decryption-main/Video-Encryption-Decryption-main/Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 130, y = 230)

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y = 580 )
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

# Main Window & Configuration
window1 = tk.Tk() # created a tkinter gui window frame
window1.title("Video Encryption Decryption") # title given is "DICTIONARY"
window1.geometry('1000x700')

# function to select file
def open_file():
    global filename
    filename = filedialog.askopenfilename(title="Select file")
    # print(filename)
    path_text.delete("1.0", "end")
    path_text.insert(END, filename)

# function to encrypt video and show encrypted video
def encrypt_fun():
    global filename
    path_list = []
    path="D:/6th sem/cns project and docs/Video-Encryption-Decryption-main/Video-Encryption-Decryption-main"
    # converting videos to images --------------------------------
    # Read the video from specified path
    cam = cv2.VideoCapture(filename)
    # print(cam.get(cv2.CAP_PROP_FPS))
    # info1.config(text="Frame Rate  :  " + str(cam.get(cv2.CAP_PROP_FPS)))
    x = int(cam.get(cv2.CAP_PROP_FPS))
    try:
        # creating a folder named data
        if not os.path.exists('D:/6th sem/cns project and docs/Video-Encryption-Decryption-main/Video-Encryption-Decryption-main/Video_Images'):
            os.makedirs('D:/6th sem/cns project and docs/Video-Encryption-Decryption-main/Video-Encryption-Decryption-main/Video_Images')
    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')
    # frame
    currentframe = 0
    x2 = 0
    while (True):
        # reading from frame
        ret, frame = cam.read()
        # print(currentframe)
        if ret:
            if currentframe % x == 0:
                # if video is still left continue creating images
                x1 = int(currentframe / x)
                name = path +'/Video_Images/frame' + str(x1) + '.jpg'
                # print(x1, end = " ")
                x2 = x2 + 1
                #         print ('Creating...' + name)
                # writing the extracted images
                cv2.imwrite(name, frame)

                # ------------- convert to encrypted image -----------------
                # name_of = './Video Images/frame' + str(x1) + '.jpg'
                image_input = imread(name, cv2.IMREAD_GRAYSCALE)
                (x3, y, z) = image_input.shape
                # for i in image_input.shape:
                #     print(i)
                image_input = image_input.astype(float) / 255.0
                # print(image_input)

                mu, sigma = 0, 0.1  # mean and standard deviation
                key = np.random.normal(mu, sigma, (x3, y,z)) + np.finfo(float).eps
                # print(key)
                image_encrypted = image_input / key
                name1 = path+ '/Video_Images/frame' + str(x1) + '.jpg'
                # path_list.append(name1)
                # print(x1)
                cv2.imwrite(name1, image_encrypted * 255)
                # ----------------------------------------------------------

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break
    #     ret,frame = cam.read()
    # info2.config(text="No. of frame/Images  :  " + str(x2))
    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()

    # print(len(path_list))
    # for i in path_list:
    #     print(i)
    ic_list = []
    z1=0
    for i in range(x2):
        ic_list.append(ImageClip(path+"/Video_Images/frame"+str(z1)+".jpg").set_duration(1))
        z1+=1
    video = concatenate(ic_list, method="compose")
    video.write_videofile('slide_show.mp4', fps=30)

    # playing encrypted video ------------
    source1 = cv2.VideoCapture('slide_show.mp4')
    # running the loop
    while True:
        # extracting the frames
        ret1, img1 = source1.read()
        # displaying the video
        cv2.imshow("Encrypted Video", img1)
        # exiting the loop
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

# function to decrypt video and show decrypted video
def decrypt_fun():
    global filename
    source = cv2.VideoCapture(filename)
    ##
    source1 = cv2.VideoCapture("D:/6th sem/cns project and docs/video.mp4")
    currentframe = 0
    x2=0
    while (True):
        # reading from frame
        ret, frame = source1.read()
        # print(currentframe)
        if ret:
            if currentframe % 60 == 0:
                # if video is still left continue creating images
                x1 = int(currentframe / 60)
                name ="D:/6th sem/cns project and docs/Video-Encryption-Decryption-main/Video-Encryption-Decryption-main/Images/sample.jpg"
                # name = path +'/Video_Images/frame' + str(x1) + '.jpg'
                # print(x1, end = " ")
                x2 = x2 + 1
                #         print ('Creating...' + name)
                # writing the extracted images
                cv2.imwrite(name, frame)

                # ------------- convert to encrypted image -----------------
                # name_of = './Video Images/frame' + str(x1) + '.jpg'
                image_input = imread(name, cv2.IMREAD_GRAYSCALE)
                (x3, y, z) = image_input.shape
                # for i in image_input.shape:
                #     print(i)
                image_input = image_input.astype(float) / 255.0
                # print(image_input)

                mu, sigma = 0, 0.1  # mean and standard deviation
                key = np.random.normal(mu, sigma, (x3, y,z)) + np.finfo(float).eps
                # print(key)
                image_encrypted = image_input / key
                # name1 = path+ '/Video_Images/frame' + str(x1) + '.jpg'
                # path_list.append(name1)
                # print(x1)
                # cv2.imwrite(name1, image_encrypted / 255)
                # ----------------------------------------------------------

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break
    ##
    # running the loop
    # print(source)
    while True:
        # extracting the frames
        ret, img = source.read()
        # converting to gray-scale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # displaying the video
        cv2.imshow("Decrypted Video", gray)
        # exiting the loop
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

# function to reset the video to original video and show preview of that
def reset_fun():
    global filename

    source3 = cv2.VideoCapture(filename)
    # running the loop
    while True:
        # extracting the frames
        ret3, img3 = source3.read()
        # displaying the video
        cv2.imshow("Original Video", img3)
        # exiting the loop
        key = cv2.waitKey(1)
        if key == ord("q"):
            break



# top label
start1 = tk.Label(text = "VIDEO  ENCRYPTION\nDECRYPTION", font=("Arial", 55, "underline"), fg="magenta") # same way bg
start1.place(x = 120, y = 10)

# lbl1 = tk.Label(text="Select any video, dimension & crop it...", font=("Arial", 40),fg="green")  # same way bg
# lbl1.place(x=50, y=100)

lbl2 = tk.Label(text="Selected Video", font=("Arial", 30),fg="brown")  # same way bg
lbl2.place(x=80, y=220)

path_text = tk.Text(window1, height=3, width=37, font=("Arial", 30), bg="light yellow", fg="orange",borderwidth=2, relief="solid")
path_text.place(x=80, y = 270)

# Select Button
selectb=Button(window1, text="ENCRYPT VIDEO",command=encrypt_fun,  font=("Arial", 25), bg = "orange", fg = "blue")
selectb.place(x = 120, y = 450)

# Select Button
selectb=Button(window1, text="DECRYPT VIDEO",command=decrypt_fun,  font=("Arial", 25), bg = "orange", fg = "blue")
selectb.place(x = 550, y = 450)

# Select Button
selectb=Button(window1, text="SELECT",command=open_file,  font=("Arial", 25), bg = "light green", fg = "blue")
selectb.place(x = 120, y = 580)

# Get Images Button
getb=Button(window1, text="RESET",command=reset_fun,  font=("Arial", 25), bg = "yellow", fg = "blue")
getb.place(x = 420, y = 580)


def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

# Get Images Button
getb=Button(window1, text="EXIT",command=exit_win1,  font=("Arial", 25), bg = "red", fg = "blue")
getb.place(x = 750, y = 580)

window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()
