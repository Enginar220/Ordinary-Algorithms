def linear_search(num,lis):
    i=0
    for x in lis:
        if num == x:
            print(num,"is in the given list.")
            break
        else:
            i += 1
    if i >= len(lis):
        print(num,"is not in the given list.")

linear_search(3,[4,5,6,2])

    