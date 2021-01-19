from typing import final, overload, runtime_checkable


class BaseClassForFinal(object):

    @final
    def final_method(self):
        print("this is final")


class ChildClassForFinal(BaseClassForFinal):

    def final_method(self):  # typechecking by zde mel hodit error/warning
        print("override")


class ClassWithOverloads(object):

    @overload
    def print(self, msg: int):
        pass

    @overload
    def print(self, msg: str):
        pass

    def print(self, msg):
        if isinstance(msg, str):
            print("Retezec je: %s" % msg)
        elif isinstance(msg, int):
            print("Cislo je: %d" % msg)
        else:
            raise ValueError("Unsupported arguments")


class_with_final_method = ChildClassForFinal()
class_with_final_method.final_method()


overloaded_class = ClassWithOverloads()
overloaded_class.print("retezec")
overloaded_class.print(666)
