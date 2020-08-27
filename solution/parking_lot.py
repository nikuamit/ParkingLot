from enum import Enum


# Vehicle type class for what all type of vehicles can come for parking
class VehicleType(Enum):
    CAR = 1
    BIKE = 2
    BUS = 3


# Vehicle class for license plate, company name and their type
class Vehicle:
    def __init__(self, licensePlate, companyName, type_of_vehicle):
        self.licensePlate = licensePlate
        self.companyName = companyName
        self.type_of_vehicle = type_of_vehicle

    def getType(self):
        return self.type_of_vehicle

    '''overwrite __eq__ methods to correctly check if two vehicle objects are same. Otherwise, they will be 
    checked at hashcode level not at content level.'''

    def __eq__(self, other):
        if other is None:
            return False
        if self.licensePlate != other.licensePlate:
            return False
        if self.companyName != other.companyName:
            return False
        if self.type_of_vehicle != other.type_of_vehicle:
            return False
        return True


# Car class inherited from Vehicle class for license plate, company name and their type
class Car(Vehicle):
    def __init__(self, licensePlate, companyName):
        Vehicle.__init__(self, licensePlate, companyName, VehicleType.CAR)


# Bike class inherited from Vehicle class for license plate, company name and their type
class Bike(Vehicle):
    def __init__(self, licensePlate, companyName):
        Vehicle.__init__(self, licensePlate, companyName, VehicleType.BIKE)


# Bus class inherited from Vehicle class for license plate, company name and their type
class Bus(Vehicle):
    def __init__(self, licensePlate, companyName):
        Vehicle.__init__(self, licensePlate, companyName, VehicleType.BUS)


class Slots:
    def __init__(self, lane, spotNumber, type_of_vehicle):
        # self.level = level
        self.lane = lane
        self.spotNumber = spotNumber
        self.vehicle = None
        self.type_of_vehicle = type_of_vehicle

    def isAvailable(self):
        return self.vehicle == None

    def park(self, vehicle):
        if vehicle.type_of_vehicle == self.type_of_vehicle:
            self.vehicle = vehicle
            return True
        else:
            return False

    def removeVehicle(self):
        self.vehicle = None
        return self.vehicle

    def getVehicle(self):
        return self.vehicle


'''Level class - Each level is an independent entity with a floor number, its lanes and the slots within it. 
The number of lanes are designed based on the number of slots. 10 slots make one lane'''


class Levels:
    def __init__(self, floorNumber, no_of_slots):
        self.floorNumber = floorNumber
        self.spots_per_lane = 10
        self.lanes = no_of_slots / self.spots_per_lane
        self.parkingSlots = set()
        self.availableSpots = []

        # Check available spots in a lane
        for lane in range(int(self.lanes)):
            for i in range(self.spots_per_lane):
                import random
                # We will randomly assign a type to each slot.
                self.availableSpots.append(Slots(lane, i, random.choice(list(VehicleType))))
                # self.availableSpots.append(Slots(lane, i, type_of_vehicle))

    # Park vehicle is spot is available
    def park(self, vehicle):
        for slot in self.availableSpots:
            if slot.park(vehicle):
                return True
        return False

    # Remove vehicle from a spot
    def remove(self, vehicle):
        for spot in self.availableSpots:
            if spot.getVehicle() == vehicle:
                spot.removeVehicle()
                return True
        return False

    # Company name for the vehicle parked at the available spots
    def companyParked(self, companyName):
        all_vehicles = []
        for spot in self.availableSpots:
            vehicle = spot.getVehicle()
            if (vehicle is not None) and (vehicle.companyName == companyName):
                all_vehicles.append(vehicle)
                #print(all_vehicles)
        return all_vehicles


# A parking lot is made up of 'n' number of levels/floors and 'm' number of slots per floor.
class ParkingLot:
    def __init__(self, no_of_floor, no_of_slot):
        self.levels = []
        for i in range(no_of_floor):
            self.levels.append(Levels(i, no_of_slot))

    # This operation inserts a vehicle accordingly, also takes care of what company vehicle it is.
    def parkVehicle(self, vehicle):
        for level in self.levels:
            if level.park(vehicle):
                return True
        return False

    # This operation exits a vehicle 'C' in a level 'm'.
    def leaveOperation(self, vehicle):
        for level in self.levels:
            if level.remove(vehicle):
                return True

    # This operation allows the user to view the list of vehicles parked for a particular company.
    def companyParked(self, companyName):
        all_vehicles = []
        for level in self.levels:
            all_vehicles.extend(level.companyParked(companyName))
        return all_vehicles
