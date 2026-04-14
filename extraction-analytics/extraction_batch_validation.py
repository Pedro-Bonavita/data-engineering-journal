"""
Journal Entry: Parameter Validation for Resin Extraction
Concept: Dictionary mapping for industrial standards and process control.
"""

# Dictionary mapping extraction standards
# Key: Extraction Method | Value: Dictionary with standard Temp and Pressure
extraction_standards = {
    "rosin": {"temp_c": 85.0, "pressure_psi": 1000},
    "bho": {"temp_c": -40.0, "pressure_psi": 45},
    "hash_wash": {"temp_c": 2.0, "pressure_psi": 0}
}

def validate_setup():
    print("\n--- EXTRACTION UNIT VALIDATION ---")
    method = input("Select extraction method (rosin/bho/hash_wash): ").lower()
    
    if method in extraction_standards:
        # Get the standard data from dictionary
        standard = extraction_standards[method]
        
        # User inputs current machine readings
        current_temp = float(input(f"Enter current temperature for {method} (ºC): "))
        
        # Logic validation (similar to your login check)
        # Here we allow a small margin of error for temperature (+/- 2 degrees)
        temp_ok = standard["temp_c"] - 2 <= current_temp <= standard["temp_c"] + 2
        
        if temp_ok:
            print(f"✅ Status: READY. Starting {method} extraction batch.")
        else:
            print(f"❌ Status: ERROR. Temperature out of range for {method}!")
    else:
        print("⚠️ Status: Method not recognized in current SOP (Standard Operating Procedure).")

# Simulate industrial loop
while True:
    print("\n1 - Validate New Batch")
    print("0 - Shutdown System")
    
    option = input("System Option: ")
    
    if option == '1':
        validate_setup()
    elif option == '0':
        print("Powering down extraction unit...")
        break