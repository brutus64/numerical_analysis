import numpy as np


#Preprocess data so its all in array format
def preprocess_data(tesla_stocks):
    sess, value = [], []
    for stock in tesla_stocks:
        sess.append(stock['trade_sess'])
        value.append(stock['value'])
    return sess, value

#O(n^2) operation as it requires finding each L_1 which takes O(n) time but there are n amounts of L's so its n*n = n^2
def lagrange_interpolate(tesla_stocks, t):
    sess, value = preprocess_data(tesla_stocks)
    res = 0
    #Loop to find each L_1, L_2, etc.
    for i in range(len(sess)):
        L = value[i]
        #Loop through to get all (x-x2)(x-x3)/(x1-x2)(x1-x3)... for L_1 and all other L's
        for j in range(len(sess)):
            if i != j:
                L *= t-sess[j]
                L /= sess[i]-sess[j]
        print(f"L_{i} value: {L}")
        res += L
    return res

#O(n) time complexity, the biggest time complexity operation here is O(n), solving Ax=b will always be a 3x3 matrix, the matrix multiplication at most is doing 3*n operations so generalized to O(n)
def quad_fit(tesla_stocks, t):
    sess, value = preprocess_data(tesla_stocks)
    res = 0
    #define both A and b
    b = np.array([val for val in value]) #y values
    A = np.array([[1, t, t**2] for t in sess])#mimics A to have c1+c2x+c3x^2 for however many t variables there are
    A_t = A.transpose() #get A transposed
    left_side = np.matmul(A_t,A) #mimics A^T * A
    right_side = np.matmul(A_t,b) #mimics A^T * b
    print("A^T * A: \n", left_side)
    print("A^T * B: \n", right_side)
    c_values = np.linalg.solve(left_side,right_side) #solves Ax=b
    print(f"c0: {c_values[0]}, c1: {c_values[1]}, c2: {c_values[2]}")
    for i in range(len(c_values)): #plug in our t for our quadratic formula
        res += c_values[i] * t ** i
    return res
    
if __name__ == '__main__':
    tesla_stocks = [
        {
            'date': 'Jan 23',
            'trade_sess': 1,
            'value': 412
        },
        {
            'date': 'Jan 24',
            'trade_sess': 2,
            'value': 407
        },
        {
            'date': 'Jan 27',
            'trade_sess': 3,
            'value': 397
        }, 
        {
            'date': 'Jan 28',
            'trade_sess': 4,
            'value': 398
        },
        {
            'date': 'Jan 29',
            'trade_sess': 5,
            'value': 417
        }
    ]
    print(f"Polynomial interpolation (used lagrange method): {lagrange_interpolate(tesla_stocks, 6)}")
    print(f"Quadratic fit: {quad_fit(tesla_stocks, 6)}")