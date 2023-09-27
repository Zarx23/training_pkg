#!/usr/bin/env python

import rospy #importar ros para python
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from geometry_msgs.msg import Twist, Point # importar mensajes de ROS tipo geometry / Twist


class Template(object):
	def __init__(self, args):
		super(Template, self).__init__()
		self.args = args
		self.sub_dist = rospy.Subscriber("/duckiebot/distanciaPato", Point, self.ruedas)
		#self.sub_joy = rospy.Subscriber("/duckiebot/Controller", Twist2DStamped, self.ruedas)
		self.pub_ruedas = rospy.Publisher("/duckiebot/wheels_driver_node/car_cmd", Twist2DStamped, queue_size=1)
		self.twist= Twist2DStamped()
		#self.punto= Point()
        def ruedas(self,distancia):
		if distancia.z < 15:
			self.twist.v = 0
			self.pub_ruedas.publish(self.twist.v)


	#def publicar(self):

	#def callback(self,msg):


def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Template('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	#rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
