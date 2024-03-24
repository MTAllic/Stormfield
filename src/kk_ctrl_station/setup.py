from setuptools import setup

package_name = 'kk_ctrl_station'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='m_talha_aamir',
    maintainer_email='mtalhaaamir11@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "control_rover = kk_ctrl_station.control_rover:main",
            "front_cam = kk_ctrl_station.front_cam:main",
            "back_cam = kk_ctrl_station.back_cam:main",
            "crop_cam = kk_ctrl_station.crop_cam:main"
        ],
    },
)
