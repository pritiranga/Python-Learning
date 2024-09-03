import os
import datetime

# Function to check cpu
def check_cpu(command):
    print(os.system(command))  # we can use "return os.system(command)"

# Function to check date
def check_date(command):
    print(os.system(command))

check_cpu("df -h")  # calling check_cpu function
check_date("date")  # calling check_date function

# OR make upper program short
def run_command(command):    # Defining function
    return os.system(command) 

run_command("df -h")         # Calling function

#function to show today's date
def show_date():
    return datetime.datetime.today()

today=show_date()
print(today)
