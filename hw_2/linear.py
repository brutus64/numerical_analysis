import numpy as np
import random
def linear(n):
    #Set up A matrix NxN uniform random -1,1
    A = []
    for _ in range(n):
        subarr = []
        for _ in range(n):
            subarr.append(random.uniform(-1,1)) #randomly uniform value from -1 to 1 for NxN
        A.append(subarr)
    A = np.array(A)
    #Sets up b vector with just 1's 
    b = np.ones(n)
    print("Original values:")
    print("A:\n", A)
    print("b:\n", b)
    
    #Guassian elimination
    for i in range(n): #Grabbing "ith" element in "ith" array, so every array below needs 0 for "ith" element        
        for j in range(i+1,n): #every array below array i
            factor = A[j][i]/A[i][i] #element i at array j, and element i at array i (to know what the factor is for subtraction)
            A[j] -= A[i] * factor #ith element in row j subtract to 0
            b[j] -= b[i] * factor #scalar subtract 
    print("Post-Guassian Elimination:")
    print("A:\n", A)
    print("b:\n", b)
    #Backward substitution
    results = [0] * n
    
    for i in range(n-1, -1, -1): #starting from last array, back up
        b_val = b[i] #value of b
        for j in range(n-1,i,-1):#start high to i, continuous substitution and subtraction
            b_val -= results[j] * A[i][j]
        results[i] = b_val/A[i][i] #at the end, just divide remaining b value by it's i element

    for i in range(len(results)):
        print(f"x{i}:", results[i])

if __name__ == '__main__':
    linear(66)