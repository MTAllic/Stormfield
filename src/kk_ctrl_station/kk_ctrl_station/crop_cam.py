import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from PIL import ImageTk, Image as PilImage
import tkinter as tk
from threading import Thread


class ImageSubscriber1(Node):
    def __init__(self):
        super().__init__('crop_cam')
        self.subscription = self.create_subscription(
            Image,
            '/my_camera3/image_raw',  # Replace with your image topic
            self.image_callback,
            10)
        self.subscription  # Prevent unused variable warning

    def image_callback(self, msg):
        image = PilImage.frombytes('RGB', (msg.width, msg.height), bytes(msg.data), 'raw')
        self.display_image(image)

    def display_image(self, image):
        global label
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo


def ros_thread():
    rclpy.init()
    node = ImageSubscriber1()
    rclpy.spin(node)


def main():
    global label
    root = tk.Tk()
    root.title("KloudKat - Crop Cam")

    label = tk.Label(root)
    label.pack()

    ros_thread_instance = Thread(target=ros_thread)
    ros_thread_instance.start()

    root.mainloop()


if __name__ == '__main__':
    main()
