'''
Open an arcade window that is 500 x 300 pixels and named 1000 Circles.
Create a class called Circle.
Initialize the x and y positions to be randomly placed somewhere in the window.
Initialize the radius to be 10 pixels.
Initialize the color to randomized 0-255 RGB color format.
Add a method to the Circle Class called draw_circle and draw the circle.
In the main program, use a for loop to call the Circle class and draw it 1000 times.
Feel free to see what happens if you draw it 10,000 times as well.
'''
import arcade
import random
import time

class Circle():
    def __init__(self):
        self.x = random.randint(0,800)
        self.y = random.randint(0,450)
        self.radius = random.randint(5,50)
        self.colorR = random.randint(200,230)
        self.colorG = random.randint(0, 200)
        self.colorB = random.randint(50, 255)
        self.segments = random.randint(-1, 6)
        self.tilt = random.randint(0, 360)
    def draw_circle(self):
        arcade.draw_circle_filled(self.x,self.y,self.radius,(self.colorR, self.colorG, self.colorB),self.tilt,self.segments)

def main():

        arcade.open_window(800, 450, "10,000 Circles")
        for i in range(0,3000):
            # time.sleep(.5)
            cir = Circle()
            cir.draw_circle()
        arcade.run()







if __name__ == "__main__":
    main()

