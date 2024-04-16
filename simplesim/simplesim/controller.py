from .wp_visualizer import *
from .random_waypoints_generator import *
from .simulator import *
from sim_msgs.msg import Waypoints
import time

class WpsPublisher(Node):
    def __init__(self):
        super().__init__('wps_publisher')

        self.drone_wps = self.declare_parameter(
            'waypoints', ['nun']).get_parameter_value().string_array_value
        
        self.get_logger().info(f'drone_wps: {str(self.drone_wps)}')

        self.publisher_ = self.create_publisher(Waypoints, 'wps', 1)
        self.send_msg(self.drone_wps)

    def send_msg(self, drone_wps):
        wps = self.process_waypoints(drone_wps)

        time.sleep(0.5)

        wps_msg = Waypoints()
        wps_msg.wps = wps

        self.publisher_.publish(wps_msg)

    def process_waypoints(self, drone_wps):
        '''
        Procesa el waypoint dado
        '''
        poses = []
        for waypoint_array in drone_wps:
            if isinstance(waypoint_array, str):
                waypoint = waypoint_array.split(";")
                self.get_logger().info('Waypoints in String format')
            else:
                waypoint = waypoint_array
                self.get_logger().info('Waypoints in array format')
            x = float(waypoint[0])
            y = float(waypoint[1])
            z = float(waypoint[2])
            
            newPos = PoseStamped()
            newPos.pose.position.x = x
            newPos.pose.position.y = y
            newPos.pose.position.z = z
            poses.append(newPos)

        return poses

    def random(self):
        return generate_random_waypoints(25, 10)

def main():
    rclpy.init()
    wps_publisher = WpsPublisher()
    rclpy.spin(wps_publisher)
    wps_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()