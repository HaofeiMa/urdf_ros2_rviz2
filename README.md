<h1 align="center">
ROS2+Rviz2 displays URDF model
</h1>

<div align="center">

[![中文文档](https://img.shields.io/badge/%E4%B8%AD%E6%96%87%E6%96%87%E6%A1%A3-ZH_CN-blue)](https://www.mahaofei.com/post/8dd7dd64.html)

</div>


Visualize urdf model in ros2 using rviz2, a example ros2 package with modify tutorial.


## 1. Experimental Environment and Preparation

**Test Environment:**
- Ubuntu 22.04 LTS
- ROS2 Humble

**Preparation:**
- URDF and corresponding Mesh files (This article uses the URDF exported from SolidWorks. For details on how to export it, please refer to this article)

**Dependencies:**
- Ensure your ROS2 installation is functioning correctly (e.g., you can run the turtle demo)
- Install joint_state_publisher and robot_state_publisher:

```shell
sudo apt install ros-$ROS_DISTRO-joint-state-publisher-gui ros-$ROS_DISTRO-robot-state-publisher
```

## 2. Workspace and Package Configuration

```shell
mkdir ros2_ws
cd ros2_ws
```

To simplify the implementation and avoid excessive modifications to files like launch, package, setup.py, etc., you can modify the code uploaded to GitHub in this article ([https://github.com/HaofeiMa/urdf_ros2_rviz2](https://github.com/HaofeiMa/urdf_ros2_rviz2)) to suit your needs. The code contains the UR5e robotic arm model with the Inspire Hand gripper.

```shell
git clone https://github.com/HaofeiMa/urdf_ros2_rviz2.git
```

After this, first, you can test whether it’s ok to build and display the existing model:

```shell
colcon build
source install/setup.bash
ros2 launch urdf_ros2_rviz2 view_robot_launch.py
```

You should see the Rviz2 interface displaying the existing model.

## 3. Modifying the Package

**(1) Create a New Package**

Create your own package and base it on the code you just cloned:

```shell
ros2 pkg create your_package_name --build-type ament_python
```

**(2) Copy Files**

Copy the `launch`, `meshes`, `rviz`, and `urdf` folders from the `urdf_ros2_rviz2` directory to your new `your_package_name` directory.

![image](https://github.com/user-attachments/assets/8d5ac694-674f-4c5f-87d0-b6dafc4acf36)


**(3) Modify setup.py**

Copy all the content of the `setup.py` file from `urdf_ros2_rviz2` into your new package, then modify`setup.py`:

```setup.py
# Line 4
package_name='your_package_name'
```

![image](https://github.com/user-attachments/assets/c753b082-f0cb-4ca2-a4a2-e19d09c08f19)


**(4) Modify package.xml**

Copy all the code from the `package.xml` file in `urdf_ros2_rviz2` and make the following modification:

```xml
<!-- Line 4 -->
<name>your_package_name</name>
```

![image](https://github.com/user-attachments/assets/52db1fff-8b27-4d18-86d2-c251d14e186e)


**(5) Copy Mesh Files**

Copy all your mesh files into the `meshes` folder and delete the original mesh files.

Note: If your `meshes` folder structure is different from mine, make sure to modify the `setup.py` file to reflect the correct STL file paths.

![image](https://github.com/user-attachments/assets/c4254dc8-64cc-4e59-b8b5-792c5fdd0ae7)


**(6) Modify URDF File**

Copy your URDF files into the `urdf` directory of `your_package_name`.

Then, make the necessary modifications: primarily, update the package name and verify that the mesh paths are correct. For example:

```xml
<mesh filename="package://urdf_ros2_rviz2/meshes/ur5e/visual/base.dae"/>
<!-- Change it to -->
<mesh filename="package://your_package_name/meshes/your_path/base.dae"/>
```

**(7) Modify Launch Files**

You need to modify the package name and the URDF file name in the launch files.

![image](https://github.com/user-attachments/assets/5df6f1fc-4143-4b09-93f1-1ff794de5802)


**(8) Modify RViz Configuration**

Open the `rviz/view.rviz` file, find line 85, and modify it as follows:

```yml
# Your model's base frame
Fixed Frame: base_link
```

**(9) Test the Setup**

Run the following commands to test the setup:

```shell
colcon build
source install/setup.bash
ros2 launch test_urdf view_robot_launch.py
```

![image](https://github.com/user-attachments/assets/94ce56c9-ec3f-4bbd-abaa-e8431041ddd3)

![image](https://github.com/user-attachments/assets/af182fb1-ae92-4c03-926b-6ad81954cdce)

