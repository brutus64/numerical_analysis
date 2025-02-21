import numpy as np

def preprocess_data(tesla_stocks):
    sess, value = [], []
    for stock in tesla_stocks:
        sess.append(stock['trade_sess'])
        value.append(stock['value'])
    return sess, value
def lagrange_interpolate(tesla_stocks, t):
    sess, value = preprocess_data(tesla_stocks)
    res = 0
    for i in range(len(sess)):
        L = value[i]
        for j in range(len(sess)):
            if i != j: #order of multiplication or division doesnt matter
                L *= t-sess[j]
                L /= sess[i]-sess[j]
        res += L
    return res

def quad_fit(tesla_stocks, t):
    sess, value = preprocess_data(tesla_stocks)
    res = 0
    b = np.array([val for val in value])
    A = np.array([[1, t, t**2] for t in sess])#mimics A to have c1+c2x+c3x^2 for however many t variables there are
    A_t = A.transpose()
    left_side = np.matmul(A_t,A) #mimics A^T * A
    right_side = np.matmul(A_t,b) #mimics A^T * b
    print(left_side)
    print(right_side)
    c_values = np.linalg.solve(left_side,right_side)
    print(c_values)
    for i in range(len(c_values)):
        res += c_values[i] * t ** i
    print(res)
    
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
    print(lagrange_interpolate(tesla_stocks, 6))
    quad_fit(tesla_stocks, 6)