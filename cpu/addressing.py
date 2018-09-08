class ABSOLUTE:
    def read(cpu, param):
        return cpu.memory[param]


class ABSOLUTE_X:
    def read(cpu, param):
        return cpu.memory[(param + cpu.x) & 0xFFFF]


class ABSOLUTE_Y:
    def read(cpu, param):
        return cpu.memory[(param + cpu.y) & 0xFFFF]


class IMMEDIATE:
    def read(cpu, param):
        return param


class IMPLICIT:
    def read(cpu, param):
        return 0
