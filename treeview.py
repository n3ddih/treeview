#!/usr/bin/python3
import argparse

# Define a function to create a nested dictionary from a list of paths
def create_tree(paths) -> dict:
    tree = {}
    for path in paths:
        parts = path.split("/")
        parts.pop(0)
        node = tree
        for part in parts:
            # If the part is not in the node, create a new dictionary for it
            if part not in node:
                node[part] = {}
            node = node[part]
    return tree

# A function to print the tree view from a nested dictionary
def print_tree(tree, indent=0) -> None:
    for key, value in tree.items():
        print("|   " * indent + "|-- " + key)
        if value:
            print_tree(value, indent + 1)

def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("file", type=str, help="File contains a list of path")

    args = parser.parse_args()
    file_name = args.file

    with open(file_name, "r") as file:
        paths = [line.strip() if line.startswith('/') else '/' + line.strip() for line in file.readlines()]
        tree = create_tree(paths)
        print_tree(tree)

if __name__ == "__main__":
    main()