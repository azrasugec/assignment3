# 📘 Assignment #3 – Git/GitHub – Stack Implementation using Linked List

This project demonstrates the implementation of a stack data structure using a linked list in Python. Each task incrementally builds upon the previous one, starting from repository setup to final data manipulation and output generation using external files. The project also integrates fundamental Git operations such as branching, committing, and merging via GitHub.

---

## ✅ Task 1 – Initialize Repository & Create README

We created a new GitHub repository named `assignment3`, cloned it locally, and initialized a `README.md` file to document our process.

![Task 1](img/task1.png)

---

## ✅ Task 2 – Create a New Branch

A new branch named `stack-implementation` was created using the command below. This branch was used to implement and test the core functionality before merging it into the `main` branch.

```bash
git checkout -b stack-implementation
```

![Task 2](img/task2.png)

---

## ✅ Task 3 – Create Project Files

The following files were created for the implementation:
- `ds.py` (data structures)
- `nodes.py` (Node class)
- `main_LL.py` (main execution file)
- `coordinates.csv` (data source file)

![Task 3](img/task3.png)

---

## ✅ Task 4 – Implement Stack with Linked List

Implemented the `Stack`, `LinkedList`, and `LinkedListNode` classes inside `ds.py`.

![Task 4](img/task4.png)

---

## ✅ Task 5 – Create Node Class

Defined a `Node` class in `nodes.py` to represent location data (id, latitude, longitude, name) imported from the CSV file.

![Task 5](img/task5.png)

---

## ✅ Task 6 – Parse CSV File and Push to Stack

Implemented `import_csv()` to read `coordinates.csv`, convert each row into a Node, and push it onto the stack.

![Task 6](img/task6.png)

---

## ✅ Task 7 – Print Removed Nodes

Ran the program to pop and print all nodes. Verified LIFO behavior by confirming the reverse order of the inserted elements.

![Task 7](img/task7.png)

---

## ✅ Task 8 – Popping Nodes from the Stack

Here, we iteratively pop each node from the stack and print its `id` and `name`. This confirms the LIFO behavior of the stack: the most recently added node is removed first. Once the stack is empty, the loop terminates.

![Task 8](img/task8.png)

---

## ✅ Task 9 – Merge & Finalize

Successfully merged `stack-implementation` into `main` using a pull request on GitHub.

![Task 9](img/task9.png)

---

## 📊 Summary Table

| Task | Description                             | File(s) Involved     |
|------|-----------------------------------------|----------------------|
| 1    | Initialized repo, created README        | `README.md`          |
| 2    | Created new branch                      | `stack-implementation` |
| 3    | Created project files                   | `ds.py`, `nodes.py`, etc. |
| 4    | Implemented Stack using Linked List     | `ds.py`              |
| 5    | Created Node class                      | `nodes.py`           |
| 6    | Parsed CSV and pushed to stack          | `main_LL.py`, `coordinates.csv` |
| 7    | Verified stack output                   | Terminal Output      |
| 8    | Explained pop behavior (LIFO)           | Terminal Output      |
| 9    | Merged to main                          | GitHub               |

---

## 🎯 Final Thoughts

With a fully functional stack built on linked lists and automated through CSV parsing, this project showcases modular design, real-world data processing, and clean Git management — from branching to merging.

