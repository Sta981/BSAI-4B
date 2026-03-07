instructions = """
0. Exit
1. Fill X completely
2. Fill Y completely
3. Empty X completely
4. Empty Y completely
5. Pour X into Y until X is empty
6. Pour X into Y until Y is full
7. Pour Y into X until Y is empty
8. Pour Y into X until X is full
"""
print(instructions)
x = 0
y = 0
g = 2
x_cap = 4
y_cap = 5
while True:
    rule = int(input("Enter your Rule(1-8):"))
    if rule == 1:
        x = x_cap
        print(f"x = {x}L , y = {y}L ")
    if rule == 2:
        y = y_cap
        print(f"x = {x}L , y = {y}L ")
    if rule == 3:     
        x = 0
        print(f"x = {x}L , y = {y}L ")
    if rule == 4:
        y = 0
        print(f"x = {x}L , y = {y}L ")
    if rule == 5:
        space = y_cap - y
        if x <= space:
            y = y + x
            x = 0
        else:
            x = x - space
            y = y_cap
        print(f"x = {x}L , y = {y}L ")

    if rule == 6:
        space = y_cap - y
        if x >= space:
            x = x - space
            y = y_cap
        else:
            y = y + x
            x = 0
        print(f"x = {x}L , y = {y}L ")
    if rule == 7:
        space = x_cap - x
        if y <= space:
            x = x + y
            y = 0
        else:
            y = y - space
            x = x_cap
    print(f"x = {x}L , y = {y}L ")
    if rule == 8:
        space = x_cap - x
        if y >= space:
            y = y - space
            x = x_cap
        else:
            x = x + y
            y = 0
        print(f"x = {x}L , y = {y}L ")

    if x == g or y ==g:
        print("Reached the goal.")
        break



