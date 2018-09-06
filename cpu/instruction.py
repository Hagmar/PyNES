def ADC(cpu, addressing_mode, param):
    operand = addressing_mode.read(cpu, param)
    cpu.a += operand
    cpu.set_bit(cpu.CARRY, cpu.a > 0xff or cpu.a < 0)
    cpu.a &= 0xff
    cpu.set_bit(cpu.OVERFLOW, cpu.a > 0x7f or cpu.a < -0x80)
    cpu.set_status(cpu.ZERO & cpu.NEGATIVE)


def AND(cpu, addressing_mode, param):
    operand = addressing_mode.read(cpu, param)
    cpu.a &= operand
    cpu.set_status(cpu.ZERO & cpu.NEGATIVE)
