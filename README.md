# rmclpy(ROS2 MQTT Client Library for Python)

## Document
- [rmclpy - rmclpy ROS2 MQTT Client Library for Python](#rmclpyros2-mqtt-client-library-for-python)
  - [Document](#document)
  - [Environment](#1-environment)
  - [SetUp Installation](#2-setup-installation)
    - [Prerequisites](#2-1-prerequisites)
      - [Install mosquitto 1.6.9](#2-1-1-install-mosquitto-169)
    - [Install python-dev-is-python3](#2-2-install-python-dev-is-python3)
    - [Install rosbridge library](#2-3-installing-rosbridge-library)
  - [Clone & Build Project](#3-clone--build-project)
    - [Clone Project](#3-1-clone-project)
    - [Install pip Requirements](#3-2-install-pip-requirements)
    - [Build Project](#3-3-build-project)
  - [Usage Examples](#4-usage-examples)


## 1. Environment
* <img src="https://img.shields.io/badge/ROS2 Foxy-22314E?style=for-the-badge&logo=ros&logoColor=white">
* <img src="https://img.shields.io/badge/python 3.8.10-3776AB?style=for-the-badge&logo=python&logoColor=white">
* <img src="https://img.shields.io/badge/mqtt-660066?style=for-the-badge&logo=mqtt&logoColor=white">
* <img src="https://img.shields.io/badge/ubuntu 20.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white">

## 2. SetUp Installation

### 2-1. Prerequisites

Before installing, please ensure the following software is installed and configured on your system:

- [ubuntu](https://ubuntu.com/) version required 20.04 - **INSTALL [ubuntu 20.04](https://ubuntu.com/)**

- [mosquitto](https://mosquitto.org/) version required 1.6.9 - **INSTALL [mosquitto 1.6.9](https://mosquitto.org/)**

- [ROS2](https://index.ros.org/doc/ros2/Installation/) version required Foxy-Fitzroy -
  **INSTALL [ROS2 Foxy-Fitzroy](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html)**

### 2-1-1. Install mosquitto 1.6.9
```bash
sudo apt-get update
sudo apt-get install mosquitto-dev
```

### 2-2. Install python-dev-is-python3
```bash
sudo apt install python3-sphinx python3-pip
sudo -H pip3 install sphinx_autodoc_typehints
sudo apt-get install python-dev-is-python3
```

### 2-3. Install rosbridge library
```bash
sudo apt-get install ros-foxy-rosbridge-library
```

## 3. Clone & Build Project

### 3-1. Clone Project
```bash
cd ${your ros2 workspace}/src
git clone https://github.com/reidlo5135/rmclpy.git
```

### 3-2. Install pip Requirements
```bash
cd ${your ros2 workspace}/src/rmclpy
pip install -r requirements.txt
```

### 3-3. Build Project
```bash
cd ~/${your ros2 workspace}/
colcon build --packages-select rmclpy
```

## 4. Usage Examples
```bash
ros2 launch rmclpy rmclpy.launch.py
```