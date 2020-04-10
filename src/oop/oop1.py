# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    """Base vehicle class"""
    pass


class GroundVehicle(Vehicle):
    """Base Ground Vehicle class"""
    pass


class Car(GroundVehicle):
    """Car class"""
    pass


class Motorcycle(GroundVehicle):
    """Motorcycle class"""
    pass


class FlightVehicle(Vehicle):
    """Base Flight Vehicle class"""
    pass


class Airplane(FlightVehicle):
    """Airplane class"""
    pass


class Starship(FlightVehicle):
    """Starship class"""
    pass
