# Q what is the difference between continue , break, and pass ?
# continue -> skip at that specific value 
# pass -> do nothing 
# break -> stop the loop/condition


for i in range(11):
    i+=1
    if i==5:
        continue
    if i == 1:
        pass
    if i == 9:
        break
    print(i)
