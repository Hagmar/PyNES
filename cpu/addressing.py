class ABSOLUTE:
    def read(cpu, param):
        return cpu.memory[param]

    def write(cpu, param, value):
        cpu.memory[param] = value


class ABSOLUTE_X:
    def read(cpu, param):
        return cpu.memory[(param + cpu.x) & 0xFFFF]

    def write(cpu, param, value):
        cpu.memory[(param + cpu.y) & 0xFFFF] = value


class ABSOLUTE_Y:
    def read(cpu, param):
        return cpu.memory[(param + cpu.y) & 0xFFFF]

    def write(cpu, param, value):
        cpu.memory[(param + cpu.y) & 0xFFFF] = value


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
