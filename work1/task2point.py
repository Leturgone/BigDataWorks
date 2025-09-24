def task2():
    n = int(input())
    db = set()
    for _ in range(n):
        name = input().strip()
        if name not in db:
            print("OK")
            db.add(name)
        else:
            i = 1
            while True:
                new_name = name + str(i)
                if new_name not in db:
                    print(new_name)
                    db.add(new_name)
                    break
                i += 1


task2()
