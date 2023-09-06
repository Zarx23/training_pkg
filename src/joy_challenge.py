#!/usr/bin/env python

import rospy #importar ros para python
from std_msgs.msg import String, Int32 #importa mensajes de ROS tipo String y Int32
from sensor_msgs.msg import Joy # impor mensaje tipo Joy
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist
from duckietown_msgs.msg import Twist2DStamped 


class Template(object):
    def __init__(self, args):
        super(Template, self).__init__()
        self.args = args
        #sucribir a joy 
        self.sub = rospy.Subscriber("/duckiebot/joy", Joy, self.callback)
        #publicar la intrucciones del control en possible_cmd
        self.publi = rospy.Publisher("/duckiebot/wheels_driver_node/car_cmd", Twist2DStamped, queue_size = 10)
        self.twist = Twist2DStamped()

    def callback(self,msg):
        a = msg.buttons[0]
        y = msg.axes[5]
        x = msg.axes[2]
        z = msg.axes[0]

        print(y, x, z)
        self.twist.omega = -z*15 + 0.098
        self.twist.v = -(y-1) + (x-1)/2

        if a == 1:
            self.twist.omega = 0
            self.twist.v = 0
        
        self.publi.publish(self.twist)
        



def main():
    rospy.init_node('test') #creacion y registro del nodo!

    obj = Template('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

    #objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

    rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
    main()

