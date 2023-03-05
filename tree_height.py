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
    input_type = input("Enter input type (I for input, F for file): ")
    
    if input_type == "I":
        n = int(input())
        parents = list(map(int, input().split()))
    elif input_type == "F":
        filename = input("Enter filename: ")
        
        try:
            with open(filename) as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
        except FileNotFoundError:
            print("Error: File not found")
            return
    else:
        print("Error: Invalid input type")
        return
    print(compute_height(n, parents))


sys.setrecursionlimit(10**7)
threading.stack_size(2**27) 
threading.Thread(target=main).start()
