# 📊 Data Analyzer and Transformer (Python)

A **menu-driven Python console application** that performs analysis and transformations on a **1D numeric array**.  
This project is designed to strengthen **Python logic, OOP concepts, recursion, lambda functions, and data processing skills**.

---

## 🚀 Project Overview

The **Data Analyzer and Transformer Program** allows users to:
- Input a 1D array of integers
- View statistical summaries
- Calculate factorial using recursion
- Filter data using lambda functions
- Sort data in ascending or descending order

The program runs continuously until the user chooses to exit.

---

## 🎯 Objectives
- Practice Object-Oriented Programming (OOP)
- Work with lists and user input
- Apply recursion and lambda functions
- Strengthen logical thinking using Python
- Build menu-driven console applications

---

## 🛠️ Features

### ➕ Input Data
- Accepts multiple integers as input
- Stores data in a 1D list

### 📊 Display Data Summary
- Displays:
  - Total number of elements
  - Minimum value
  - Maximum value
  - Sum of all elements
  - Average of elements

### 🔁 Factorial Calculation (Recursion)
- Calculates factorial of a number selected from the array
- Uses **recursive function**
- Validates:
  - Number exists in array
  - Number is positive

### 🔍 Filter Data by Threshold (Lambda Function)
- Filters elements **greater than a user-defined threshold**
- Uses `filter()` with `lambda`

### 🔃 Sort Data
- Sort options:
  - Ascending order
  - Descending order

### 🚪 Exit Program
- Gracefully terminates the application

---

## 🧩 Concepts Used
- Object-Oriented Programming (Class & Object)
- `while` loop and `for` loop
- `match-case` statement (Python 3.10+)
- Lists and built-in functions (`min`, `max`, `sum`)
- Recursion
- Lambda functions
- Exception handling (`try-except`)
- Menu-driven program design

---

## 🧪 Sample Output

```text
Welcome to the Data Analyzer and Transformer Program

Main Menu:
1. Input Data
2. Display Data Summary
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Exit program

📊 Data Summary:
Total elements: 5
Minimum value: 2
Maximum value: 10
Sum of all values: 30
Average value: 6.0

Factorial of 5 is: 120

Filtered values (greater than threshold): [7, 8, 10]
