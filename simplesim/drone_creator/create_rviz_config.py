import sys

def generate_file(num):
    base_content = """
Panels:
  - Class: rviz_common/Displays
    Name: Displays
  - Class: rviz_common/Views
    Name: Views
Visualization Manager:
  Displays:
    - Class: rviz_default_plugins/Grid
      Name: Grid
      Value: true
      Plane Cell Count: 60
      Cell Size: 20
      Color: 60;60;60

    - Alpha: 0.8
      Class: rviz_default_plugins/RobotModel
      Description Topic:
        Value: /robot_description
      Name: RobotModel
      Value: true
    - Class: rviz_default_plugins/TF
      Name: TF
      Value: true
"""
    
    drone_template = """
    - Class: rviz_default_plugins/Pose
      Name: Pose
      Shape: Axes
      Axes Length: 2
      Axes Radius: 1
      Value: true
      Topic: drone_{0}/pose
      Color: (0,0,0)
    - Class: rviz_default_plugins/Marker
      Name: Marker
      Topic: drone_{0}/marker
      Value: True
    - Class: rviz_default_plugins/PointStamped
      Name: PointStamped
      Topic: drone_{0}/point
      Value: True
      Radius: 0.5
"""
    
    global_options = """
  Global Options:
    Background Color: 255; 255; 255
    Fixed Frame: base_link
    Frame Rate: 60
  Tools:
    - Class: rviz_default_plugins/MoveCamera
  Value: true
  Views:
    Current:
      Class: rviz_default_plugins/Orbit
      Distance: 257.0596923828125
      Enable Stereo Rendering:
        Stereo Eye Separation: 0.05999999865889549
        Stereo Focal Distance: 1
        Swap Stereo Eyes: false
        Value: false
      Focal Point:
        X: 53,825
        Y: 50,907
        Z: 8,4884
      Focal Shape Fixed Size: true
      Focal Shape Size: 0.05000000074505806
      Invert Z Axis: false
      Name: Orbit
      Near Clip Distance: 0.009999999776482582
      Pitch: 0,664797
      Target Frame: <Fixed Frame>
      Value: Orbit (rviz)
      Yaw: 4.6949992179870605
Window Geometry:
  Height: 800
  Width: 1200
"""

    with open("../rviz/auto_many_drones_config.rviz", "w") as file:
        file.write(base_content)
        for i in range(num):
            file.write(drone_template.format(i))
        file.write(global_options)

