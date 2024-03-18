from puyapy import ARC4Contract, arc4


class Monkay(ARC4Contract):

    @arc4.abimethod()
    def hello(self, name: arc4.String) -> arc4.String:
        return "Hello, " + name

    @arc4.abimethod()
    def goodbye(self, name: arc4.String) -> arc4.String:
        return "Goodbye, " + name

    @arc4.abimethod()
    def lottery(self, name: arc4.String, age: arc4.String) -> arc4.String:
        return "Name, " + name + " " + "Age, " + age
