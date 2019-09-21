class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.initialage=initialAge
        if self.initialage<0:
           print("Age is not valid, setting age to 0.")
           self.initialage=0
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.initialage<13:
           print("You are young.")
        if self.initialage>= 13 and self.initialage<18:
           print("You are a teenager.")
        if self.initialage>18:
           print("you are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.initialage+=1

t = int(input())
for i in range(0, t):
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")