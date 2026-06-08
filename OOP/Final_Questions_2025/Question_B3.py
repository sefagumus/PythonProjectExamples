class Vehicles:
    def __init__(self, brand, model, max_speed, max_acceleration, plate):
        self.brand= brand
        self.model = model
        self.max_hiz = max_speed
        self.max_acceleration = max_acceleration
        self.plate = plate

class Garage:
    def __init__(self):
        self.vehicles = []


    def Add(self, vehicle):
        self.vehicles.append(vehicle)


    def Remove(self, plate):

        for vehicle in self.vehicles:

            if vehicle.plate == plate:
                self.vehicles.remove(vehicle)
                print("Vehicle removed")
                return

        print("Vehicle not found")


    def ListVehicles(self):

        for vehicle in self.vehicles:
            print(
                vehicle.brand,
                vehicle.model,
                vehicle.plate
            )


v1 = Vehicles("BMW", "320", 240, 7.2, "34LTE339")
v2 = Vehicles("Audi","A8", 200, 6.8, "07BGZ34")

g = Garage()
g.Add(v1)
g.Add(v2)

g.ListVehicles()
g.Remove("07BGZ34")
g.ListVehicles()