from virtualbox import  VirtualBox, Session
from virtualbox.library import ISystemProperties, AccessMode, DeviceType, MediumVariant, IMedium, MediumState, StorageBus, INetworkAdapter, NetworkAttachmentType
from machine import VMachine
from network import VNetworkAdapter
from hdd import VHardDisk
from disk import VDisk

box = VirtualBox()

def create_machine(name):
    # Hard Disk Creation
    hdd = VHardDisk(box, 'hdisk.vdi', 20)

    # DVD Creation
    dvd = VDisk(box, 'ubuntu-18.04.2-live-server-amd64.iso')

    # Machine Creation
    machine = VMachine(box, name)

    # Configure
    machine.set_cpu_count(2)
    machine.set_memory_size(512)
    machine.set_os_type('Ubuntu_64')

    # HardDisk & DVD Attachement
    hdd.attach_to_machine(machine)
    dvd.attach_to_machine(machine)

    # NAT Network
    host_only_network = VNetworkAdapter(box, machine, NetworkAttachmentType.host_only, 'vboxnet0')
    host_only_network.attach_to_machine(machine, 0)

    # HostOnly Network
    host_only_network = VNetworkAdapter(box, machine, NetworkAttachmentType.bridged, 'wlp2s0')
    host_only_network.attach_to_machine(machine, 1)

create_machine('tp3')
