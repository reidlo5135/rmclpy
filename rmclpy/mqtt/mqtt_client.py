import paho.mqtt.client as mqtt

from rclpy.node import Node

from typing import Any


MQTT_TRANSPORT_TYPE_WS: str = 'websockets'
MQTT_TRANSPORT_TYPE_TCP: str = 'tcp'
MQTT_WEBSOCKETS_PATH: str = '/ws'


class Client:

    def __init__(self, node: Node) -> None:
        self.client: mqtt.Client
        self.node: Node = node
        
        self.broker_address: str = 'localhost'
        self.broker_port: int = 1883
        self.__client_name: str = 'klsqjfioqweklrnkl'
        self.__client_keep_alive: int = 60
        self.__user_name: str = ''
        self.__password: str = '1234'
        self.__type: str = 'tcp'
        self.is_connected: bool = False
        

    def connect(self) -> None:
        try:
            if self.__type == MQTT_TRANSPORT_TYPE_TCP:
                self.client = mqtt.Client(self.__client_name, clean_session = True, userdata = None, transport = MQTT_TRANSPORT_TYPE_TCP)
            elif self.__type == MQTT_TRANSPORT_TYPE_WS:
                self.client = mqtt.Client(self.__client_name, clean_session = True, userdata = None, transport = MQTT_TRANSPORT_TYPE_WS)
                self.client.ws_set_options(path = MQTT_WEBSOCKETS_PATH)
            else:
                return
            self.client.username_pw_set(self.__user_name, self.__password)
            
            self.client.on_connect = self.__on_connect
            self.client.on_disconnect = self.__on_disconnect
            self.client.on_message = self.__on_message
            self.client.connect(self.broker_address, self.broker_port, self.__client_keep_alive)

            if self.client.is_connected:
                self.node.get_logger().info(f'MQTT Client is connected to [{self.broker_address}:{self.broker_port}]')
                self.is_connected = self.client.is_connected
            else:
                self.node.get_logger().error('MQTT failed to connect')
                self.is_connected = self.client.is_connected
        except OSError as ose:
            self.node.get_logger().error(f'MQTT OSError : {ose}')
        except Exception as e:
            self.node.get_logger().error(f'MQTT Error : {e}')
    

    def run(self) -> None:
        if self.is_connected:
            self.node.get_logger().info('MQTT Client is running')
            self.client.loop_start()
        else:
            self.node.get_logger().error('MQTT Client is not connected to broker')
            return


    def rerun(self) -> None:
        self.client.disconnect()
        self.client.loop_stop()
        self.run()


    def __on_connect(self, client: Any, user_data: Any, flags: Any, rc: Any) -> None:
        if rc == 0:
            self.node.get_logger().info(f'MQTT connection succeeded result code : [{str(rc)}]')
        else:
            self.node.get_logger().error(f'MQTT connection failed result code : [{str(rc)}] ')
            
    
    def __on_disconnect(self, client: Any, user_data: Any, rc: Any) -> None:
        if rc != 0:
            self.node.get_logger().error(f'MQTT disconnection result code : [{str(rc)}] ')
            self.rerun()
            

    def __on_message(self, client: Any, user_data: Any, msg: Any) -> None:
        pass
    

    def publish(self, topic: str, payload: Any, qos: int) -> None:
        self.client.publish(topic = topic, payload = payload, qos = qos)


    def subscribe(self, topic: str, qos: int) -> None:     
        self.node.get_logger().info(f'MQTT granted subscription\n\ttopic : {topic}\n\tqos : {qos}')
        self.client.subscribe(topic = topic, qos = qos)


__all__ = ['mqtt_client']