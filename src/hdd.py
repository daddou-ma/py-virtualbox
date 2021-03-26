from virtualbox.library import AccessMode, DeviceType, MediumVariant
from session import VSession

class VHardDisk:
    def __init__(self, box, filename, size = 1):
        hd_path = '/home/ubuntu/Desktop/CC/python/' + filename
        hd_size = size * 1024 * 1024 * 1024

        try:
            self.medium = box.open_medium(hd_path, DeviceType.hard_disk, AccessMode.read_write, True)
        except:
            self.medium = VHardDisk.create(box, filename, size)

    @staticmethod
    def create(box, filename, size = 1):
        hd_path = '/home/ubuntu/Desktop/CC/python/' + filename
        hd_size = size * 1024 * 1024 * 1024

        print(filename)

        medium = box.create_medium("VDI", hd_path, AccessMode.read_write, DeviceType.hard_disk)
        progress = medium.create_base_storage(hd_size , [MediumVariant.standard])
        progress.wait_for_completion()

        return box.open_medium(hd_path, DeviceType.hard_disk, AccessMode.read_write, True)

    def attach_to_machine(self, machine):
        session = VSession(machine.get_machine())
        session.get_machine().attach_device("SATA", 0, 0, DeviceType.hard_disk, self.medium)
        session.close()

    def get_medium(self):		
        return self.medium