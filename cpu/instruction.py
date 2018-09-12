def signed(value):
    return value - 0xFF if value > 0x7F else value


def ADC(cpu, addressing_mode, param):
    operand = addressing_mode.read(cpu, param)
    cpu.a += operand
    cpu.set_bit(cpu.CARRY, cpu.a > 0xFF or cpu.a < 0)
    cpu.a &= 0xFF
    cpu.set_bit(cpu.OVERFLOW, cpu.a > 0x7F or cpu.a < -0x80)
    cpu.set_status(cpu.ZERO & cpu.NEGATIVE, cpu.a)


def AND(cpu, addressing_mode, param):
    operand = addressing_mode.read(cpu, param)
    cpu.a &= operand
    cpu.set_status(cpu.ZERO & cpu.NEGATIVE, cpu.a)


def ASL(cpu, addressing_mode, param):
    value = addressing_mode.read(cpu, param)
    cpu.set_bit(cpu.CARRY, value & 0x80)
    value = (value << 1) & 0xFF
    addressing_mode.write(cpu, param)


def BCC(cpu, addressing_mode, param):
    if not cpu.carry():
        branch(cpu, param)


def BCS(cpu, addressing_mode, param):
    if cpu.carry():
        branch(cpu, param)


def BEQ(cpu, addressing_mode, param):
    if cpu.zero():
        branch(cpu, param)


def BMI(cpu, addressing_mode, param):
    if cpu.negative():
        branch(cpu, param)


def BNE(cpu, addressing_mode, param):
    if not cpu.zero():
        branch(cpu, param)


def BPL(cpu, addressing_mode, param):
    if not cpu.negative():
        branch(cpu, param)


def BVC(cpu, addressing_mode, param):
    if not cpu.overflow():
        branch(cpu, param)


def BVS(cpu, addressing_mode, param):
    if cpu.overflow():
        branch(cpu, param)


def CLC(cpu, addressing_mode, param):
    cpu.set_bit(cpu.CARRY, 0)


def CLD(cpu, addressing_mode, param):
    cpu.set_bit(cpu.DECIMAL, 0)


def CLI(cpu, addressing_mode, param):
    cpu.set_bit(cpu.INTERRUPT, 0)


def CLV(cpu, addressing_mode, param):
    cpu.set_bit(cpu.OVERFLOW, 0)


def DEX(cpu, addressing_mode, param):
    cpu.x -= 1
    cpu.x &= 0xFF
    cpu.set_status(cpu.ZERO & cpu.NEGATIVE, cpu.x)


def DEY(cpu, addressing_mode, param):
    cpu.y -= 1
    cpu.set_bit(cpu.NEGATIVE, cpu.y & cpu.NEGATIVE)
    cpu.y &= 0xFF
    cpu.set_bit(cpu.ZERO, cpu.y == 0)


def INX(cpu, addressing_mode, param):
    cpu.x = (cpu.x + 1) & 0xFF
    cpu.set_status(cpu.ZERO & cpu.NEGATIVE, cpu.x)


def INY(cpu, addressing_mode, param):
    cpu.y = (cpu.y + 1) & 0xFF
    cpu.set_status(cpu.ZERO & cpu.NEGATIVE, cpu.y)


def branch(cpu, relative_addr):
    cpu.pc = (cpu.pc + signed(relative_addr)) & 0xFFFF
