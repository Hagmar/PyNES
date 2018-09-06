from cpu import addressing as addr
from cpu import instruction as instr
import logging


class CPU:
    class Instruction:
        def __init__(self, function, addressing, param_bytes, cycles):
            self.function = function
            self.addressing = addressing
            self.param_bytes = param_bytes
            self.cycles = cycles

        def __call__(self, cpu):
            self.function(
                    cpu,
                    addressing,
                    cpu.memory[cpu.pc+1:cpu.pc+1+self.param_bytes])

    def __init__(self):
        self.log = logging.getLogger('PyNES')

        self.CARRY = 0x01
        self.ZERO = 0x02
        self.NEGATIVE = 0x80

        self.pc = 0
        self.sp = 0xFD
        self.p = 0x34
        self.a = 0
        self.x = 0
        self.y = 0

        self.memory = [0] * 0xffff

        self.opcodes = {
                0x29: self.Instruction(instr.AND, addr.IMMEDIATE, 1, 2),
        }

    def p_carry(self):
        return self.p & self.CARRY

    def p_zero(self):
        return self.p & self.ZERO

    def p_interript_disable(self):
        return self.p & 0x04

    def p_decimal(self):
        return self.p & 0x08

    def p_overflow(self):
        return self.p & 0x40

    def p_negative(self):
        return self.p & self.NEGATIVE

    def set_status(self, bits):
        if bits & self.ZERO:
            set_bit(self.ZERO, self.a == 0)
        if bits & self.NEGATIVE:
            set_bit(self.NEGATIVE, self.a & 0x80 == 0x80)

    def set_bit(self, bit, cond):
        if cond:
            self.p |= bit
        else:
            self.p &= ~bit
