#! /usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge


# global bridge
bridge = CvBridge()

def callback(data):
    global direction

    cv_image =  bridge.imgmsg_to_cv2(data, 'bgr8')
    cv2.imshow('callback',cv_image)
    
    key = cv2.waitKey(5)
    
    if key == ord('w'):
        direction = 'GO'
    elif key == ord('s'):
        direction = 'STOP'
    elif key == ord('x'):
        direction = 'BACK'
    elif key == ord('d'):
        direction = 'RIGHT'
    elif key == ord('a'):
        direction = 'LEFT'
    pub =rospy.Publisher('/motor_commands',String,queue_size=10)
    pub.publish(direction)
    rospy.sleep(0.3)

def main():
    rospy.init_node('planner_node')
    rospy.Subscriber('/camera/image_raw',Image,callback)
    rospy.spin()
   

if __name__ =='__main__':
    direction = None
    main()
    pass