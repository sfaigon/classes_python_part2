class Vehicle():
    def __init__(self,make,model, running = False):
        self.make = make
        self.model = model
        self.running = running
    def start(self):
        self.running = True
        print("running ...")
    def stop(self):
        self.running = False
        print("stopped ...")
    def __str__(self):
        return f"Vehicle is a {self.make} model {self.model}"
car = Vehicle("Tesla", "Model S")
print(car.make, car.model)
print(car)
print(car.running)
car.start()
print(car.running)
car.stop()