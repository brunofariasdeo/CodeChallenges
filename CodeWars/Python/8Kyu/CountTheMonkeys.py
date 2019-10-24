def monkey_count(n):

    monkeys = [1]
    
    if n == 1:
        return monkeys
    else: 
        count = 1 
        while len(monkeys) < n:
            print(count)
            count+=1
            monkeys.append(count)

        return monkeys

print(monkey_count(10))