#!/usr/bin/env python3
import rospy
from move_base_msgs.msg import MoveBaseActionGoal
import tf
from geometry_msgs.msg import Quaternion,PoseWithCovarianceStamped
from std_msgs.msg import String
from actionlib_msgs.msg import GoalStatusArray,GoalID
global order_list,goal_list
order_list = {}
goal_list = []
class var:
    def __init__(self):
    	self.val = 0
Rooms = ["Kitchen","Table1","Table2","Table3","Home"]

def callback(data):
    global order_list,goal_list
    order = data.data
    order_list[order]="Preparing"
    print(order_list)
    if goal_list==[]:
    	room = "Kitchen"
    	goal_list.append(room)
    	talker(room)
    	
def callback3(data):
    global order_list,goal_list
    cancel_pub = rospy.Publisher('/move_base/cancel', GoalID, queue_size=10)
    
    cancel_msg = GoalID()
    cancel_pub.publish(cancel_msg)
    global order_list,goal_list
    order = data.data
    menu,no,table = order.split(":")
    if table in goal_list:
        goal_list.remove(table)
        if order_list[order]=="Delievering":
            order_list[order]="Cancelled return to kitchen"
        elif order_lisr[order]=="Preparing":
            order_list[order]="Cancelled at kitchen"
    
    
def talker(room):
    pub = rospy.Publisher("goal_robot", String,queue_size=0)
    data = String()
    data.data = room
    c =0
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
    	pub.publish(data)
    	rate.sleep()
    	c+=1
    	if c>10:break

def callback2(data):
    global order_list,goal_list
    if data.status_list[-1].text == "Goal reached." and goal_list!=[]:
    	room = goal_list[0]
    	goal_list = goal_list[1:]
    	if room=="Kitchen" and goal_list==[]:
    	    for i in order_list.keys():
    	        order_list[i] = "Delivering"
    	        menu,no,table = i.split(":")
    	        goal_list.append(table)
    	    talker(goal_list[0])
    	elif goal_list==[]:
    	    if "Cancelled return to kitchen" in order_list.values():
    	    	for i in order_list.keys():
    	    	    order_list[i] ="Delievered"
    	    	talker("Kitchen")
    	    else:
    	    	for i in order_list.keys():
    	    	    order_list[i] ="Delievered"
    	    	talker("Home")
    	    
    	else:
    	    talker(goal_list[0])
    	

def listener():
    global processing, new_msg, msg
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('brain', anonymous=True)
    rospy.Subscriber("move_base/status", GoalStatusArray, callback2)
    rospy.Subscriber("Order", String, callback)
    rospy.Subscriber("Order_cancel", String, callback3)
    # spin() simply keeps python from exiting until this node is stopped
    
    rospy.spin()

if __name__ == '__main__':
    listener()
