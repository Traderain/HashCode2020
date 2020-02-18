

def main():
    lines = []

    fp = './Pizza/a_example'


    with open(fp + '.in') as f:
        lines = f.readlines()

    split0 = lines[0].split(' ')
    max = split0[0]
    typelimit = split0[1]

    pizzatypes = lines[1].strip().split(' ')


    
    # Driver program to test above function 
    val = [] 
    wt = []
    for idx in range(0, len(pizzatypes)):
        val.append(int(pizzatypes[idx]))
        wt.append(int(pizzatypes[idx]))
    W = int(max)
    n = len(val) 
    ret = knapSack(W, wt, val, n)
    with open(fp + '.out', 'w') as fo:
        fo.write(str(len(ret)) + "\n")
        for i in range(0, len(ret)):
            for j in range(0, len(pizzatypes)):
                if pizzatypes[j] == ret[i]:
                    fo.write(str(j) + " ")

        fo.write("\n")

    


# A Dynamic Programming based Python  
# Program for 0-1 Knapsack problem 
# Returns the maximum value that can  
# be put in a knapsack of capacity W 
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 

    asd = [[list() for x in range(W + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                if val[i-1] + K[i-1][w-wt[i-1]] >= K[i-1][w]:
                    asd[i][w].append(K[i-1][w-wt[i-1]])
                    asd[i][w].append(val[i-1])
                    K[i][w] = val[i-1] + K[i-1][w-wt[i-1]]
                else:
                    #K[i-1][w][1].append(K[i-1][w][0])
                    for item in asd[i-1][w]:
                        asd[i][w].append(item)
                    K[i][w] = K[i-1][w]
                #K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                #K[i-1][w][1].append(K[i-1][w][0])
                for item in asd[i-1][w]:
                    asd[i][w].append(item)
                K[i][w] = K[i-1][w] 
  
    lower = len(asd)
    upper = len(asd[0])
    return asd[lower-1][upper-1]

if __name__ == "__main__":
    main()

