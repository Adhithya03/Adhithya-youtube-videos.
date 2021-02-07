from manimlib.imports import *

class requirements(Scene):
	def construct(self):	
		a=Text("Requirements for this video")
		a.shift(UP*3)
		b=Text("PYTHON").set_color_by_gradient(BLUE,YELLOW)
		b.shift(UP*1.5)
		c=Text("PYCHARM").set_color_by_gradient(GREEN,YELLOW)
		c.next_to(b,DOWN,buff=1.1)
		d=Text("ANACONDA").set_color(GREEN)
		d.next_to(c,DOWN,buff=1.1)
		f=Text("If you don't have them please watch my previous video.")
		f.set_color_by_gradient(YELLOW,BLUE,GREEN,PURPLE)
		rect=Rectangle(4,5)
		rect.set_color_by_gradient(YELLOW,BLUE,GREEN,PURPLE)
		newrext=Rectangle(13,1.6)
		VGroup(rect,b,c,d).shift(DOWN*0.5)
		self.wait(1.5)
		self.play(ShowCreation(rect),ShowCreation(a))
		self.play(Write(b))
		self.play(Write(c))
		self.play(Write(d))
		self.wait(2)
		self.play(Uncreate(rect),FadeOut(b,LEFT),FadeOut(c,RIGHT),FadeOut(d,LEFT),Uncreate(a))
		self.play(ShowCreation(newrext),Write(f))
		self.wait(2)
		self.play(Uncreate(newrext),Uncreate(f))
		self.wait()

class titles(Scene):
	def construct(self):
		openingpycharm=Text("Opening pycharm and creating a new project")
		installing_pyautogui=Text("Installing Pyautogui")
		use_of_pyautogui=Text("Some of main functions of Pyautogui include virtual clicking and typing")
		use_of_pyautogui.scale(0.7)
		spam_text=Text("We text some text to spam so we are getting it.")
		store_our_text=Text("We need to store our text in some text file for future use.")
		open_the_file=Text("Opening the file in read mode and store it in a variable.")
		loop=Text("Ok Now I will explain working of for loop ?")
		VGroup(loop[33:36]).set_color(GREEN)
		rect=Rectangle(11,2)
		self.play(ShowCreation(rect),FadeIn(openingpycharm,RIGHT))
		self.wait(1.5)
		self.play(FadeOut(openingpycharm,RIGHT),Uncreate(rect))
		self.wait(2)
		rect=Rectangle(5,1)
		self.play(ShowCreation(rect),FadeIn(installing_pyautogui,RIGHT))
		self.wait(1.5)
		self.play(FadeOut(installing_pyautogui,RIGHT),Uncreate(rect))
		self.wait(2)
		

		rect=Rectangle(12.5,1)
		self.play(ShowCreation(rect),FadeIn(use_of_pyautogui,RIGHT))
		self.wait(3)
		self.play(FadeOut(use_of_pyautogui,RIGHT),Uncreate(rect))
		self.wait(2)
		

		rect=Rectangle(11,2)
		self.play(ShowCreation(rect),FadeIn(spam_text,RIGHT))
		self.wait(2.3)
		self.play(FadeOut(spam_text,RIGHT),Uncreate(rect))
		self.wait(2)

		rect=Rectangle(14,2)
		self.play(ShowCreation(rect),FadeIn(store_our_text,RIGHT))
		self.wait(2)
		self.play(FadeOut(store_our_text,RIGHT),Uncreate(rect))
		self.wait(2)

		rect=Rectangle(13,2)
		self.play(ShowCreation(rect),FadeIn(open_the_file,RIGHT))
		self.wait(2.5)
		self.play(FadeOut(open_the_file,RIGHT),Uncreate(rect))
		self.wait(2)

		rect=Rectangle(11,2)
		self.play(ShowCreation(rect),FadeIn(loop,RIGHT))
		self.wait(1.5)
		self.play(FadeOut(loop,RIGHT),Uncreate(rect))
		self.wait(2)

class forloop(Scene):
	def construct(self):
		first_line=Text("for i in text_file :")
		first_line.shift(UP*1.2)
		second_line=Text("pg.typewrite(i)")
		third_line=Text("pg.press('enter')")
		second_line.next_to(first_line,DOWN,aligned_edge=LEFT+RIGHT*45)
		third_line.next_to(second_line,DOWN,aligned_edge=LEFT)
		VGroup(second_line[2],third_line[2],first_line[0:3],first_line[5:8]).set_color("#f92672")#pink
		VGroup(third_line[9:-1]).set_color("#e6db74")
		VGroup(second_line[3:12],third_line[3:8]).set_color(GREEN) #Green
		self.play(Write(first_line),run_time=1)
		self.play(Write(second_line),run_time=1)
		self.play(Write(third_line),run_time=1)
		self.wait(1)


class forloop(Scene):
	def construct(self):
		rectangle=Rectangle(height=5,width=3.7)
		rectangle.to_corner(RIGHT)
		variable=Text("text_file =",font_size=28,font="Consolas",
            t2s={"slant": ITALIC},
            t2c={"slant": ORANGE, "weight": RED})
		VGroup(rectangle, variable).arrange(LEFT, buff=0.2)
		
		for_syntax=Text("""

			for i in text_file:
				
				pg.typewrite(i)
				
				pg.press('enter')

			""")
		first_line=Text("1.Bee Movie Script - Dialogue Transcript",font_size=20)
		second_line=Text("2.According to all known laws of aviation",font_size=20)
		other_lines=Text("""							3.there is no way a bee.
							
							4.should be able to fly.
							
							5.Its wings are too small to get
							
							6.its fat little body off the ground.
							
							7.The bee, of course, flies anyway
							
							8.because bees don't care
							
							9.what humans think is impossible.
							
							10.Yellow, black. Yellow, black.
							
							11.Yellow, black. Yellow, black.""",font_size=20)
		
		loop=Text("Loop",color=GREEN).scale(1.5)
		first=Text("1",color=PURPLE).scale(1.5)
		second=Text("2",color=PURPLE).scale(1.5)	
