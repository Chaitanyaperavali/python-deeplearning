# fun to find triplets with sum = 0
def getTriplet(list):
    # creates an empty list to hold triplets
    zeroTripletList = []
    # iterate over each element, and the next too elements in remaining sublist
    for x in range(0,list.__len__()-2):
        for y in range(x+1,list.__len__()-1):
            for z in range(y+1,list.__len__()):
                sum = list[x]+list[y]+list[z]
                if(sum == 0):
                    # add triplet to the list if sum =0
                    zeroTripletList.append((list[x],list[y],list[z]))

    for w in zeroTripletList:
        print(w)


getTriplet([1,3,-6,4,-1,2,8,-2,9])
