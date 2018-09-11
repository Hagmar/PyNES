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
    value = (value <<= 1) & 0xFF
    addressing_mode.write(cpu, param)


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
