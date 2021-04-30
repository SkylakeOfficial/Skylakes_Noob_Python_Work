#WDNMD
upper, lower, num = 0, 0, 0
this_is_my_input = input()
for i in range(len(this_is_my_input)):
    if this_is_my_input[i].isupper():
        upper += 1
    if this_is_my_input[i].islower():
        lower += 1
    if this_is_my_input[i].isdigit():
        num += 1
print("{:d}\n{:d}\n{:d}".format(upper, lower, num))