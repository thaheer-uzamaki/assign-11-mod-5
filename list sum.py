def sum_list(things):
    sum_numbers = 0
    for t in things:
        sum_numbers += t
    return sum_numbers
lst=list()
p = int(input(" number of items in list: - "))
for i in range(p):
    lst.append(int(input()))
print(sum_list(lst))