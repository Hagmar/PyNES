def ADC(cpu, addressing_mode):
    pass


def AND(cpu, addressing_mode):
    operand = addressing_mode.read(cpu)
    cpu.register_a &= operand
    cpu.set_status(cpu.ZERO & cpu.NEGATIVE)
