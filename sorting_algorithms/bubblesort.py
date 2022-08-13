def bubble_sort(numbers):
    for x in range(len(numbers)-1):
        for y in range(len(numbers)-x-1):
            if numbers[x] > numbers[y+x+1]:
                temp = numbers[y+x+1]
                numbers[y+x+1] = numbers[x]
                numbers[x] = temp
    return numbers
                
