
ops = {"write": "w", "read": "r", "execute": "x"}
perm = {}

n = int(input());

for _ in range(n):
    parts = input().split();
    name = parts[0];
    if len(parts) > 1:
        perm[name] = parts[1:]
    else:
        perm[name] = []

m = int(input())
for _ in range(m):
    op, name = input().split()
    n = ops[op]
    allowed = perm.get(name)
    if n in allowed:
        print("\nOK")
    else:
        print("\nAccess denied")