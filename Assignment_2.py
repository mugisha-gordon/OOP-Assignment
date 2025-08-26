from abc import ABC, abstractmethod

class Moveable(ABC):
    """An abstract base class that requires a move() method."""
    @abstractmethod
    def move(self) -> None:
        pass

# Vehicles
class Car(Moveable):
    def move(self) -> None:
        print("Driving")

class Plane(Moveable):
    def move(self) -> None:
        print("Flying")

class Boat(Moveable):
    def move(self) -> None:
        print("Sailing")

# Animal
class Dog(Moveable):
    def move(self) -> None:
        print("Running")

def perform_moves(things: list[Moveable]) -> None:
    """Call move() on each object to demonstrate polymorphism."""
    for thing in things:
        thing.move()

if __name__ == "__main__":
    # Create a mixed collection of objects that all implement move()
    things = [Car(), Plane(), Boat(), Dog()]

    # Each object responds to the same method name differently
    perform_moves(things)
