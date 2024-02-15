from .wp_visualizer import *
from .random_waypoints_generator import *
from .simulator import *
from sim_msgs.msg import Waypoints
import time

class WpsPublisher(Node):
    def __init__(self):
        super().__init__('wps_publisher')

        self.drone_id = self.declare_parameter(
            'drone_id', 'x').get_parameter_value().string_value

        self.publisher_ = self.create_publisher(Waypoints, 'wps', 1)
        self.send_msg(drone_id)

    def send_msg(self, drone_id):
        wps = self.random()

        time.sleep(0.5)

        wps_msg = Waypoints()
        wps_msg.wps = wps
        drone_id = str(wps_msg.drone_id)

        self.publisher_.publish(wps_msg)

    def random(self):
        return generate_random_waypoints(25, 5)

    def prueba1(self):
        poses = []

        for i in range(0, 17):
            newPos = PoseStamped()
            poses.append(newPos)

        poses[0].pose.position.x = float(0)
        poses[0].pose.position.y = float(0)

        poses[1].pose.position.x = float(20)
        poses[1].pose.position.y = float(80)

        poses[2].pose.position.x = float(40)
        poses[2].pose.position.y = float(0)

        poses[3].pose.position.x = float(70)
        poses[3].pose.position.y = float(20)

        poses[4].pose.position.x = float(90)
        poses[4].pose.position.y = float(80)

        poses[5].pose.position.x = float(110)
        poses[5].pose.position.y = float(80)

        poses[6].pose.position.x = float(110)
        poses[6].pose.position.y = float(0)

        poses[7].pose.position.x = float(130)
        poses[7].pose.position.y = float(0)

        poses[8].pose.position.x = float(130)
        poses[8].pose.position.y = float(80)

        poses[9].pose.position.x = float(150)
        poses[9].pose.position.y = float(80)

        poses[10].pose.position.x = float(150)
        poses[10].pose.position.y = float(0)

        poses[11].pose.position.x = float(210)
        poses[11].pose.position.y = float(20)
        
        poses[12].pose.position.x = float(220)
        poses[12].pose.position.y = float(40)

        poses[13].pose.position.x = float(210)
        poses[13].pose.position.y = float(60)

        poses[14].pose.position.x = float(180)
        poses[14].pose.position.y = float(60)

        poses[15].pose.position.x = float(170)
        poses[15].pose.position.y = float(40)

        poses[16].pose.position.x = float(180)
        poses[16].pose.position.y = float(20)

        return poses

def main():
    # between = input("Meter in between points")
    # number = input("number of points")
    rclpy.init()
    wps_publisher = WpsPublisher()
    rclpy.spin(wps_publisher)

if __name__ == '__main__':
    main()