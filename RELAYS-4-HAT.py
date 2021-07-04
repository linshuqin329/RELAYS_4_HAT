  #!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time



Relay_Ch1 = 26
Relay_Ch2 = 21
Relay_Ch3 = 20
Relay_Ch4 = 19

Relay_Key1 = 12
Relay_Key2 = 6
Relay_Key3 = 16
Relay_Key4 = 13


Key1_state=0
Key2_state=0
Key3_state=0
Key4_state=0



def Key1_Interrupt(Relay_Key1):
    global Key1_state
    Key1_state=not Key1_state   
    #print(Key1_state)
    time.sleep(0.1)
    if (Key1_state == 0):
        GPIO.output(Relay_Ch1,GPIO.LOW)
        print("Channel 1 : OFF")       
    elif(Key1_state == 1):
        GPIO.output(Relay_Ch1,GPIO.HIGH)
        print("Channel 1 : ON")


def Key2_Interrupt(Relay_Key2):
    global Key2_state
    Key2_state=not Key2_state   
    #print(Key2_state)
    time.sleep(0.1)   
    if (Key2_state == 0):
        GPIO.output(Relay_Ch2,GPIO.LOW)
        print("Channel 2 : OFF")       
    elif(Key2_state == 1):
        GPIO.output(Relay_Ch2,GPIO.HIGH)
        print("Channel 2 : ON")  
  

def Key3_Interrupt(Relay_Key3):
    global Key3_state
    Key3_state=not Key3_state   
    #print(Key3_state)
    time.sleep(0.1)
    if (Key3_state == 0):
        GPIO.output(Relay_Ch3,GPIO.LOW)
        print("Channel 3 : OFF")       
    elif(Key3_state == 1):
        GPIO.output(Relay_Ch3,GPIO.HIGH)
        print("Channel 3 : ON")


def Key4_Interrupt(Relay_Key4):
    global Key4_state
    Key4_state=not Key4_state   
    #print(Key4_state)
    time.sleep(0.1)
    if (Key4_state == 0):
        GPIO.output(Relay_Ch4,GPIO.LOW)
        print("Channel 4 : OFF")       
    elif(Key4_state == 1):
        GPIO.output(Relay_Ch4,GPIO.HIGH)
        print("Channel 4 : ON")   

  
  
  
  
  

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Relay_Ch1,GPIO.OUT)
GPIO.setup(Relay_Ch2,GPIO.OUT)
GPIO.setup(Relay_Ch3,GPIO.OUT)
GPIO.setup(Relay_Ch4,GPIO.OUT)

GPIO.setup(Relay_Key1,GPIO.IN)
GPIO.setup(Relay_Key2,GPIO.IN)
GPIO.setup(Relay_Key3,GPIO.IN)
GPIO.setup(Relay_Key4,GPIO.IN)


GPIO.add_event_detect(Relay_Key1,GPIO.FALLING,Key1_Interrupt,200)
GPIO.add_event_detect(Relay_Key2,GPIO.FALLING,Key2_Interrupt,200)
GPIO.add_event_detect(Relay_Key3,GPIO.FALLING,Key3_Interrupt,200)
GPIO.add_event_detect(Relay_Key4,GPIO.FALLING,Key4_Interrupt,200)











GPIO.output(Relay_Ch1,GPIO.HIGH)
time.sleep(0.4)
GPIO.output(Relay_Ch2,GPIO.HIGH)
time.sleep(0.4)
GPIO.output(Relay_Ch3,GPIO.HIGH)
time.sleep(0.4)
GPIO.output(Relay_Ch4,GPIO.HIGH)
time.sleep(0.4)
GPIO.output(Relay_Ch4,GPIO.LOW)
time.sleep(0.4)
GPIO.output(Relay_Ch3,GPIO.LOW)
time.sleep(0.4)
GPIO.output(Relay_Ch2,GPIO.LOW)
time.sleep(0.4)
GPIO.output(Relay_Ch1,GPIO.LOW)
time.sleep(0.4)






while True:
    
    
 
		

    print("Channel1: %d    Channel2: %d    Channel3: %d    Channel4: %d" %(Key1_state,Key2_state,Key3_state,Key4_state))
    time.sleep(1.5)

GPIO.cleanup()  
    
    
    
    
    
    
    
    
    
    