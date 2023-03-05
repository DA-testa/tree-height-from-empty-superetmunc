##221RDC037
##RDCM0 Finanšu inženierija
##18.grupa

import sys
import threading


def compute_height(n, parents): 
    nodes = [[] for _ in range(n)]

    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            nodes[parents[i]].append(i)
    def height(node):
        if not nodes[node]:
            return 1
        else:
            return 1 + max(height(child) for child in nodes[node])
    return height(root)


def main():
    
    filename = input("Enter filename (or press Enter for keyboard input): ")

    if filename and 'a' not in filename:
        try:
            with open(filename) as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
        except FileNotFoundError:
            print(f"Error: File {filename} not found")
            return
    else:
        n = int(input())
        parents = list(map(int, input().split()))

    
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7) 
threading.stack_size(2**27)   
threading.Thread(target=main).start()
