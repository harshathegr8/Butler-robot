# Butter-robot
This is a ros based robot simulation which depicts the robot based simulation

# Launch
For launching the robot in the gazebo environment with the navigation setup run the command **roslaunch robot_navigation amcl_nav.launch** 

# Odering
For ordering to a table enter the command **rostopic pub --once /Order std_msgs/String PBM:2:Table1** this incicates that the order of PBM(paneer butter masala) of 2 quesntities is required for table 1

Similarly **rostopic pub --once /Order std_msgs/String CCM:2:Table2** and **rostopic pub --once /Order std_msgs/String CBM:2:Table3** can also be given which will indicate as order for the respective tables

# Working of the robot
The logic of the robot is based on the node **mind.py** present in the **robot_navigation** package **scripts** folder 
The movement of the robot is based on the node **server.py** present in the **robot_navigation** package **scripts** folder 
