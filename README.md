# Bring-Your-Own-Project
# UPI Fraud Detection Simulator
# Project Overview
The UPI Fraud Detection Simulator is a beginner-friendly Python project that mimics how digital payment systems detect potentially fraudulent transactions.With the rise of UPI-based payments, online scams and frauds have become increasingly common. This project aims to spread awareness by demonstrating how simple rule-based systems can identify suspicious transactions.

# Problem Statement
UPI fraud and online scams are growing rapidly. Users often unknowingly send money to unknown or suspicious accounts.

# Solution
This project takes transaction details as input and analyzes them using basic rule-based logic to determine whether a transaction is Safe or Risky.

# Features
* Takes user input (sender, receiver UPI ID, amount, transaction frequency)
* Detects suspicious patterns:
   ~ Unknown receiver UPI ID
   ~ Large transaction amount
   ~ Multiple transactions in short time
   ~ Suspicious UPI ID patterns
* Assigns a risk score based on conditions
* Displays:
   ✅ Safe Transaction
   🚨 Risky Transaction
* Provides user confirmation for risky transactions

# Technologies Used
* Python (Core)
* Basic concepts:
   ~ Conditional statements (if-else)
   ~ Lists
   ~ User input handling
   ~ Simple logic building

# How It Works
The system uses a rule-based scoring method:
Condition                    Risk Score
Unknown UPI ID                 +2
Amount > ₹5000                 +2
Multiple transactions (>3)     +1
Suspicious pattern in UPI ID   +1
If total score ≥ 3 → Transaction is marked as RISKY
Otherwise → Transaction is SAFE

# How to Run the Project
Make sure Python is installed
Copy the code into a .py file (e.g., upi_fraud_detector.py)
Open terminal / command prompt
Run the program: python upi_fraud_detector.py
Enter the required inputs and view the result

# Sample Output
====== UPI Fraud Detection Simulator ======
Enter Your Name: Rahul
Enter Receiver UPI ID: random123@ok
Enter Amount (₹): 8000
How many transactions in last 5 minutes? 4

Checking transaction...

⚠️ Unknown UPI ID
⚠️ High amount transaction
⚠️ Too many transactions in short time
⚠️ Suspicious UPI pattern

----- RESULT -----
🚨 Transaction Status: RISKY
Advice: Do NOT proceed without verification!

# Future Improvements
~ GUI interface using Tkinter
~ OTP verification system
~ Transaction history storage
~ Machine Learning-based fraud detection
~ Integration with real payment APIs (simulation)

# Learning Outcomes
Understanding real-world problem solving
Applying conditional logic in practical scenarios
Improving python programming skills
Applying conditional logic in practical scenarios
Building rule-based systems
Improving Python programming skills
