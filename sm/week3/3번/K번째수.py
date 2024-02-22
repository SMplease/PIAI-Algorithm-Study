def solution(array, commands):
    ary3 = []

    for ary in commands:
        ary2 = []
        ## ary[0]=2, ary[1]=5, ary[2]=3
        for j in range(ary[0],ary[1]+1):
            ary2.append(array[j-1])
        ary2.sort()
        print(ary2)
        ary3.append(ary2[ary[2]-1])
    
    return ary3
