import re
from hospital_system import HospitalSystem

def display_menu() -> None:
    print("\n" + "="*60)
    print("\t\tUCC HOSPITAL MANAGEMENT SYSTEM")
    print("="*60)
    print("1.  Patient Management")
    print("2.  Doctor Management")
    print("3.  Appointment Management")
    print("4.  Billing System")
    print("5.  View Records")
    print("6.  Exit")
    print("="*60)

def patient_menu(hospital: HospitalSystem) -> None:
    while True:
        print("\n--- PATIENT MANAGEMENT ---")
        print("1. Register New Patient")
        print("2. View Patient Details")
        print("3. List All Patients")
        print("4. Back to Main Menu")
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice == "1":
            try:
                name = input("Enter patient name: ").strip()
                while not re.match("^[A-Z][a-z]+ [A-Z][a-z]+$", name):
                    print ("Error! Make sure you only use letters in your name")
                    name = input("Please patient name: ")
                age = int(input("Enter patient age: "))
                while age <= 0 or age > 150:
                    print ("Age must be between 1 and 150")
                    age = int(input("Please enter patient age: "))
                gender = input("Enter patient gender (male/female/other): ").strip().lower()
                while not (gender in ['male', 'female', 'other']):
                    print ("Gender must be male, female, or other")
                    gender = input("Enter patient gender (male/female/other): ").strip().lower()
                hospital.add_patient(name, age, gender)
            except ValueError:
                print("Invalid age! Please enter a valid number.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            patient_id = input("Enter patient ID: ").strip().upper()
            hospital.view_patient_details(patient_id)
        elif choice == "3":
            hospital.list_all_patients()
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please try again.")

def doctor_menu(hospital: HospitalSystem) -> None:
    while True:
        print("\n--- DOCTOR MANAGEMENT ---")
        print("1. Add New Doctor")
        print("2. View Doctor Details")
        print("3. List All Doctors")
        print("4. Back to Main Menu")
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice == "1":
            try:
                name = input("Enter doctor name: ").strip()
                while not re.match("^[A-Z][a-z]+ [A-Z][a-z]+$", name):
                    print ("Error! Make sure you only use letters in your name")
                    name = input("Please doctor name: ")
                age = int(input("Enter doctor age: "))
                while age <= 0 or age > 150:
                    print ("Age must be between 1 and 150")
                    age = int(input("Please enter doctor age: "))
                gender = input("Enter doctor gender (male/female/other): ").strip().lower()
                while not (gender in ['male', 'female', 'other']):
                    print ("Gender must be male, female, or other")
                    gender = input("Enter doctor gender (male/female/other): ").strip().lower()
                specialty = input("Enter doctor specialty: ").strip()
                hospital.add_doctor(name, age, gender, specialty)
            except ValueError:
                print("Invalid age! Please enter a valid number.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            doctor_id = input("Enter doctor ID: ").strip().upper()
            hospital.view_doctor_details(doctor_id)
        elif choice == "3":
            hospital.list_all_doctors()
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please try again.")

def appointment_menu(hospital: HospitalSystem) -> None:
    while True:
        print("\n--- APPOINTMENT MANAGEMENT ---")
        print("1. Book Appointment")
        print("2. Cancel Appointment")
        print("3. View Appointment")
        print("4. List All Appointments")
        print("5. Back to Main Menu")
        choice = input("\nEnter your choice (1-5): ").strip()
        if choice == "1":
            try:
                patient_id = input("Enter patient ID: ").strip()
                while patient_id not in hospital.patients:
                    print("Patient not found!")
                    patient_id = input("Enter patient ID: ").strip()
                doctor_id = input("Enter doctor ID: ").strip()
                while doctor_id not in hospital.doctors:
                    print("Doctor not found!")
                    doctor_id = input("Enter doctor ID: ").strip()
                print("Available slots:")
                print("Please enter the date and time for the appointment.")
                year = input("Enter appointment year (YYYY): ").strip()
                while not year.isdigit() or len(year) != 4 or int(year) < hospital.year:
                    print("Invalid year! Please enter a valid year (YYYY). Year must be greater than or equal to the current year.")
                    year = input("Enter appointment year (YYYY): ").strip()
                month= input("Enter appointment month (1-12): ").strip()
                while not month.isdigit() or int(month) < hospital.month or int(month) > 12:
                    print("Invalid month! Please enter a valid month (1-12). Month must be greater than or equal to the current month.")
                    month = input("Enter appointment month (1-12): ").strip()
                day = input("Enter appointment day (1-31): ").strip()
                while not day.isdigit() or (int(day) < hospital.day and int(month) <= hospital.month) or int(day) > 31:
                    print("Invalid day! Please enter a valid day (1-31). Day must be greater than or equal to the current day.")
                    day = input("Enter appointment day (1-31): ").strip()
                print("Available slots:")
                hospital.view_doctor_details(doctor_id)
                date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
                time = input("Enter appointment time (HH:MM): ").strip()
                while not re.match(r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$", time) :
                    print("Invalid time format! Please enter time in HH:MM format.")
                    time = input("Enter appointment time (HH:MM): ").strip()
                    while not hospital.is_available(doctor_id, date, time):
                        print("Doctor is not available at this time. Please choose another time.")
                        time = input("Enter appointment time (HH:MM): ").strip()
                hospital.book_appointment(patient_id, doctor_id, date, time)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            appointment_id = input("Enter appointment ID: ").strip()
            hospital.cancel_appointment(appointment_id)
        elif choice == "3":
            appointment_id = input("Enter appointment ID: ").strip()
            hospital.view_appointment(appointment_id)
        elif choice == "4":
            hospital.list_all_appointments()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

def billing_menu(hospital: HospitalSystem) -> None:
    while True:
        print("\n--- BILLING SYSTEM ---")
        print("1. Generate Bill")
        print("2. Add Service to Bill")
        print("3. View Bill/Receipt")
        print("4. Back to Main Menu")
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice == "1":
            appointment_id = input("Enter appointment ID: ").strip()
            hospital.generate_bill(appointment_id)
        elif choice == "2":
            try:
                appointment_id = input("Enter appointment ID: ").strip()
                service_name = input("Enter service name: ").strip()
                fee = float(input("Enter service fee: "))
                hospital.add_service_to_bill(appointment_id, service_name, fee)
            except ValueError:
                print("Invalid fee! Please enter a valid number.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "3":
            appointment_id = input("Enter appointment ID: ").strip().upper()
            hospital.view_bill(appointment_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please try again.")

def view_records_menu(hospital: HospitalSystem) -> None:
    while True:
        print("\n--- VIEW RECORDS ---")
        print("1. List All Patients")
        print("2. List All Doctors")
        print("3. List All Appointments")
        print("4. Back to Main Menu")
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice == "1":
            hospital.list_all_patients()
        elif choice == "2":
            hospital.list_all_doctors()
        elif choice == "3":
            hospital.list_all_appointments()
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please try again.")

def main():
    hospital = HospitalSystem()
    print("Welcome to UCC Hospital Management System!")
    print("Loading Sample Data...")
    try:
        hospital.add_patient("John Smith", 35, "male")
        hospital.add_patient("Mary Johnson", 28, "female")
        hospital.add_patient("Robert Davis", 45, "male")
        hospital.add_doctor("Dr. Sarah Wilson", 40, "female", "Cardiology")
        hospital.add_doctor("Dr. Michael Brown", 38, "male", "Pediatrics")
        hospital.add_doctor("Dr. Lisa Garcia", 35, "female", "Neurology")
        print("Sample data loaded successfully!")
    except Exception as e:
        print(f"Error loading sample data: {e}")
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        if choice == "1":
            patient_menu(hospital)
        elif choice == "2":
            doctor_menu(hospital)
        elif choice == "3":
            appointment_menu(hospital)
        elif choice == "4":
            billing_menu(hospital)
        elif choice == "5":
            view_records_menu(hospital)
        elif choice == "6":
            print("\nThank you for using UCC Hospital Management System!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main() 