from kivy.app import App
from kivy.graphics import *
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from math import sqrt


x1,y1 = 0,0
x2,y2 = 0,0
x3,y3 = 0,0
f1,f2,f3 = False, False, False
#va=0,0
#vb=0,0
#vc=0,0

class triApp(App):
	def build(self):
		#configure tuio
		Config.set('input', 'fid1', 'tuio,0.0.0.0:3333')
		Tri = tric()
		return Tri



class tric(Widget):
	
	perimeter= NumericProperty(0)
	length1= NumericProperty(0)
	length2= NumericProperty(0)
	length3= NumericProperty(0)
	
	#set window color to white
	Window.clearcolor=(1,1,1,1)
	
	def on_touch_down(self,touch):
		global f1,f2,f3
		global x1,y1,x2,y2,x3,y3
		
		if 'button' in touch.profile:
			print("Exiting..")
			return
		
		#checking for fiducials
		if 'markerid' in touch.profile:
		
		#if fiducial id 1 is detected store respective coordinates in x1,y1 	
			if touch.fid==1:
				x1=touch.pos[0]
				y1=touch.pos[1]
				print("Yes1")
				f1=True
				
		
		#if fiducial id 2 is detected store respective coordinates in x2,y2 		
			if touch.fid==2:
				x2=touch.pos[0]
				y2=touch.pos[1]
				print("Yes2")
				f2=True
				
		
		#if fiducial id 3 is detected store respective coordinates in x3,y3 		
			if touch.fid==3:
				x3=touch.pos[0]
				y3=touch.pos[1]
				print("Yes3")
				f3=True
				
		
		#when all 3 fiducials are detected draw triangle		
			if f1 and f2 and f3:
				#print("kuch toh print kar")
				with self.canvas:
					self.canvas.clear()
					Color(rgb=(0,0,0))
					Line(points=(x1,y1,x2,y2,x3,y3,x1,y1),width = 2.5)
					
					with self.canvas.after:
						#a=(x1,y1)
						#va=Vector(a)
						
						#b=(x2,y2)
						#vb=Vector(b)
						
						#	c=(x3,y3)
						#vc=Vector(c)
						
						length1 = sqrt (pow(x2-x1,2)+pow(y2-y1,2))
						length2 = sqrt (pow(x2-x3,2)+pow(y2-y3,2))
						length3 = sqrt (pow(x3-x1,2)+pow(y3-y1,2))

						#length1 = Vector(va).distance()
						#length2 = Vector(vb).distance()
						#length3 = Vector(vc).distance()
						self.perimeter=0
						self.perimeter = length1 + length2 + length3
									
	
