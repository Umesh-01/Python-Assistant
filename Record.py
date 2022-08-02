import cv2
import psutil
import numpy as np
import os
import pyautogui

def screen_record():                                                                  #Screen Recording function              
                                                                                       
    user = psutil.users()[0].name                                                     #gets the user name 
    f_path = "C:\\Users\\" + user + "\\Desktop"       
    # f_path = input("Enter where u want to save the file")                           #can also have an option as to where the user wants to save the file
    if os.path.exists(f_path):
        save_file = os.path.join(f_path,"output.mp4")    
    else:
        save_file ="output.mp4"                                                       #saves the file in the corresponding directory

    s_size = (1920,1080)
    fps = 10.0                                                                        #determines how fast the slow the playback speed will be

    fcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(save_file,fcc,fps,(s_size))

    while 1:

        img = pyautogui.screenshot()
        frm = np.array(img)
        frm = cv2.cvtColor(frm,cv2.COLOR_BGR2RGB)
        cv2.imshow("recorder",frm)
        cv2.namedWindow("recorder",cv2.WINDOW_NORMAL)
        cv2.resizeWindow("recorder", 800,800)
        out.write(frm)
        
        key = cv2.waitKey(1)                                                           # q to close the window and stop recording
        if key == 113:
            break

    cv2.destroyAllWindows()
    out.release()
