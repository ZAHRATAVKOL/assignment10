# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:03:51 2022

@author: zahra tavakoli
"""

class First:
    def __init__(self, a, b, c, d):
        self.side1=a
        self.side2=b
        self.side3=c
        self.side4=d
    def perimeter(self):
        p=self.side1 + self.side2 + self.side3 + self.side4
        print("perimeter=",p)
   
class rectangle(First):
    def __init__(self, a, b):
        super().__init__(a, b, a, b)
    def area(self):
        a = self.side1 * self.side2
        print("area of rectangle=", a)
    def perimeter_rec(self):
        p=(self.side1*2) + (self.side2*2) 
        print("perimeter of rectangle=",p)
class Circle(First):
    def __init__(self, a, b):
        super().__init__(a, b, a, b)
    def area_circle(self):
        a_c = (self.side1* self.side1)*3.14
        print("area of Circle=", a_c)
    def perimeter_circle(self):
        p_c=(self.side1 *2)*3.14
        print("perimeter of Circle=",p_c)
        
q1=First(7,5,6,4)
q1.perimeter()

r1=rectangle(10, 20)
r1.area()
p1=rectangle(10,20)
p1.perimeter_rec()

r_circle=Circle(2,0)
r_circle.area_circle()
r2_p=Circle(2,0)
r2_p.perimeter_circle()

