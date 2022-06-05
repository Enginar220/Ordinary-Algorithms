def linear_search(num,lis) :
    i=0
    for x in lis :
        if num == lis[i] :
            print(num,"is in the list.")
            break
        else :
             i += 1
    if  i >= len(lis) :
        print(num,"is not in the list.")

linear_search(12,[1,2,3,4,5,6,12])
