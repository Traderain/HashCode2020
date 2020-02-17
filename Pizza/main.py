

def main():
    lines = []
    with open('./Pizza/a_example.in') as f:
        lines = f.readlines()

    split0 = lines[0].split(' ')
    max = split0[0]
    typelimit = split0[1]

    pizzatypes = lines[1].split(' ')
    
    # Driver program to test above function 
    val = [60, 100, 120] 
    wt = [10, 20, 30] 
    W = 50
    n = len(val) 
    print(knapSack(W, wt, val, n)) 

    


# A Dynamic Programming based Python  
# Program for 0-1 Knapsack problem 
# Returns the maximum value that can  
# be put in a knapsack of capacity W 
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = (0, list())
            elif wt[i-1] <= w: 
                if val[i-1] + K[i-1][w-wt[i-1]] > K[i-1][w]:
                    K[i][w][1].append(val[i-1] + K[i-1][w-wt[i-1]])
                    K[i][w] = (val[i-1] + K[i-1][w-wt[i-1]], K[i][w][1])
                else:
                    K[i][w][1].append(K[i-1][w])
                    K[i][w] = (K[i-1][w], K[i][w][1])
                #K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w][1].append(K[i-1][w])
                K[i][w] = (K[i-1][w], K[i][w][1]) 
  
    return K[n][W] 

if __name__ == "__main__":
    main()

def formatoutput(pizzas):
    print(len(pizzas) + "\n")
    for i in range(0, len(pizzas)):
        print(i + " ")
    print("\n")

