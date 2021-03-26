

class VSession:
	def __init__(self, machine):
		self.session = machine.create_session()

	def get_session(self):		
		return self.session

	def get_machine(self):		
		return self.session.machine

	def close(self, ):
		self.session.machine.save_settings()
		self.session.unlock_machine()
