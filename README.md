# Tree View

## Current problems

Tree command is a very useful command. It shows the current or target directory and its child in tree format.

However, tree does not provide tree when given a list of file paths. This can be useful when you want to visualize a list of files, or the output of `find` command.

## Ideas

- Write a program in Python.
    - Consider using Go for optimization. Given longer files (>10000 files)
- View tree format from a list of paths. For examples:
    - Output of `find` command
    - A list of API's path
- Command in format: `treeview paths.txt`

## Example input file

> Generated from `find` command

```
test/
test/folder1
test/folder1/abc.txt
test/folder1/child1
test/folder1/test1.txt
test/folder2
test/folder2/abc.txt
test/folder2/run.sh
test/folder2/test.txt
test/folder2/test2.txt
test/test.txt
```

## Example output

```bash
$ ./treeview.py paths.txt
|-- test
|   |--
|   |-- folder1
|   |   |-- abc.txt
|   |   |-- child1
|   |   |-- test1.txt
|   |-- folder2
|   |   |-- abc.txt
|   |   |-- run.sh
|   |   |-- test.txt
|   |   |-- test2.txt
|   |-- test.txt
```

