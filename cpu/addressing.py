class ABSOLUTE:
    def read(cpu, param):
        return cpu.memory.read(param)

    def write(cpu, param, value):
        cpu.memory.write(param, value)


class ABSOLUTE_X:
    def read(cpu, param):
        return cpu.memory.read(param + cpu.x)

    def write(cpu, param, value):
        cpu.memory.write(param + cpu.x)


class ABSOLUTE_Y:
    def read(cpu, param):
        return cpu.memory.read(param + cpu.y)

    def write(cpu, param, value):
        cpu.memory.write(param + cpu.y)


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


class RELATIVE:
    def read(cpu, param):
        pass

    def write(cpu, param, value):
        pass


class ZERO_PAGE:
    def read(cpu, param):
        return cpu.memory.read(param)

    def write(cpu, param, value):
        cpu.memory.write(param, value)


class ZERO_PAGE_X:
    def read(cpu, param):
        return cpu.memory.read(param + cpu.x)

    def write(cpu, param, value):
        cpu.memory.write(param + cpu.x, value)


class ZERO_PAGE_Y:
    def read(cpu, param):
        return cpu.memory.read(param + cpu.y)

    def write(cpu, param, value):
        cpu.memory.write(param + cpu.y, value)
