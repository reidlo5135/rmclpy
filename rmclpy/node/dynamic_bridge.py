import rclpy

from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.exceptions import ROSInterruptException

from ..mqtt.mqtt_client import Client


class DynamicBridge(Node):
    def __init__(self) -> None:
        self.mqtt_client: Client = Client(self)
        self.mqtt_client.connect()
        self.mqtt_client.run()


def main(args=None) -> None:
    rclpy.init(args=args)

    try:
        node: Node = DynamicBridge()
        node_name: str = node.get_name()
        multi_threaded_executor: MultiThreadedExecutor = MultiThreadedExecutor()
        multi_threaded_executor.add_node(node = node)
        multi_threaded_executor.spin()
    except ROSInterruptException as rie:
        node.get_logger().warn(f'===== {node_name} terminated with Ctrl-C {rie} =====')

    rclpy.shutdown()


if __name__ == '__main__':
    main()