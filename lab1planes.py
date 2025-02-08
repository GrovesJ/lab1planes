from queue import Queue # type: ignore
from stack import Stack
from linkedlist import LinkedList

RUNWAY_LENGTH = 7
HANGAR_SIZE = 5

waiting_runway = Queue()
hangar = Stack()

def checkup(plane) -> bool:
    needs_repairs = False
    if needs_repairs:
        return True
    else:
        return False


def process_planes():
    #input
    while True:
        user_input = input("Name\tNeeds Repairs?[Yes/No]\n")
        if user_input == "":
            return False
        name, repair_status = user_input.split("\t")
        
       
        
        if repair_status == "Yes":
            if hangar.size() < HANGAR_SIZE:
                hangar.push(name)
            else:
                clear_runway()
                hangar_to_runway()
                hangar.push(name)
        elif repair_status == "No" and hangar.size() < HANGAR_SIZE:
            waiting_runway.enqueue(name)
        else:
            clear_runway()
            waiting_runway.enqueue(name)

        clear_runway()
        hangar_to_runway()
        clear_runway()

        

def clear_runway() -> None:
    while waiting_runway.size() > 0:
        print({waiting_runway.dequeue()},"Departing")


def hangar_to_runway() -> None:
    while hangar.size() > 0:
        if  waiting_runway.size() < RUNWAY_LENGTH:
            waiting_runway.enqueue(hangar.pop())
        else:
            clear_runway()
            waiting_runway.enqueue(hangar.pop())


process_planes()