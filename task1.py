# ============================================================
# Task 1: User Login Check
# Real-World Application: Authentication systems
# ============================================================

print("----------- Task 1: User Login Check -----------")

# Predefined credentials
correct_username = "admin"
correct_password = "1234"

# Input from user
username = input("Enter username: ")
password = input("Enter password: ")

# Check login credentials
if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Credentials")


# ============================================================
# Task 2: Pass / Fail Analyzer
# Real-World Application: Academic evaluation systems
# ============================================================

print("\n----------- Task 2: Pass / Fail Analyzer -----------")

marks = [45, 78, 90, 33, 60]

pass_count = 0
fail_count = 0

for mark in marks:
    if mark >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("Total Students:", len(marks))
print("Passed Students:", pass_count)
print("Failed Students:", fail_count)


# ============================================================
# Task 3: Simple Data Cleaner
# Real-World Application: Data preprocessing before analysis
# ============================================================

print("\n----------- Task 3: Simple Data Cleaner -----------")

names = [" Alice ", "bob", " CHARLIE "]

cleaned_names = []

for name in names:
    cleaned = name.strip().lower()  # remove spaces + convert to lowercase
    cleaned_names.append(cleaned)

print("Original Names:", names)
print("Cleaned Names:", cleaned_names)


# ============================================================
# Task 4: Message Length Analyzer
# Real-World Application: Text filtering and validation systems
# ============================================================

print("\n----------- Task 4: Message Length Analyzer -----------")

messages = ["Hi", "Welcome to the platform", "OK"]

for message in messages:
    length = len(message)
    print(f"Message: '{message}' | Length: {length}")
    
    if length > 10:
        print("⚠️ This message is longer than 10 characters")


# ============================================================
# Task 5: Error Message Detector
# Real-World Application: Monitoring and log analysis systems
# ============================================================

print("\n----------- Task 5: Error Message Detector -----------")

logs = ["INFO", "ERROR", "WARNING", "ERROR"]

error_count = 0

for log in logs:
    if log == "ERROR":
        error_count += 1

print("Total ERROR entries:", error_count)
