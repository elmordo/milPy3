from typing  import List, Callable, NoReturn


ChildList = List["Child"]
FindChildFn = Callable[[ChildList], "Child"]


class Parent(object):

    def __init__(self, child: "Child"):
        self.children: ChildList = [child]
        child.parent = self

    def find_child(self, fn: FindChildFn) -> "Child":
        return fn(self.children)

class Child(object):

    def __init__(self):
        self.parent: Parent = None

    def no_return() -> NoReturn:
        pass
