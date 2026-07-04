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

