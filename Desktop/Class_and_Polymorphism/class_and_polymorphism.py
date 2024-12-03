# Assignment 1: Design Your Own Class!
# Creating a Smartphone class and a CameraPhone subclass

class Smartphone:
    def __init__(self, brand, model, battery_level, os):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level
        self.os = os

    def check_battery(self):
        print(f"Battery level is {self.battery_level}%")

    def turn_on(self):
        if self.battery_level > 0:
            print(f"{self.model} is now ON!")
        else:
            print("Battery is too low to turn on!")

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.model}...")

class CameraPhone(Smartphone):
    def __init__(self, brand, model, battery_level, os, camera_megapixels):
        super().__init__(brand, model, battery_level, os)
        self.camera_megapixels = camera_megapixels

    def take_picture(self):
        print(f"Taking a picture with {self.camera_megapixels}MP camera!")

# Example Usage for Assignment 1
smartphone = Smartphone("Samsung", "Galaxy S21", 80, "Android")
smartphone.check_battery()
smartphone.turn_on()
smartphone.install_app("Instagram")

camera_phone = CameraPhone("Apple", "iPhone 14", 50, "iOS", 12)
camera_phone.take_picture()
camera_phone.check_battery()

# Activity 2: Polymorphism Challenge!
# Creating Vehicle classes with different move() implementations

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Example Usage for Activity 2
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
