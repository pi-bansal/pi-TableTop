def main():
	print("Hello")
	choice=input("1. Pong \n2. Quad \nEnter your choice")
	if choice==2:
		import tri
		tri.triApp().run()
		main()
	elif choice==1:
		import pong
		pong.PongApp().run()
		main()
			
if __name__ == '__main__':
	main()
