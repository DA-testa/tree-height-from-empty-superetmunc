import sys
import threading
import re
from array import *
import numpy as np
import os

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
    command=input("Enter input type (I for keyboard, F for file): ")
    parents=array('i')
    if 'I' in command:
        n=int(input())
        parent=input()
        a=re.split(' ',parent)
        for x in a: 
             parents.append(int(x))

    if 'F' in command:
        file=input("Enter filename: ")
        name="test/"+file
        if 'a' in file:
            print("wrong file name")
        elif os.path.isfile(name):
            with open(name,"r") as file:
                n=int(file.readline())
                lines=file.readlines()
                nodes=lines[1:]
                for nodes in lines:
                    a=re.split(' ',nodes)
                    for x in a:
                        parents.append(int(x))
        else:
            print(f"Error: File {file} not found in test folder")
            return

    tree, root = build_tree(n, parents)
    height = compute_height(tree, root)
    print(height)

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
