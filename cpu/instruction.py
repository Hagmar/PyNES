def ADC(cpu, addressing_mode, param):
    pass


def AND(cpu, addressing_mode, param):
    operand = addressing_mode.read(cpu, param)
    cpu.register_a &= operand
    cpu.set_status(cpu.ZERO & cpu.NEGATIVE)
