from algopy import (
    ARC4Contract,
    String,
    BoxMap,
    arc4,
    subroutine
)
from algopy.arc4 import abimethod

class BoxKey(arc4.Struct):
    index: arc4.UInt64

class BoxValue(arc4.Struct):
    greeting: arc4.String

class HelloWorld(ARC4Contract):
    def __init__(self) -> None:
        self.greetings = BoxMap(BoxKey, BoxValue)

    @abimethod()
    def storeGreeting(self, indice: arc4.UInt64, name: String) -> None:
        key = BoxKey(
            index=indice
        )
        self.greetings[key] = BoxValue(
            greeting= arc4.String("Hello" + name)
        )
    
    @abimethod()
    def getGreeting(self, indice: arc4.UInt64) -> arc4.String:
        key = BoxKey(
            index=indice
        )
        return self.greetings[key].greeting
