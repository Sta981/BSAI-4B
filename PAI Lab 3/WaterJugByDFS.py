start = (0,0)
g = 2
x_cap = 4
y_cap = 5
visited = set()
stack = [(start,[])]

def rule1(x,y):
    x = x_cap
    return (x,y)    
def rule2(x,y):
    y= y_cap
    return (x,y)
def rule3(x,y):
    x = 0
    return (x,y)
def rule4(x,y):
    y = 0
    return (x,y)
def rule5(x,y):
    total = x + y
    if total <= y_cap:
        return (0, total)
    else:
        return (total - y_cap, y_cap) 
def rule6(x,y):
    total = x + y
    if total <= y_cap:
        return (0,total)
    else:
        return(total-y_cap,y_cap)
def rule7(x,y):
    total = x + y
    if total <= x_cap:
        return (total, 0)
    else:
        return (x_cap,total - x_cap)
def rule8(x,y):
    total = x + y
    if total <= x_cap:
        return (total,0)
    else:
        return(x_cap,total-x_cap)

while stack:
    current_state,path = stack.pop()
    x,y=current_state
    if x == g or y == g:
        print(f"Found the Goal: {path}")
        print(f"Final state: X={x}L, Y={y}L")
        break
    if current_state in visited:
        continue
    visited.add(current_state)

    rules = [rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8]
    for rule_num , rule_func in enumerate(rules,1):
        new_x ,new_y =  rule_func(current_state[0],current_state[1])
        new_state = (new_x,new_y)
        if new_state not in visited:
            stack.append((new_state,path + [rule_num]))





