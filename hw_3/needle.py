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
                    mapping[1] += 1
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
    plot_results(results, n)
    
def plot_results(results, n):
    diameters = sorted(results.keys())
    data = {
        1: [],
        2: [],
        3: [],
        4: []
    }
    for d in diameters:
        values = results[d]
        print(d, values)
        for i in range(1, 5): #can cross at least 1 to 4 lines
            count = values.get(i, 0)
            prob = float(count) / float(n)
            data[i].append(prob)
            
    print(data)
    plt.figure(figsize=(12, 8))
    colors = ['blue', 'green', 'red', 'purple']
    labels = ['1 line', '2 lines', '3 lines', '4 lines']
    for i, lines in enumerate(range(1, 5)):
        plt.plot(diameters, data[lines], 'o-', color=colors[i], linewidth=2, markersize=8, label=labels[i])
    plt.xlabel("diameter")
    plt.ylabel("probability")
    plt.title("# of at least lines v.s diameter size")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    
             
        
    
if __name__ == '__main__':
    needle(4444444, 1)