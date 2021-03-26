from virtualbox.library import AccessMode, DeviceType, MediumVariant
from session import VSession

class VDisk:
	def __init__(self, box, filename):
		dvd_path = '/home/ubuntu/Desktop/CC/python/' + filename

		self.medium = box.open_medium(dvd_path, DeviceType.dvd, AccessMode.read_only, True)

	def attach_to_machine(self, machine):
		session = VSession(machine.get_machine())
		session.get_machine().attach_device("IDE", 0, 0, DeviceType.dvd, self.medium)
		session.close()

	def get_medium(self):		
		return self.medium