# Assignment #3 – Git/GitHub – Stack Implementation with Linked List

## 📂 Repository Contents

- `ds.py` → Contains the stack implementation using a linked list.
- `nodes.py` → Defines the `Node` class with ID, latitude, longitude, and name.
- `coordinates.csv` → Stores sample node data in CSV format.
- `main_LL.py` → Handles CSV import, stack operations, and printing results.

---

## 📸 Screenshots

### Task 1 – Creating the Repository on GitHub  
![task1](img/task1.png)

### Task 2 – Cloning the Repository via Terminal  
![task2](img/task2.png)

### Task 3 – Creating Files  
![task3](img/task3.png)

### Task 4 – Writing the Code  
![task4](img/task4.png)

### Task 5 – Running the Script & Output  
![task5](img/task5.png)


## Task 6 – Reading Node Data from CSV

In this step, we implemented a function that reads geographical node data from a CSV file and converts it into a list of `Node` objects. Each line in the CSV includes an `id`, `latitude`, `longitude`, and `name`, which are parsed and used to instantiate the `Node` class. This list is later used to populate our stack.

![Task 6](img/task6.png)

## Task 7 – Pushing Nodes onto the Stack

Once the nodes are read from the CSV file, each node is pushed onto the stack using our custom `push` method. The stack is implemented using a linked list, which allows us to maintain the Last-In-First-Out (LIFO) behavior. This step verifies that nodes are correctly stored in the stack.

![Task 7](img/task7.png)

## Task 8 – Popping Nodes from the Stack

Here, we iteratively pop each node from the stack and print its `id` and `name`. This confirms the LIFO behavior of the stack: the most recently added node is removed first. Once the stack is empty, the loop terminates.

![Task 8](img/task8.png)

## Task 9 – Final Code Integration and Output Testing

In the final step, we ran the complete script (`main_LL.py`) to verify the full functionality. The program reads nodes from the CSV, pushes them onto the stack, and then pops and prints them one by one. The final output confirms that all components are working together correctly.

![Task 9](img/task9.png)


---

## 📝 Usage

To run the project:



```bash
python main_LL.py

