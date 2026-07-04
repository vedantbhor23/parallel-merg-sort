# 🚀 Merge Sort & Multithreaded Merge Sort Visualization

A Python desktop application that demonstrates the working of **Merge Sort** and **Multithreaded Merge Sort** through an interactive graphical user interface (GUI). The application compares the execution time of both algorithms, helping users understand the effect of multithreading on sorting performance.

---

## 📌 Overview

This project implements the Merge Sort algorithm in two ways:

* **Standard Merge Sort**
* **Multithreaded Merge Sort**

Users can provide their own input array or generate a random array. After sorting, the application displays the sorted results along with the execution time of each approach for performance comparison.

---

## ✨ Features

* Interactive graphical user interface (GUI)
* Standard Merge Sort implementation
* Multithreaded Merge Sort implementation
* User-defined or randomly generated input arrays
* Execution time comparison
* Displays sorted output
* Simple and easy-to-use interface

---

## 🛠️ Technologies Used

* Python 3
* Tkinter (GUI)
* threading
* random
* time

---

## 📂 Project Structure

```text
Merge-Sort-Visualization/
│── merg_sort_ui.py
│── README.md
└── requirements.txt
```

---

## ⚙️ Requirements

* Python **3.8** or later

This project uses only Python's standard library, so no additional packages need to be installed.

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
```

2. Navigate to the project folder:

```bash
cd your-repository
```

3. Run the application:

```bash
python merg_sort_ui.py
```

The graphical user interface will launch automatically.

---

## 📖 Usage

1. Launch the application.
2. Enter the input array or generate a random array.
3. Start the sorting process.
4. View:

   * Sorted array
   * Execution time of Standard Merge Sort
   * Execution time of Multithreaded Merge Sort
   * Performance comparison

---

## 📊 Time Complexity

| Algorithm                | Best       | Average    | Worst      | Space |
| ------------------------ | ---------- | ---------- | ---------- | ----- |
| Merge Sort               | O(n log n) | O(n log n) | O(n log n) | O(n)  |
| Multithreaded Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n)  |

> **Note:** Due to Python's Global Interpreter Lock (GIL), multithreading may not always provide a performance improvement for CPU-bound tasks. The comparison is intended for educational purposes.

---

## 🎯 Learning Objectives

* Understand the Divide and Conquer technique
* Learn the implementation of Merge Sort
* Explore multithreading in Python
* Compare sequential and parallel algorithm execution
* Analyze algorithm performance using execution time

---

## 🚀 Future Improvements

* Add visualization of the sorting process
* Include additional sorting algorithms
* Display performance graphs
* Support larger datasets
* Improve GUI design and user experience

---

## 👨‍💻 Author

**Vedant Bhor**

Computer Engineering Student

PES Modern College of Engineering, Pune

---

## 📄 License

This project is intended for educational and academic purposes.
