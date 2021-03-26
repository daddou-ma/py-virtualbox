from virtualbox import  VirtualBox, Session
from virtualbox.library import ISystemProperties, AccessMode, DeviceType, MediumVariant, IMedium, MediumState, StorageBus, INetworkAdapter, NetworkAttachmentType, LockType
from session import VSession
from network import VNetworkAdapter
from hdd import VHardDisk
from disk import VDisk

class VMachine:
	def __init__(self, box, name):
		self.name = name
		self.box = box

		try:
			self.machine = box.find_machine(name)
		except:
			self.machine = VMachine.create(box, name)

	@staticmethod
	def create(box, name):
		machine = box.create_machine('', name, [], '', '')

		#machine.set_boot_order(1, DeviceType.dvd)
		#machine.bios_settings.ioapic_enabled = True

		box.register_machine(machine)

		session = VSession(machine)
		session.get_machine().add_storage_controller("SATA", StorageBus.sata)
		session.get_machine().add_storage_controller("IDE", StorageBus.ide)
		session.close()

		return machine
	
	def set_cpu_count(self, cpus):
		session = VSession(self.machine)
		session.get_machine().cpu_count = cpus
		session.close()

	def set_memory_size(self, memory):
		session = VSession(self.machine)
		session.get_machine().memory_size = memory
		session.close()

	def set_os_type(self, os_type):
		session = VSession(self.machine)
		session.get_machine().os_type_id = os_type
		session.close()

	def get_machine(self):
		return self.machine
	
	def get_ip(self):
		res = self.machine.enumerate_guest_properties('/VirtualBox/GuestInfo/Net/1/V4/IP')
		return res[1][0]
		
	def launch(self):
		session = Session()
		progress = self.machine.launch_vm_process(session, 'gui', '')
		progress.wait_for_completion()
		self.instance = session

	def launch_headless(self):
		session = Session()
		progress = self.machine.launch_vm_process(session, 'headless', '')
		progress.wait_for_completion()

		self.instance = session

	def shutdown(self):
		self.session.console.power_down()

