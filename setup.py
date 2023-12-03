from setuptools import setup

package_name: str = 'rmclpy'

packages_list: list = [
    package_name
]

setup(
    name=package_name,
    version='0.1.0',
    packages=packages_list,
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
        ],
    },
)
