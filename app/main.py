class Animal:
    alive: list = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"Animal: {self.name}, "
                f"health: {self.health}, "
                f"hidden: {self.hidden}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if not isinstance(animal, Herbivore):
            return
        if animal.hidden:
            return
        animal.health -= 50
        if animal.health <= 0 and animal in Animal.alive:
            Animal.alive.remove(animal)
