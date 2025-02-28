from setuptools import setup
from glob import glob

package_name = 'urdf_ros2_rviz2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, glob('launch/*.py')),
  	('share/' + package_name+'/urdf/', glob('urdf/*')),
  	('share/' + package_name+'/rviz/', glob('rviz/*')),
  	('share/' + package_name+'/meshes/ur5e/collision/', glob('meshes/ur5e/collision/*')),
  	('share/' + package_name+'/meshes/ur5e/visual/', glob('meshes/ur5e/visual/*')),
    ('share/' + package_name+'/meshes/inspire_hand/', glob('meshes/inspire_hand/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros-industrial',
    maintainer_email='olmer@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
