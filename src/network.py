from session import VSession
from virtualbox.library import NetworkAttachmentType

class VNetworkAdapter:
	def __init__(self, box, machine, adapter_type, adapter_name):
		self.adapter_type = adapter_type
		self.adapter_name = adapter_name

		if adapter_type == NetworkAttachmentType.nat_network:
			box.create_nat_network(adapter_name)
	
	def attach_to_machine(self, machine, slot):
		session = VSession(machine.get_machine())
		adapter = session.get_machine().get_network_adapter(slot)
		adapter.attachment_type = self.adapter_type
		
		if self.adapter_type == NetworkAttachmentType.host_only:
			adapter.host_only_interface = self.adapter_name
		elif self.adapter_type == NetworkAttachmentType.bridged:
			adapter.bridged_interface = self.adapter_name
		adapter.enabled = True
		self.adapter = adapter

		session.close()

	def get_adapter(self):		
		return self.adapter
