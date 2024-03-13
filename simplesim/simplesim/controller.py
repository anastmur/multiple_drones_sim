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
        # if drone_id == 'drone_0':
        #     wps = self.prueba3()
        # elif drone_id == 'drone_1':
        #     wps = self.prueba2()
        # else:
        #     wps = self.prueba4()

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

    def prueba1(self):
        poses = []

        for i in range(0, 17):
            newPos = PoseStamped()
            poses.append(newPos)

        poses[0].pose.position.x = float(0)
        poses[0].pose.position.y = float(0)

        poses[1].pose.position.x = float(20)
        poses[1].pose.position.y = float(80)
        poses[1].pose.position.z = float(50)

        poses[2].pose.position.x = float(40)
        poses[2].pose.position.y = float(0)
        poses[2].pose.position.z = float(0)

        poses[3].pose.position.x = float(70)
        poses[3].pose.position.y = float(20)
        poses[3].pose.position.z = float(-20)

        poses[4].pose.position.x = float(90)
        poses[4].pose.position.y = float(80)
        poses[4].pose.position.z = float(-40)

        poses[5].pose.position.x = float(110)
        poses[5].pose.position.y = float(80)
        poses[5].pose.position.z = float(-20)

        poses[6].pose.position.x = float(110)
        poses[6].pose.position.y = float(0)

        poses[7].pose.position.x = float(130)
        poses[7].pose.position.y = float(0)

        poses[8].pose.position.x = float(130)
        poses[8].pose.position.y = float(80)
        poses[8].pose.position.z = float(50)

        poses[9].pose.position.x = float(150)
        poses[9].pose.position.y = float(80)
        poses[9].pose.position.z = float(50)

        poses[10].pose.position.x = float(150)
        poses[10].pose.position.y = float(0)
        poses[10].pose.position.z = float(20)

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
    
    def prueba2(self):
        poses = []

        for i in range(0, 10):
            newPos = PoseStamped()
            poses.append(newPos)

        poses[0].pose.position.x = float(0)
        poses[0].pose.position.y = float(0)

        poses[1].pose.position.x = float(80)
        poses[1].pose.position.y = float(0)
        poses[1].pose.position.z = float(-10)

        poses[2].pose.position.x = float(0)
        poses[2].pose.position.y = float(40)
        poses[2].pose.position.z = float(0)

        poses[3].pose.position.x = float(80)
        poses[3].pose.position.y = float(40)
        poses[3].pose.position.z = float(0)

        poses[4].pose.position.x = float(50)
        poses[4].pose.position.y = float(80)
        poses[4].pose.position.z = float(0)

        poses[5].pose.position.x = float(0)
        poses[5].pose.position.y = float(80)
        poses[5].pose.position.z = float(0)

        poses[6].pose.position.x = float(0)
        poses[6].pose.position.y = float(120)
        poses[6].pose.position.z = float(20)

        poses[7].pose.position.x = float(40)
        poses[7].pose.position.y = float(160)
        poses[7].pose.position.z = float(0)

        poses[8].pose.position.x = float(80)
        poses[8].pose.position.y = float(120)
        poses[8].pose.position.z = float(10)

        poses[9].pose.position.x = float(40)
        poses[9].pose.position.y = float(120)
        poses[9].pose.position.z = float(0)

        return poses
    
    def prueba3(self):
        poses = []

        for i in range(0, 10):
            newPos = PoseStamped()
            poses.append(newPos)

        poses[0].pose.position.x = float(110)
        poses[0].pose.position.y = float(80)
        poses[0].pose.position.z = float(0)

        poses[1].pose.position.x = float(110)
        poses[1].pose.position.y = float(0)

        poses[2].pose.position.x = float(130)
        poses[2].pose.position.y = float(0)

        poses[3].pose.position.x = float(130)
        poses[3].pose.position.y = float(80)
        poses[3].pose.position.z = float(20)

        poses[4].pose.position.x = float(150)
        poses[4].pose.position.y = float(80)
        poses[4].pose.position.z = float(10)

        poses[5].pose.position.x = float(150)
        poses[5].pose.position.y = float(0)
        poses[5].pose.position.z = float(20)

        poses[6].pose.position.x = float(210)
        poses[6].pose.position.y = float(20)
    
        poses[7].pose.position.x = float(220)
        poses[7].pose.position.y = float(40)
        poses[7].pose.position.z = float(0)

        poses[8].pose.position.x = float(210)
        poses[8].pose.position.y = float(60)
        poses[8].pose.position.z = float(0)

        poses[9].pose.position.x = float(180)
        poses[9].pose.position.y = float(60)
        poses[9].pose.position.z = float(10)

        return poses
    
    def prueba4(self):
        poses = []

        for i in range(0, 10):
            newPos = PoseStamped()
            poses.append(newPos)

        poses[0].pose.position.x = float(-100)
        poses[0].pose.position.y = float(50)

        poses[1].pose.position.x = float(-80)
        poses[1].pose.position.y = float(120)

        poses[2].pose.position.x = float(-80)
        poses[2].pose.position.y = float(0)

        poses[3].pose.position.x = float(-60)
        poses[3].pose.position.y = float(0)

        poses[4].pose.position.x = float(-60)
        poses[4].pose.position.y = float(120)

        poses[5].pose.position.x = float(-40)
        poses[5].pose.position.y = float(80)

        poses[6].pose.position.x = float(-40)
        poses[6].pose.position.y = float(60)

        poses[7].pose.position.x = float(-20)
        poses[7].pose.position.y = float(50)

        poses[8].pose.position.x = float(-20)
        poses[8].pose.position.y = float(20)
        
        poses[9].pose.position.x = float(-100)
        poses[9].pose.position.y = float(50)

        return poses

def main():
    rclpy.init()
    wps_publisher = WpsPublisher()
    rclpy.spin(wps_publisher)

if __name__ == '__main__':
    main()