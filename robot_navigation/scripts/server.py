#!/usr/bin/env python3
import rospy
from move_base_msgs.msg import MoveBaseActionGoal
import tf
from geometry_msgs.msg import Quaternion,PoseWithCovarianceStamped
from std_msgs.msg import String
from actionlib_msgs.msg import GoalStatusArray

a = [2]
class var:
    def __init__(self):
    	self.val = 0
Rooms = ["Kitchen","Table1","Table2","Table3","Home"]
positions = {"Kitchen":[-6.593123912811279,-4.76052713394165,-0.04910203355782901,0.9987937676520042], #In format of [x,y,z,w] x,y for position and z,w for orientation
"Table1":[4.198648929595947,-4.5905866622924805,-0.02406874683506601,0.999710305751516],
"Table2":[3.284440040588379,0.3772444725036621,-0.014928150547790033,0.999888568952172],
"Table3":[3.595571994781494,4.586675643920898,0.0639926354087079,0.9979503708168298],

"Home":[-5.917774677276611,3.025883197784424,-0.011848303790638982,0.9999298063850706]}

i,R,c = var(),var(),var()
def talker(goal):
    pub = rospy.Publisher("move_base/goal", MoveBaseActionGoal,queue_size=0)
    data = MoveBaseActionGoal()
    data.goal.target_pose.header.stamp = rospy.rostime.Time.now()
    data.header.stamp = rospy.rostime.Time.now()
    data.goal.target_pose.header.frame_id = 'map' 
    
    data.goal.target_pose.pose.position.x = goal[0]
    data.goal.target_pose.pose.position.y = goal[1]
    data.goal.target_pose.pose.orientation.z = goal[2]
    data.goal.target_pose.pose.orientation.w = goal[3]
    rate = rospy.Rate(10) # 10hz
    c =0
    while not rospy.is_shutdown():
    	pub.publish(data)
    	rate.sleep()
    	c+=1
    	if c>10:break

    
def callback2(data):
    if c.val == 0:
    	R.val = rospy.Time.now().secs
    	talker(positions[Rooms[i.val]])
    	c.val+=1
    elif data.status_list[-1].text == "Goal reached.":
    	i.val+=1
    	if i.val==6:
    	    i.val=0
    	talker(positions[Rooms[i.val]])
    elif data.status_list[-1].text == "Failed to find a valid plan. Even after executing recovery behaviors.":
    	pass
    else:
    	pass  

def callback(data):
    talker(positions[data.data])

def listener():
    global processing, new_msg, msg
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('moving', anonymous=True)
    #rospy.Subscriber("move_base/status", GoalStatusArray, callback)
    rospy.Subscriber("goal_robot", String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    
    rospy.spin()

if __name__ == '__main__':
    listener()
