import os
import sys
import threading


def build_tree(n, parents):
    tree = [[] for _ in range(n)]
    root = None

    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)

    return tree, root


def compute_height(tree, root):
    if not tree[root]:
        return 1
    else:
        heights = [compute_height(tree, child) for child in tree[root]]
        return 1 + max(heights)


def main():
    input_type = input("Enter input type (I for keyboard, F for file): ")
    if input_type == "I":
        n = int(input())
        parents = list(map(int, input().split()))
    elif input_type == "F":
        filename = input("Enter filename: ")
        if filename and 'a' not in filename:
            path = os.path.join(os.getcwd(), 'test', filename)
        try:
            with open(path) as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
        except FileNotFoundError:
            print(f"Error: File {filename} not found in test folder")
            return
    else:
        n = int(input())
        parents = list(map(int, input().split()))

    tree, root = build_tree(n, parents)
    print(compute_height(tree, root))


sys.setrecursionlimit(10**7)
threading.stack_size(2**27) 
threading.Thread(target=main).start()
