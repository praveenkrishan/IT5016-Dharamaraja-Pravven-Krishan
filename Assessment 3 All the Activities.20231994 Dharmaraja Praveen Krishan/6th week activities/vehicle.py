class Vehicle:
    def start(self):
        print("Vehicle started.")
        
    def stop(self):
        print("Vehicle stopped.")

class Car(Vehicle):
    def honk(self):
        print("Honk! Honk!")


car = Car()
car.start()
car.honk()
car.stop()