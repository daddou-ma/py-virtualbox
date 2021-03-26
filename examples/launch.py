from virtualbox import  VirtualBox, Session
from machine import VMachine

box = VirtualBox()

def launch_machine(name):
    # Machine Creation
    machine = VMachine(box, name)


    # Launch Machine
    machine.launch()

#create_machine('m3')
launch_machine('tp3')
