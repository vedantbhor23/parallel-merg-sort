import threading
import time
import random
import tkinter as tk
from tkinter import messagebox, scrolledtext



# ------------------- MERGE FUNCTION -------------------
def merge(arr, left, mid, right):
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    i = j = 0
    k = left

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

# ------------------- NORMAL MERGE SORT -------------------
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

# ------------------- MULTITHREADED MERGE SORT -------------------
def threaded_merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        left_thread = threading.Thread(target=threaded_merge_sort, args=(arr, left, mid))
        right_thread = threading.Thread(target=threaded_merge_sort, args=(arr, mid + 1, right))
        left_thread.start()
        right_thread.start()
        left_thread.join()
        right_thread.join()
        merge(arr, left, mid, right)

# ------------------- MAIN FUNCTION (GUI HANDLER) -------------------
def run_sort():
    try:
        n = int(entry_n.get())
        user_input = entry_arr.get().strip()

        if user_input.lower() == "r":
            arr = [random.randint(0, 100000) for _ in range(n)]
        else:
            arr = list(map(int, user_input.split()))
            if len(arr) != n:
                messagebox.showwarning("Input Warning", "Number of elements doesn't match input count.")
                return

        arr1 = arr.copy()
        arr2 = arr.copy()

# --- Normal Merge Sort ---
        start_time = time.time()
        merge_sort(arr1, 0, len(arr1) - 1)
        normal_time = time.time() - start_time

# --- Multithreaded Merge Sort ---
        start_time = time.time()
        threaded_merge_sort(arr2, 0, len(arr2) - 1)
        threaded_time = time.time() - start_time

