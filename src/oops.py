class circle:
    pi=3.1415
    def __init__(self,radius):
        self.rad=radius
    def cal_area(self):
        self.area=circle.pi*(self.rad**2)
    def cal_parameter(self):
        self.parameter=2*circle.pi*self.rad

radius=int(input("enter radius"))
c=circle(radius)
c.cal_area()
c.cal_parameter()
print(c.__dict__)
c.rad=5
c.area=99
print(c.__dict__)
c1=circle(radius)
print(c1.__dict__)
