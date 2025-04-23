def macro_expander(code):
    lines = code.strip().split('\n')
    macros = {}
    expanded_code = []

    i = 0
    while i < len(lines):
        if lines[i].startswith("MACRO"):
            name = lines[i + 1].strip()
            body = []
            i += 2
            while lines[i] != "MEND":
                body.append(lines[i])
                i += 1
            macros[name] = body
        else:
            if lines[i].strip() in macros:
                expanded_code.extend(macros[lines[i].strip()])
            else:
                expanded_code.append(lines[i])
        i += 1

    print("Expanded Code:")
    for line in expanded_code:
        print(line)

# Sample macro code
code = """\
MACRO
DISPLAY
PRINT Hello
MEND
START
DISPLAY
STOP
"""

macro_expander(code)
