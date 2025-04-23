def pass1(assembly_code):
    symtab = {}
    locctr = 0
    lines = assembly_code.strip().split("\n")
    pooltab = []
    lit_table = []
    literal_index = 0

    print("Intermediate Code:")
    for line in lines:
        parts = line.strip().split(maxsplit=3)

        if len(parts) == 4:
            label, opcode, reg, operand = parts
        elif len(parts) == 3:
            label = "-"
            opcode, reg, operand = parts
        elif len(parts) == 2:
            label = "-"
            opcode, reg = parts
            operand = "-"
        elif len(parts) == 1:
            label = "-"
            opcode = parts[0]
            reg = operand = "-"
        else:
            continue

        # Handle START
        if opcode == "START":
            locctr = int(reg)
            print(f"{locctr}\t{label}\t{opcode}\t{reg}\t{operand}")
            continue

        # Handle labels
        if label != "-":
            symtab[label] = locctr

        # Handle literals
        if operand.startswith("='") or operand.startswith("='"):
            if operand not in lit_table:
                lit_table.append(operand)

        # Handle LTORG
        if opcode == "LTORG":
            for lit in lit_table[literal_index:]:
                print(f"{locctr}\t*\tDC\t{lit}\t-")
                literal_index += 1
                locctr += 3
            continue

        # Handle DS (define storage)
        if opcode == "DS":
            symtab[label] = locctr
            locctr += 3 * int(reg)
            print(f"{locctr-3}\t{label}\t{opcode}\t{reg}\t{operand}")
            continue

        # Handle END
        if opcode == "END":
            # Allocate remaining literals
            for lit in lit_table[literal_index:]:
                print(f"{locctr}\t*\tDC\t{lit}\t-")
                literal_index += 1
                locctr += 3
            print(f"{locctr}\t{label}\t{opcode}\t{reg}\t{operand}")
            break

        print(f"{locctr}\t{label}\t{opcode}\t{reg}\t{operand}")
        locctr += 3

    print("\nSymbol Table:")
    for symbol in symtab:
        print(symbol, "=>", symtab[symbol])

    print("\nLiteral Table:")
    for idx, lit in enumerate(lit_table):
        print(f"{idx+1}\t{lit}")

# Sample Input
code = """\
JOHN    START   200
        MOVER   R1 ='3'
        MOVEM   R1 x
L1      MOVER   R2 ='2'
        LTORG
X       DS      1
        END
"""

pass1(code)
