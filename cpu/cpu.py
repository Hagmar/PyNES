import logging


class CPU:
    def __init__(self):
        register_pc = 0
        register_sp = 0xFD
        register_p = 0x34
        register_a = 0
        register_x = 0
        register_y = 0

        memory = [0] * 0xffff

    def p_carry(self):
        return self.register_p & 0x01

    def p_zero(self):
        return self.register_p & 0x02

    def p_interript_disable(self):
        return self.register_p & 0x04

    def p_decimal(self):
        return self.register_p & 0x08

    def p_overflow(self):
        return self.register_p & 0x40

    def p_negative(self):
        return self.register_p & 0x80

    class Instruction:
        def __init__(self, function):
            self.function = function

        def __call__(self):
            pass
