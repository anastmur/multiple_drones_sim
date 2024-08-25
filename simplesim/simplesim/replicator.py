from geometry_msgs.msg import PoseStamped
import rclpy
from rclpy.node import Node
import time
import itertools


class Publisher(Node):
    def __init__(self):

        super().__init__('replicator')

        self.publisher_ = self.create_publisher(PoseStamped, '/replicator/pose', 1)

        POSES = self.declare_parameter(
            'poses', ['nun']).get_parameter_value().string_array_value
        
        self.get_logger().info('Received poses publisher')
        
        self.start(POSES)

    def start(self, POSES):
        # time.sleep(3)
        self.get_logger().info('Starting')
        self.get_logger().info(f'[{POSES[0]}]')
        for string in POSES:
            point_str = string.split(";")
            x = float(point_str[0])
            y = float(point_str[1])
            z = float(point_str[2])

            next_pose = PoseStamped()

            next_pose.pose.position.x = x
            next_pose.pose.position.y = y
            next_pose.pose.position.z = z

            next_pose.header.frame_id = "base_link"

            self.publisher_.publish(next_pose)
            self.get_logger().info('Publishing')
            self.get_logger().info(string)
            time.sleep(0.01)


def main():
    rclpy.init()
    pose_replicator = Publisher()
    rclpy.spin(pose_replicator)
    pose_replicator.destroy_node()
    rclpy.shutdown()
