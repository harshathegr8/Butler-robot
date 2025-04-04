# Butter-robot
This is a ros based robot simulation which depicts the robot based simulation

# Launch
For launching the robot in the gazebo environment with the navigation setup run the command **roslaunch robot_navigation amcl_nav.launch** 

# Odering
For ordering to a table enter the command **rostopic pub --once /Order std_msgs/String PBM:2:Table1** this incicates that the order of PBM(paneer butter masala) of 2 quesntities is required for table 1

Similarly **rostopic pub --once /Order std_msgs/String CCM:2:Table2** and **rostopic pub --once /Order std_msgs/String CBM:2:Table3** can also be given which will indicate as order for the respective tables

# Working of the robot
The logic of the robot is based on the node **mind.py** present in the **robot_navigation** package **scripts** folder this will run a node called **Brain** which will subscribe to the **Order** and **Order_cancel** string topics and based on that will publish a topic called **goal_robot** which is a string topic which will denote the room name the robot should go to.
The movement of the robot is based on the node **server.py** present in the **robot_navigation** package **scripts** folder this will run a node called **Server** which will subscribe to the String topic called **goal_robot** which contains the string of the room name the robot should go to. This will then publish a topic called **move_base/goal** which will contain the coordinates of the goal room position based on which the robot will then be made to move by the **move_base** node.
