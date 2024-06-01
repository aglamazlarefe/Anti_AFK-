from random import randint
from time import sleep
from pyautogui import press, keyDown as keydown, keyUp as keyup,moveTo,click

hazır= 5
while hazır >= 1:
    print(hazır)
    sleep(1)
    hazır -=1 


    
x1= randint(0,4)
x2=randint(0,4)
x3=randint(0,4)
x4=randint(0,4)
def sola():
    keydown("a")
    sleep(randint(0,3))    
    keyup("a")
def ileri():
    keydown("w")
    sleep(randint(0,3))
    keyup("w")
def geri():
    keydown("s")
    sleep(randint(0,3))
    keyup("s")
def sağa(): 
    keydown("d")
    sleep(randint(0,3))
    keyup("d")        
def olasılık_x4():
    if x4 == 1:
        sola()
    elif x4 == 2:
        sağa()
    elif x4 == 3:
        geri()
    elif x4 == 4:
        ileri()        
def olasılık_x3():
    if x3== 1:     
        geri()
        olasılık_x4()
    elif  x3== 2:
        ileri()    
        olasılık_x4()
    elif x3== 3:
        sola()
        olasılık_x4
    elif x3 ==4:
        sağa()
        olasılık_x4
def olasılık_x2():
    if x2== 1:
        sağa()
        
    elif x2==2: 
        sola()
        olasılık_x3
    elif x2 == 3:
        ileri()
        olasılık_x3
    elif x2 == 4:
        geri()
        olasılık_x3       
def olasılık_x1():

    if x1== 1:
        ileri()
        olasılık_x2
    elif x1==2:
        geri()
        olasılık_x2

    elif x1== 3:
        sağa()
        olasılık_x2
    elif x1== 4:
        sola()
        olasılık_x2


while True:
    
    olasılık_x1()
    
    x1= randint(0,4)
    x2=randint(0,4)
    x3=randint(0,4)
    x4=randint(0,4)
    