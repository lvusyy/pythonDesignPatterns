class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.cpu = None
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = ('Cpu: {}'.format(self.cpu),
                'Memroy: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu))

        return '\n'.join(info)


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('HASU2331212')

    def configure_cpu(self, cpu_model):
        self.computer.cpu = cpu_model

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, cpu, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in (
            self.builder.configure_cpu(cpu), self.builder.configure_memory(memory), self.builder.configure_hdd(hdd),
            self.builder.configure_gpu(gpu))]

    @property
    def computer(self):
        return self.builder.computer


def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(cpu="AMD Ryzen 1800X", hdd=1024, memory=16, gpu="GTX1050Ti 4GB")
    computer = engineer.computer
    print(computer)


if __name__ == '__main__':
    main()
