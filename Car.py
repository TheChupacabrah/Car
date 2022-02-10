#Car Class
#John Hatch
class Car(object):
    
    condition = "The DeLorean is new"
    print(condition)
    
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
        
        #print(model, color, mpg)
    
    def display_car(self):
        print("This is a " + self.color + self.model + " with " + self.mpg + " MPG") 
    
    def drive_car(self):
        self.condition = "After driving, the DeLorean is used"
        print(self.condition) 

my_car = Car("DeLorean", "Silver ", "88")
my_car.display_car()
my_car.drive_car()

print()

class Ecar(Car):
    
    condition = "The red Tesla is brand new"
    print(condition)
    
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type
    
    def display_car(self):
        print("This is a " + self.color + self.model + " with a " + self.battery_type + " battery")
        
    def drive_car(self):
        self.condition = "After driving, the red Tesla is still like new"
        print(self.condition)
        
my_e_car = Ecar("Tesla", "Red ", "0", "molten salt")
my_e_car.display_car()
my_e_car.drive_car()
