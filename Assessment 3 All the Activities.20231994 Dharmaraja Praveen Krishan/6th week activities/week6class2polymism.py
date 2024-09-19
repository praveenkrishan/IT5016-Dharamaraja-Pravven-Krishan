class Device:
    def turn_on(self):
        pass

class Tv(Device):
    def turn_on(self):
        return "Tv is now on"

class Fan(Device):
    def turn_on(self):
        return "Fan is spinning"

class Light(Device):
    def turn_on(self):
        return "Light is on now"

def activate_device(device):
    print(device.turn.on())

tv = Tv()
fan = Fan()
light = Light()

activate_device(tv)
activate_device(fan)
activate_device(light)