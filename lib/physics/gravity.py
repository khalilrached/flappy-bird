import pygame
import time
from lib.physics.equation import Equation


class GravityForce:

    def __init__(self, strength, on: pygame.Rect):
        self.start = time.time()
        self.strength = strength
        self.equation = Equation(strength,0,on.y)
        self.rect_object = on

    def add_force(self,strength):
        self.start = time.time()
        self.equation = Equation(self.equation.a,strength,self.rect_object.y)

    def apply(self):
        delta_time = time.time() - self.start
        diff = self.equation.call(delta_time) - self.rect_object.y
        self.rect_object = self.rect_object.move(0, diff)
        # print(f"delta_time={delta_time}, equation::call={self.equation.call(delta_time)}, equation={self.equation}")
        return self.rect_object
