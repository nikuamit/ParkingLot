import unittest
from parking_lot import ParkingLot, Car, Bike, Bus


class TestParkingLot(unittest.TestCase):

    def test_park(self):
        parkingLotObj = ParkingLot(6, 30)
        res2 = parkingLotObj.parkVehicle(Car(10, "Amazon"))
        res3 = parkingLotObj.parkVehicle(Bike(20, "Amazon"))
        res4 = parkingLotObj.parkVehicle(Bus(30, "Microsoft"))

        self.assertEqual(res2, True)
        self.assertEqual(res3, True)
        self.assertEqual(res4, True)


    def test_leave_operation(self):
        parkingLotObj = ParkingLot(6, 30)
        self.assertTrue(parkingLotObj.parkVehicle(Car(20, "Google")))
        #self.assertTrue(parkingLotObj.leaveOperation(Car(10, "Google")))
        self.assertTrue(parkingLotObj.leaveOperation(Car(20, "Google")))
        self.assertEqual(parkingLotObj.leaveOperation(Car(20, "Google")), None)


    def test_companyParked(self):
        parkingLotObj = ParkingLot(6, 30)
        # res1 = parkingLotObj.parkVehicle(Car(20, "Google"))
        # res2 = parkingLotObj.companyParked("Google")
        self.assertTrue(parkingLotObj.parkVehicle(Car(20, "Google")))
        self.assertEqual(parkingLotObj.companyParked("Google"), [Car(20, "Google")])
        #self.assertEqual(parkingLotObj.companyParked("Google"), Car(10, "Google"))
        print(parkingLotObj.companyParked("Google"))


    def test_all(self):
        parkingLotObj = ParkingLot(3, 10)
        # Atleast 1 parking spot for car.
        # First park a car, it should return True.
        self.assertTrue(parkingLotObj.parkVehicle(Car(10, "Google")))
        # Get the list of cars, it should give one car we parked.
        self.assertEqual(parkingLotObj.companyParked("Google"), [Car(10, "Google")])
        # Remove that car successfully.
        self.assertTrue(parkingLotObj.leaveOperation(Car(10, "Google")))
        # Now the list of cars should be empty.
        self.assertEqual(parkingLotObj.companyParked("Google"), [])


if __name__ == '__main__':
    unittest.main()
