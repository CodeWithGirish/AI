from collections import defaultdict

def compute_first(productions):
    first = defaultdict(set)

    def first_of(symbol):
        if symbol.islower() or symbol == 'ε':
            return {symbol}
        if symbol in first and first[symbol]:
            return first[symbol]
        for production in productions[symbol]:
            for char in production:
                result = first_of(char)
                first[symbol].update(result - {'ε'})
                if 'ε' not in result:
                    break
            else:
                first[symbol].add('ε')
        return first[symbol]

    for non_terminal in productions:
        first_of(non_terminal)

    return dict(first)

productions = {
    "S": ["AB"],
    "A": ["a", "ε"],
    "B": ["b"]
}

first = compute_first(productions)
print("FIRST sets:")
for nt in first:
    print(f"{nt} : {first[nt]}")
