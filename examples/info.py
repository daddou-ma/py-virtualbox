from virtualbox import  VirtualBox, Session
from machine import VMachine

box = VirtualBox()

def show_information(name):
    # Machine Creation
    machine = VMachine(box, name)

    # Print Machine IP
    print("IP: " + machine.get_ip())

#create_machine('m3')
show_information('m3')
