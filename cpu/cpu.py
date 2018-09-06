import logging


class CPU:
    class Instruction:
        def __init__(self, function):
            self.function = function

        def __call__(self):
            pass

    def __init__(self):
        self.log = logging.getLogger('PyNES')

        self.ZERO = 0x02
        self.NEGATIVE = 0x80

        self.register_pc = 0
        self.register_sp = 0xFD
        self.register_p = 0x34
        self.register_a = 0
        self.register_x = 0
        self.register_y = 0

        self.memory = [0] * 0xffff

        self.opcodes = {
        }

    def p_carry(self):
        return self.register_p & 0x01

    def p_zero(self):
        return self.register_p & self.ZERO

    def p_interript_disable(self):
        return self.register_p & 0x04

    def p_decimal(self):
        return self.register_p & 0x08

    def p_overflow(self):
        return self.register_p & 0x40

    def p_negative(self):
        return self.register_p & self.NEGATIVE

    def set_status(self, bits):
        if bits & self.ZERO:
            set_bit(self.ZERO, self.register_a == 0)
        if bits & self.NEGATIVE:
            set_bit(self.NEGATIVE, self.register_a & 0x80 == 0x80)

    def set_bit(self, bit, cond):
        if cond:
            self.register_p |= bit
        else:
            self.register_p &= ~bit
