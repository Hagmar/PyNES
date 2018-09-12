from cpu import addressing as addr
from cpu import instruction as instr
import logging


class CPU:
    class Instruction:
        def __init__(self, function, addressing, instr_bytes, cycles):
            self.function = function
            self.addressing = addressing
            self.instr_bytes = instr_bytes
            self.cycles = cycles

        def __call__(self, cpu):
            param = 0
            for i in range(self.instr_bytes - 1):
                param += cpu.memory[cpu.pc + i + 1] << 8 * i

            self.function(cpu, self.addressing, param)

    class Memory:
        def __init__(self):
            self.memory = [0] * 0xFFFF

        def read(self, addr):
            return self.memory[addr]

        def write(self, addr, value):
            self.memory[addr] = value

    def __init__(self):
        self.log = logging.getLogger('PyNES')

        self.CARRY = 0x01
        self.ZERO = 0x02
        self.INTERRUPT = 0x04
        self.DECIMAL = 0x08
        self.OVERFLOW = 0x40
        self.NEGATIVE = 0x80

        self.pc = 0
        self.sp = 0xFD
        self.p = 0x34
        self.a = 0
        self.x = 0
        self.y = 0

        self.memory = self.Memory()

        self.opcodes = {
                0x06: self.Instruction(instr.ASL, addr.ZERO_PAGE, 2, 5),
                0x0A: self.Instruction(instr.ASL, addr.ACCUMULATOR, 1, 2),
                0x0E: self.Instruction(instr.ASL, addr.ABSOLUTE, 3, 6),

                0x16: self.Instruction(instr.ASL, addr.ZERO_PAGE_X, 2, 6),
                0x18: self.Instruction(instr.CLC, addr.IMPLICIT, 1, 2),
                0x1E: self.Instruction(instr.ASL, addr.ABSOLUTE_X, 3, 7),

                0x25: self.Instruction(instr.AND, addr.ZERO_PAGE, 2, 3),
                0x29: self.Instruction(instr.AND, addr.IMMEDIATE, 2, 2),
                0x2D: self.Instruction(instr.AND, addr.ABSOLUTE, 3, 4),

                0x35: self.Instruction(instr.AND, addr.ZERO_PAGE_X, 2, 4),
                0x39: self.Instruction(instr.AND, addr.ABSOLUTE_Y, 3, 4),
                0x3D: self.Instruction(instr.AND, addr.ABSOLUTE_X, 3, 4),

                0x58: self.Instruction(instr.CLI, addr.IMMEDIATE, 1, 2),

                0x65: self.Instruction(instr.ADC, addr.ZERO_PAGE, 2, 3),
                0x69: self.Instruction(instr.ADC, addr.IMMEDIATE, 2, 2),
                0x6D: self.Instruction(instr.ADC, addr.ABSOLUTE, 3, 4),

                0x75: self.Instruction(instr.ADC, addr.ZERO_PAGE_X, 2, 4),
                0x79: self.Instruction(instr.ADC, addr.ABSOLUTE_Y, 3, 4),
                0x7D: self.Instruction(instr.ADC, addr.ABSOLUTE_X, 3, 4),

                0x88: self.Instruction(instr.DEY, addr.IMPLICIT, 1, 2),

                0xB8: self.Instruction(instr.CLV, addr.IMMEDIATE, 1, 2),

                0xCA: self.Instruction(instr.DEX, addr.IMPLICIT, 1, 2),

                0xD8: self.Instruction(instr.CLD, addr.IMPLICIT, 1, 2)
        }

    def carry(self):
        return self.p & self.CARRY

    def zero(self):
        return self.p & self.ZERO

    def interrupt_disable(self):
        return self.p & self.INTERRUPT

    def decimal(self):
        return self.p & self.DECIMAL

    def overflow(self):
        return self.p & self.OVERFLOW

    def negative(self):
        return self.p & self.NEGATIVE

    def set_status(self, bits, value):
        if bits & self.ZERO:
            set_bit(self.ZERO, value)
        if bits & self.NEGATIVE:
            set_bit(self.NEGATIVE, value & self.NEGATIVE)

    def set_bit(self, bit, cond):
        if cond:
            self.p |= bit
        else:
            self.p &= ~bit

    def read_mem(self, addr):
        return self.memory.read(addr)

    def write_mem(self, addr, value):
        self.memory.write(addr, value)
