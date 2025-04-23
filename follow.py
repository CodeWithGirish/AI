from collections import defaultdict

productions = {
    "S": ["AB"],
    "A": ["a", "ε"],
    "B": ["b"]
}

first = {
    "S": {"a", "b", "ε"},
    "A": {"a", "ε"},
    "B": {"b"}
}

def compute_follow(productions, start_symbol):
    follow = defaultdict(set)
    follow[start_symbol].add("$")

    updated = True
    while updated:
        updated = False
        for head, bodies in productions.items():
            for body in bodies:
                for i in range(len(body)):
                    symbol = body[i]
                    if symbol.isupper():
                        if i + 1 < len(body):
                            next_symbol = body[i+1]
                            follow_set = first[next_symbol] - {"ε"}
                            if not follow_set.issubset(follow[symbol]):
                                follow[symbol].update(follow_set)
                                updated = True
                        else:
                            if not follow[head].issubset(follow[symbol]):
                                follow[symbol].update(follow[head])
                                updated = True
    return dict(follow)

follow = compute_follow(productions, "S")
print("FOLLOW sets:")
for nt in follow:
    print(f"{nt} : {follow[nt]}")
