def second_largest(list):
    first = list[0]
    second = list[1]
    
    if first > second :
        first , second = second , first
        
    for num in list[2:]:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return first , second
    