from typing import List
import dataclasses


@dataclasses.dataclass()
class MyItem(object):
    name: str
    age: int
    children: List[str] = dataclasses.field(default_factory=list)

    def make_me_older(self):
        self.age += 1


item = MyItem(name=["trotl"], age=10, children=["magor", "blbec"])  # typ se nekontroluje, slouzi jen k hintum IDE
item = MyItem(name="trotl", age=10, children=["magor", "blbec"])
print(item)
item.make_me_older()
print(item)
