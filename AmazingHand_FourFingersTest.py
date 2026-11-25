import time
import numpy as np

from rustypot import Scs0009PyController

#list of all 8 servos from amazing hand set
ID_1 = 1 
ID_2 = 2 
ID_3 = 3 
ID_4 = 4  
ID_5 = 5
ID_6 = 6
ID_7 = 7
ID_8 = 8
MiddlePos_1 = -20 #Middle position for servo ID_1, ID_3, ID_5, ID_7
MiddlePos_2 = 20 #Middle position for servo ID_2, ID_4, ID_6, ID_8

c = Scs0009PyController(
        serial_port="COM3", #insert your correct COM port here
        baudrate=1000000,
        timeout=0.5,
    )

def main():
    
    c.write_torque_enable(ID_1, 1)
    c.write_torque_enable(ID_2, 1)
    c.write_torque_enable(ID_3, 1)
    c.write_torque_enable(ID_4, 1)
    c.write_torque_enable(ID_5, 1)
    c.write_torque_enable(ID_6, 1)
    c.write_torque_enable(ID_7, 1)
    c.write_torque_enable(ID_8, 1) 
    #1 = On / 2 = Off / 3 = Free
    
    while True:
        

        CloseFingerBottom()
        time.sleep(3)


        OpenFingerBottom()
        time.sleep(1)

        CloseFingerMiddle()
        time.sleep(3)
        
        
        OpenFingerMiddle()
        time.sleep(1)

        CloseFingerTop()
        time.sleep(3)
        
        
        OpenFingerTop()
        time.sleep(1)

        CloseFingerThumb()
        time.sleep(1)

        OpenFingerThumb()
        time.sleep(1)
        

#Callibration might not work with your servo set,
#Preform calibration to your servo set specifically
def CloseFingerThumb():
    
    c.write_goal_speed(ID_1, 6) # Set speed for ID_1 to 6 => Max Speed
    c.write_goal_speed(ID_2, 6) # Set speed for ID_1 to 6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1-40)
    Pos_2 = np.deg2rad(MiddlePos_2-30)
    c.write_goal_position(ID_3, Pos_1)
    c.write_goal_position(ID_4, Pos_2)
    time.sleep(0.01)

def OpenFingerThumb():
    c.write_goal_speed(ID_1, 6) # Set speed for ID_1 to 6 => Max Speed
    c.write_goal_speed(ID_2, 6) # Set speed for ID_1 to 6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1-260)
    Pos_2 = np.deg2rad(MiddlePos_2+100)
    c.write_goal_position(ID_3, Pos_1)
    c.write_goal_position(ID_4, Pos_2)
    time.sleep(0.01)

def CloseFingerTop():
    
    c.write_goal_speed(ID_3, 6) # Set speed for ID_1 to 6 => Max Speed
    c.write_goal_speed(ID_4, 6) # Set speed for ID_1 to 6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1-40)
    Pos_2 = np.deg2rad(MiddlePos_2-30)
    c.write_goal_position(ID_3, Pos_1)
    c.write_goal_position(ID_4, Pos_2)
    time.sleep(0.01)

def CloseFingerMiddle():
    
    c.write_goal_speed(ID_5, 6) # Set speed for ID_1 to 6 => Max Speed
    c.write_goal_speed(ID_6, 6) # Set speed for ID_1 to 6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1-70)
    Pos_2 = np.deg2rad(MiddlePos_2-30)
    c.write_goal_position(ID_5, Pos_1)
    c.write_goal_position(ID_6, Pos_2)
    time.sleep(0.01)

def CloseFingerBottom():
    
    c.write_goal_speed(ID_7, 6) # Set speed for ID_1 to 6 => Max Speed
    c.write_goal_speed(ID_8, 6) # Set speed for ID_1 to 6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1+20)
    Pos_2 = np.deg2rad(MiddlePos_2+30)
    c.write_goal_position(ID_7, Pos_1)
    c.write_goal_position(ID_8, Pos_2)
    time.sleep(0.01)


def OpenFingerTop():
    c.write_goal_speed(ID_3, 6) # Set speed for ID_1 to 6 => Max Speed
    c.write_goal_speed(ID_4, 6) # Set speed for ID_1 to 6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1-260)
    Pos_2 = np.deg2rad(MiddlePos_2+100)
    c.write_goal_position(ID_3, Pos_1)
    c.write_goal_position(ID_4, Pos_2)
    time.sleep(0.01)

def OpenFingerMiddle():
    c.write_goal_speed(ID_5, 6) # Set speed for ID_1 to 6 => Max Speed
    c.write_goal_speed(ID_6, 6) # Set speed for ID_1 to 6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1-190)
    Pos_2 = np.deg2rad(MiddlePos_2+80)
    c.write_goal_position(ID_5, Pos_1)
    c.write_goal_position(ID_6, Pos_2)
    time.sleep(0.01)

def OpenFingerBottom():
    c.write_goal_speed(ID_7, 6) # Set speed for ID_1 to 6 => Max Speed
    c.write_goal_speed(ID_8, 6) # Set speed for ID_1 to 6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1-110)
    Pos_2 = np.deg2rad(MiddlePos_2-160)
    c.write_goal_position(ID_7, Pos_1)
    c.write_goal_position(ID_8, Pos_2)
    time.sleep(0.01)








if __name__ == '__main__':
    main()


