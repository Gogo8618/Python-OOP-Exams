from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):

    MAX_MILEAGE = 180.00
    ADDITIONAL_ENERGY = 5

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=self.MAX_MILEAGE)

    def drive(self, mileage):

        self.battery_level -= (round(mileage / self.MAX_MILEAGE *100) + self.ADDITIONAL_ENERGY)