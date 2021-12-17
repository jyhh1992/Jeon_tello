import cv2 as cv
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String

from cv_bridge import CvBridge
bridge = CvBridge()
direction = None
def callback(data):
    cv_image = bridge.imgmsg_to_cv2(data, 'bgr8')

    cv.imshow('callback', cv_image)
    key = cv.waitKey(1)
    
    if key == ord('w'):
        direction = 'GO'    # go
    elif key == ord('s'):
        direction = 'STOP'    # stop
    elif key == ord('x'):
        direction = 'BACK'    # back
    elif key == ord('a'):
        direction = 'LEFT'    # left
    elif key == ord('d'):
        direction = 'RIGHT'    # right
    pub = rospy.Publisher('/motor_commands', String, queue_size=10)
    pub.publish(direction)
    # rospy.sleep(0.3)

def main():
    rospy.init_node('planner_node')
    rospy.Subscriber('/camera/image_raw', Image, callback)
    rospy.spin()

if __name__ == '__main__':
    main()

    pass
