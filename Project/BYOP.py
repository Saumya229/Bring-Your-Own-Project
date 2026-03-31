import time

print("====== UPI Fraud Detection Simulator ======")

# Trusted UPI IDs (simple list)
trusted_upi = [
    "amazon@upi",
    "flipkart@upi",
    "swiggy@upi",
    "zomato@upi",
    "paytm@upi"
]

# Take user input
sender = input("Enter Your Name: ")
receiver_upi = input("Enter Receiver UPI ID: ")
amount = float(input("Enter Amount (₹): "))
num_transactions = int(input("How many transactions in last 5 minutes? "))

print("\nChecking transaction...")
time.sleep(2)

# Risk variables
risk_score = 0

# Rule 1: Unknown receiver
if receiver_upi not in trusted_upi:
    print("Unknown UPI ID")
    risk_score = risk_score + 2

# Rule 2: Large amount
if amount > 5000:
    print("High amount transaction")
    risk_score = risk_score + 2

# Rule 3: Too many transactions
if num_transactions > 3:
    print("Too many transactions in short time")
    risk_score = risk_score + 1

# Extra beginner-level realistic rule
# Rule 4: Suspicious UPI pattern
if "123" in receiver_upi or receiver_upi.endswith("@ok"):
    print("Suspicious UPI pattern")
    risk_score = risk_score + 1

# Final decision
print("\n----- RESULT -----")

if risk_score >= 3:
    print("Transaction Status: RISKY")
    print("Advice: Do not proceed without verification!")

    # Simple confirmation (realistic touch)
    choice = input("Do you still want to continue? (yes/no): ")
    if choice.lower() == "yes":
        print("Transaction Done (at your own risk!)")
    else:
        print("Transaction Cancelled")

else:
    print(" Transaction Status: SAFE")
    print("Transaction Successful!")

print("\nThank you for using system!")
