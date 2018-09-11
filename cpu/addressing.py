class ABSOLUTE:
    def read(cpu, param):
        return cpu.memory.read(param)

    def write(cpu, param, value):
        cpu.memory.write(param, value)


class ABSOLUTE_X:
    def read(cpu, param):
        return cpu.memory.read((param + cpu.x) & 0xFFFF)

    def write(cpu, param, value):
        cpu.memory.write((param + cpu.y) & 0xFFFF, value)


class ABSOLUTE_Y:
    def read(cpu, param):
        return cpu.memory.read((param + cpu.y) & 0xFFFF)

    def write(cpu, param, value):
        cpu.memory.write((param + cpu.y) & 0xFFFF, value)


class ACCUMULATOR:
    def read(cpu, _):
        return cpu.a

    def write(cpu, _, value):
        cpu.a = value


class IMMEDIATE:
    def read(cpu, param):
        return param


class IMPLICIT:
    def read(cpu, param):
        return 0


class ZERO_PAGE:
    def read(cpu, param):
        return cpu.memory.read(param)

    def write(cpu, param, value):
        cpu.memory.write(param, value)


class ZERO_PAGE_X:
    def read(cpu, param):
        return cpu.memory.read((param + cpu.x) & 0xFF)

    def write(cpu, param, value):
        cpu.memory.write((param + cpu.x) & 0xFF, value)


class ZERO_PAGE_Y:
    def read(cpu, param):
        return cpu.memory.read((param + cpu.y) & 0xFF)

    def write(cpu, param, value):
        cpu.memory.write((param + cpu.y) & 0xFF, value)
