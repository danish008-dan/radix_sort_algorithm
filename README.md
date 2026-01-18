Project Title: Radix Sort Algorithm

Overview
This project contains a Python implementation of the Radix Sort algorithm. Radix Sort works by sorting numbers digit by digit, starting from the least significant digit and moving toward the most significant digit. Counting Sort is used internally to ensure stable sorting at each digit level.

Purpose
The purpose of this project is to demonstrate a clear and well-documented implementation of Radix Sort suitable for academic learning, DAA coursework, and interview preparation.

Algorithm Used
Radix Sort
Counting Sort (as a subroutine)

Features

Non-comparison based sorting algorithm

Stable sorting technique

Efficient for large integer datasets

Well-commented and easy-to-understand code

Suitable for GitHub portfolio and academic submission

Time and Space Complexity
Time Complexity: O(d × (n + k))
Where d is the number of digits, n is the number of elements, and k is the base (10).

Space Complexity: O(n + k)

Stability
Radix Sort is a stable sorting algorithm.

Input Constraints

Works with non-negative integers

Best suited for datasets with numbers having similar digit lengths

Use Cases

Sorting roll numbers or student IDs

Sorting large numeric datasets

Educational and interview preparation purposes

How to Run

Ensure Python is installed on your system

Open a terminal or command prompt

Run the file using:
python radix_sort.py

Output
The program prints the original array followed by the sorted array.
