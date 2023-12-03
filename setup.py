import os
from glob import glob
from setuptools import setup

package_name: str = 'rmclpy'
node_package_name: str = package_name + '.node'
mqtt_package_name: str = package_name + '.mqtt'
topic_package_name: str = package_name + '.topic'
service_package_name: str = package_name + '.service'
action_package_name: str = package_name + '.action'

packages_list: list = [
    package_name,
    node_package_name,
    mqtt_package_name,
    topic_package_name,
    service_package_name,
    action_package_name
]

setup(
    name=package_name,
    version='0.1.0',
    packages=packages_list,
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='reidlo',
    maintainer_email='naru5135@wavem.net',
    description='ROS2 MQTT Client Library for Python',
    license='Apache 2.0 LICENSE',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dynamic_bridge = rmclpy.node.dynamic_bridge:main'
        ],
    },
)
