from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.config import Config
from kivy.graphics import Color
from kivy.core.window import Window

'''from kivy.graphics import Color, Rectangle

with PongGame.canvas:
	Color(0,1,0,1)
	self.rect = Rectangle(size=PongGame.size,pos=PongGame.pos)
'''
class PongApp(App):
	def build(self):
		Config.set('input', 'fid1', 'tuio,0.0.0.0:3333')
		Config.set('graphics', 'fullscreen', 'fake')
		#Config.set('window', 'height', 'height/2')
		#Config.set('window', 'left', '50')
		game = PongGame()
		game.serve_ball()
		Clock.schedule_interval(game.update, 1.0 / 60.0)
		return game
                        
class PongPaddle(Widget):
	score = NumericProperty(0)

	def bounce_ball(self, ball):
		if self.collide_widget(ball):
			vx, vy = ball.velocity
			offset = (ball.center_y - self.center_y) / (self.height / 2)
			bounced = Vector(-1 * vx, vy)
			vel = bounced * 1.1
			ball.velocity = vel.x, vel.y + offset

class PongBall(Widget):


	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)
	velocity = ReferenceListProperty(velocity_x, velocity_y)

	
	def move(self):
		self.pos = Vector( *self.velocity) + self.pos

class PongGame(Widget):
	Window.clearcolor=(1,1,1,1)
	ball = ObjectProperty(None)
	player1 = ObjectProperty(None)
	player2 = ObjectProperty(None)

	def serve_ball(self, vel=(4, 0)):
		self.ball.center = self.center
		self.ball.velocity = vel
	def update(self, dt):
		self.ball.move()

		self.player1.bounce_ball(self.ball)
		self.player2.bounce_ball(self.ball)

		if (self.ball.y < self.y) or (self.ball.top > self.top):
			self.ball.velocity_y *= -1

		if self.ball.x < self.x:
			self.player2.score += 1
			self.serve_ball(vel=(4, 0))
		if self.ball.x > self.width:
			self.player1.score += 1
			self.serve_ball(vel=(-4, 0))

	def on_touch_move(self, touch):
		if 'button' in touch.profile:
			print("Exiting..")
			return
		if 'markerid' in touch.profile:
			if touch.fid%2==0:
				self.player1.center_y = touch.pos[1]
			if touch.fid%2==1:
				self.player2.center_y = touch.pos[1]
	'''
			
	def on_touch_move(self,touch):
		if touch.fid==1:
			print("Hello")
		
		print(touch.profile)
		if 'markerid' in touch.profile:
			print("Marker available")
		else:
			print("Marker unavailable")
		'''
		


#if __name__ == '__main__':
#	PongApp().run()


