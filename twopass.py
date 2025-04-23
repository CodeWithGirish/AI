def pass1(assembly_code):
    symtab = {}
    locctr = 0
    lines = assembly_code.strip().split("\n")
    
    print("Intermediate Code:")
    for line in lines:
        parts = line.strip().split()

        # Handle missing label
        if len(parts) == 4:
            label, opcode, reg, operand = parts
        elif len(parts) == 3:
            label = "-"
            opcode, reg, operand = parts
        elif len(parts) == 2:
            label = "-"
            opcode, reg = parts
            operand = "-"
        else:
            continue  # Skip invalid line
        
        if label != "-":
            symtab[label] = locctr
        print(f"{locctr}\t{label}\t{opcode}\t{reg}\t{operand}")
        locctr += 3

    print("\nSymbol Table:")
    for symbol in symtab:
        print(symbol, "=>", symtab[symbol])

# Sample input
code = """\
LOOP    MOVER   AREG    ONE
        ADD     AREG    TWO
        STOP
ONE     DC      1
TWO     DC      2
"""

pass1(code)
