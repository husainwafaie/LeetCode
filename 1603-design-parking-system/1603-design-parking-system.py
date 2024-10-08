class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.dct = {}
        self.dct[1] = big
        self.dct[2] = medium
        self.dct[3] = small

    def addCar(self, carType: int) -> bool:
        if self.dct[carType] != 0:
            self.dct[carType] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)