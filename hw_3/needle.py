import random
from collections import defaultdict
import matplotlib.pyplot as plt
def needle(n, w):
    results = {}
    diameters = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.5, 2.0, 3.0]
    for d in diameters:
        #each line is at a whole number so it's 0,1,etc.
        mapping = defaultdict(int)
        for _ in range(n):
            y_point = random.uniform(0,1)
            if d < w:
                if y_point + d/2 >= 1 or y_point - d/2 <= 0:
                    mapping['1'] += 1
            else:
                #diameter goes as high as 3, so at best, it can touch -1.5 and 2.5 from a random number 0 to 1
                possible_lines = [-1, 0, 1, 2]
                lines_crossed = 0
                for line in possible_lines:
                    if abs(y_point - line) <= d/2:
                        lines_crossed += 1
                for i in range(1, lines_crossed+1):
                    mapping[i] += 1
                # print(f"AT this diameter {d} we crossed {lines_crossed}, from {y_point}")
        results[d] = mapping
    for key, value in results.items():
        print("diameter", key)
        print("table", value)
    # plot_results(diameters, results, n)    
# def plot_results(d, results, n):
#     data = {
#         0: [],
#         1: [],
#         2: [],
#         3: [],
#         4: []
#     }
#     for val in d:
#         crossings = results[d]
#         for x in range(5):
#             count = sum(crossings[k] for k in crossings if k >= x)
#             prob = count/n
#             data[x].append(prob)
#     fig, ax = plt.subplots(figsize=(12,8))
#     colors = ['red']
#     for line_count in ['0','1','2','3']:
#         if line_count in p:
             
        
    
if __name__ == '__main__':
    needle(4444444, 1)