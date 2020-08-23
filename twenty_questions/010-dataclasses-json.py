from dataclasses import dataclass
from dataclasses_serialization.json import JSONSerializer
import json

@dataclass
class Person:
    eye_color: str
    hair_color: str
    hair_count: int
    name: str
    life_span: int

poobear = Person ('blue', 'red', 400000, 'PooBear', 89)

print(poobear.life_span / 2)

with open('person.json', 'w') as file:
    file.write(json.dumps(JSONSerializer.serialize(poobear)))
