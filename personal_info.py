# ==============================================================================
# Author: Smruti Ranjan Sahoo
# Project: Personal Information Manager
# Description: An interactive CLI application that stores static personal data,
#              accepts validated dynamic user inputs, and prints a formatted profile.
# ==============================================================================

def main():
    # --------------------------------------------------------------------------
    # Step 6: Welcome Message
    # --------------------------------------------------------------------------
    print("=" * 50)
    print("      WELCOME TO PERSONAL INFORMATION MANAGER       ")
    print("=" * 50)
    print()

    # --------------------------------------------------------------------------
    # Step 2: Store Static Information
    # --------------------------------------------------------------------------
    # Storing baseline profile details using correct data types
    name = "Smruti Ranjan Sahoo"  # String: Full name
    age = 20                      # Integer: Current age in years
    city = "Odisha"               # String: Current city/state location
    hobby = "Coding and Physics"  # String: Primary interest

    # --------------------------------------------------------------------------
    # Step 3: Get User Input with Basic Validation
    # --------------------------------------------------------------------------
    print("Please customize your profile card below:")
    
    # Validation loop for Favorite Food
    while True:
        fav_food = input("Enter your favorite food: ").strip()
        if fav_food == "":
            print("❌ Input cannot be empty. Please enter a valid food item.")
        else:
            break
            
    # Validation loop for Favorite Color
    while True:
        fav_color = input("Enter your favorite color: ").strip()
        if fav_color == "":
            print("❌ Input cannot be empty. Please enter a valid color.")
        else:
            break

    print("\nProcessing your profile...\n")

    # --------------------------------------------------------------------------
    # Step 6: Enhancements (Data Calculations)
    # --------------------------------------------------------------------------
    # Calculate age in months based on the static integer age variable
    age_in_months = age * 12

    # --------------------------------------------------------------------------
    # Step 4: Display Formatted Information
    # --------------------------------------------------------------------------
    # Standardizing string formatting using string methods (.title(), .upper())
    print("-" * 50)
    print(f" PROFILE CARD: {name.upper()} ")
    print("-" * 50)
    
    # Displaying static and calculated data using f-strings
    print(f"📍 Location      : {city.title()}")
    print(f"⏳ Age           : {age} years old ({age_in_months:,} months)")
    print(f"🎨 Primary Hobby : {hobby}")
    
    print("-" * 50)
    print(" USER PREFERENCES ")
    print("-" * 50)
    
    # Displaying validated dynamic data
    print(f"🍲 Favorite Food : {fav_food.title()}")
    print(f"🎨 Favorite Color: {fav_color.title()}")
    print("-" * 50)
    print()

    # --------------------------------------------------------------------------
    # Step 6: Goodbye Message
    # --------------------------------------------------------------------------
    print("=" * 50)
    print("        Profile saved successfully! Goodbye.        ")
    print("=" * 50)

if __name__ == "__main__":
    main()
