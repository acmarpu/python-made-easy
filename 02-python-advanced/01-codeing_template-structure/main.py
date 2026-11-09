# This is main.py
# very simple code to run the pipeline  

# importing Modules

import os
import sys

import math
from datetime import datetime

from core.calculator import Calculator
from core.user import user_login
from config.settings import DATABASE_CONFIG, user_profiles
from utils.helpers import log_info

# Declaring Variables
# Reading these variables from config folder
valid_user = user_login("user1", "password123")
log_info(f"User user1 {valid_user} logged in successfully.")

user_profile = user_profiles.get("user1", {"name": "unknown", "age": 0})
log_info(f"User profile: {user_profile}")


# main function()
def main():
    # Calling the modules and functions in sequence (squence of business logic/ packages /modules  /functions /class or obejcts)
    log_info("Starting the main function...")

    # METHOD 1: Using the Calculator class to perform addition
    # calc = Calculator()
    # result = calc.add(5, 3)
    

    # METHOD 2: Using the Calculator function to perform addition
    Calculator_result = Calculator(5, 3, "add" )



# Call the main function
if __name__ == "__main__":
    main()