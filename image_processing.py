import numpy as np
import cv2
import math
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  
video = cv2.VideoCapture(0)

ena = 11
in2 = 13
in1 = 15
in3 = 16 
in4 = 18
enb = 22

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
p=GPIO.PWM(ena,100)
p.start(25)

def dur():
    print("Motorlar durdu.")
    GPIO.output(ena,GPIO.LOW)
    GPIO.output(enb,GPIO.LOW)

def ileri():
    for i in range(5): 
                i=i+1
                break
    print("Motorlar ileri gidiyor")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(ena,GPIO.HIGH)
    
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(enb,GPIO.HIGH)
    
 
def sol():
    for i in range(5): 
        i=i+1
        break
    print("Motorlar saga gidiyor")
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(ena,GPIO.HIGH)
    
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(enb,GPIO.HIGH)
    
    
def sag():
    for i in range(5): 
        i=i+1
        break
    print("Motorlar sola gidiyor")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(ena,GPIO.HIGH)
    
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(enb,GPIO.HIGH)
    
    
  
while(1):
     
    _, image = video.read()         
    hsvFrame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    

    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)    
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
    contours, hierarchy = cv2.findContours(green_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 5000):
            x, y, w, h = cv2.boundingRect(contour)
            image= cv2.rectangle(image, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 255), 2)
            a=int(x+(w/2))
            b=int(y+(h/2))
            image = cv2.circle(image,(a,b),5,(255,0,0),-1)
            image = cv2.circle(image,(320,240),5,(0,255,0),-1)
    # Creating contour to track green color
            contours, hierarchy = cv2.findContours(green_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)    
            
            R = w  
            A= (math.pi*R*R)/1000
            
            print(A)
            dx = 410-a 
            dy = 230-b
         
            if (A>180):
                dur()
                print("hooop durr")
            elif (A>=110):              
                if (dx<-80):
                    sag()
                    p.ChangeDutyCycle(25)
                    print("Sağa dön")
           
                elif (dx>80):
                    sol()
                    p.ChangeDutyCycle(25)
                    print("Sola dön")
                    
                elif (-80<dx<80):
                    print("Sabit")
                    ileri()
                    p.ChangeDutyCycle(25)   
                    print("yavaş")
                    
            elif (90<A<110):
                if (dx<-80):
                    sag()
                    p.ChangeDutyCycle(50)
                    print("Sağa dön")
                   
                elif (dx>80):
                    sol()
                    p.ChangeDutyCycle(50)
                    print("Sola dön")
                  
                elif (-80<dx<80):
                    ileri()
                    print("Sabit")
                    
                    p.ChangeDutyCycle(50)   
                    print("sabit hız")
                  
            elif (A<90):
                if (dx<-80):
                    sag()
                    p.ChangeDutyCycle(75)
                    print("Sağa dön")
                   
                elif (dx>80):
                    sol()
                    p.ChangeDutyCycle(75)
                    print("Sola dön")
                    
                elif (-80<dx<80):
                    ileri()
                    print("Sabit")
                    p.ChangeDutyCycle(75)
                    print("hızlan")
                 
            
            print(float(A))       
            cv2.imshow("Multiple Color Detection in Real-TIme", image)
            if cv2.waitKey(2) & 0xFF == ord('q'):
                video.release()
                cv2.destroyAllWindows() 
                break
GPIO.cleanup()

"""  
    black_lower = np.array([0,0,0], np.uint8)  
    black_upper = np.array([50,50,100], np.uint8)   
    black_mask = cv2.inRange(hsvFrame, black_lower,black_upper)   
    contours, hierarchy = cv2.findContours(black_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
"""   
   