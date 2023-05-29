import random
from dataclasses import dataclass, field

import img.characters as images


@dataclass
class Character:
    name: str
    max_hp: int
    damage: int
    image: str
    attack_image: str
    damage_image: str
    attack_expressions: list[str]
    damage_expressions: list[str]
    hp: int = field(init=False)

    def __post_init__(self):
        self.hp = self.max_hp

    def __str__(self) -> str:
        return self.name

    def attack(self, other: "Character") -> int:
        damage_dealt = min(self.damage, other.hp)
        other.hp -= damage_dealt
        return damage_dealt


BART = Character(
    name="Bart Simpson",
    max_hp=random.randint(50, 100),
    damage=random.randint(5, 25),
    image=images.bart,
    attack_image=images.bart_attack,
    damage_image=images.bart_damage,
    attack_expressions=["EAT MY SHORTS!", "GET BENT!", "COWABUNGA!"],
    damage_expressions=["AYYYY CARAMBAA!!!", "AWW, MAN!!", "GOOD GRIEF!!!", "OW, QUIT IT!"],
)
HOMER = Character(
    name="Homer Simpson",
    max_hp=random.randint(70, 120),
    damage=random.randint(1, 15),
    image=images.homer,
    attack_image=images.homer_attack,
    damage_image=images.homer_damage,
    attack_expressions=["WOO HOO!!", "BORING!"],
    damage_expressions=["D'OHH!", "WHY YOU LITTLE!!", "BAAARRRT!!!", "AARGHHH!"],
)
