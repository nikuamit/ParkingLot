# ParkingLot
-----------------------------------
| Parking lot design using Python |
-----------------------------------


Process Brief :
--------------

This is a Parking lot system designed using object oriented principles in Python.

The objects in my design are ParkingLot, Levels, Slots and Vehicle

Following objects has been considered in the design:

• ParkingLot - A parking lot is made up of 'n' number of levels/floors and 'm' number of slots per floor.

• Levels - Each level is an independent entity with a floor number, its lanes and the slots within it. The number of lanes are designed based on the number of slots. 10 slots make one lane.

• Slots - The slots are considered as the independent entities to each other where in the type of the vehicle is considered to fill the slot.

• Vehicles - Object with plate no., company name and their type. A vehicle has the attributes of license plate and the company it is from.

I have considered Levels and Slots as entities that are independent so that any level can be added with a desired number of spots later.Each time a vehicle comes in or goes out, a list of vehicles for the particular company is updated. Also the available spots are updated in the particular level.

Methods: 

ParkVehicle - This operation inserts a vehicle accordingly, also takes care of what company vehicle it is. 

Leave Operation - This operations exits a vehicle 'C' in a level 'm'. 

CompanyParked - This operation allows the user to view the list of vehicles parked for a particular company.


I believe that this is the start of a discussion and I will be given further instructions after going through this code. Any questions are Welcomed!
