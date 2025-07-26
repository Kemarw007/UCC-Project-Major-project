from datetime import datetime
from typing import Dict, Optional
from patient import Patient
from doctor import Doctor
from appointment import Appointment
from bill import Bill

class HospitalSystem:
    """Main hospital management system class"""
    
    def __init__(self):
        self.patients: Dict[str, Patient] = {}
        self.doctors: Dict[str, Doctor] = {}
        self.appointments: Dict[str, Appointment] = {}
        self.bills: Dict[str, Bill] = {}
        self.month= datetime.now().date().month
        self.year = datetime.now().date().year
        self.day = datetime.now().date().day
    
    def add_patient(self, name: str, age: int, gender: str) -> Optional[str]:
        """Add a new patient to the system"""
        try:
            patient = Patient(name, age, gender)
            if patient.validate():
                self.patients[patient.patient_id] = patient
                print(f"Patient registered successfully! Patient ID: {patient.patient_id}")
                return patient.patient_id
            else:
                print("Invalid patient data. Please try again.")
                return None
        except Exception as e:
            print(f"Error adding patient: {e}")
            return None
    
    def add_doctor(self, name: str, age: int, gender: str, specialty: str) -> Optional[str]:
        """Add a new doctor to the system"""
        try:
            doctor = Doctor(name, age, gender, specialty)
            if doctor.validate():
                self.doctors[doctor.doctor_id] = doctor
                print(f"Doctor added successfully! Doctor ID: {doctor.doctor_id}")
                return doctor.doctor_id
            else:
                print("Invalid doctor data. Please try again.")
                return None
        except Exception as e:
            print(f"Error adding doctor: {e}")
            return None
    
    def book_appointment(self, patient_id: str, doctor_id: str, date: str, time: str) -> Optional[str]:
        """Book an appointment between patient and doctor"""
        try:
            # Validate patient and doctor exist
            if patient_id not in self.patients:
                print("Patient not found!")
                return None
            
            if doctor_id not in self.doctors:
                print("Doctor not found!")
                return None
            
            patient = self.patients[patient_id]
            doctor = self.doctors[doctor_id]
            
            # Check if doctor is available
            if not doctor.is_available(date, time):
                print("Doctor is not available at the specified time!")
                return None
            
            # Check for scheduling conflicts
            for appointment in self.appointments.values():
                if (appointment.doctor.doctor_id == doctor_id and 
                    appointment.date == date and 
                    appointment.time == time and 
                    appointment.status != "Cancelled"):
                    print("This time slot is already booked!")
                    return None
            
            # Create appointment
            appointment = Appointment(patient, doctor, date, time)
            self.appointments[appointment.appointment_id] = appointment
            
            # Add to patient's appointment list
            patient.book_appointment(appointment)
            
            print(f"Appointment booked successfully! Appointment ID: {appointment.appointment_id}")
            return appointment.appointment_id
            
        except Exception as e:
            print(f"Error booking appointment: {e}")
            return None
    
    def cancel_appointment(self, appointment_id: str) -> bool:
        """Cancel an appointment"""
        try:
            if appointment_id in self.appointments:
                appointment = self.appointments[appointment_id]
                if appointment.cancel():
                    print(f"Appointment {appointment_id} cancelled successfully!")
                    return True
                else:
                    print("Unable to cancel appointment.")
                    return False
            else:
                print("Appointment not found!")
                return False
        except Exception as e:
            print(f"Error cancelling appointment: {e}")
            return False
    
    def generate_bill(self, appointment_id: str) -> Optional[str]:
        """Generate a bill for an appointment"""
        try:
            if appointment_id not in self.appointments:
                print("Appointment not found!")
                return None
            
            appointment = self.appointments[appointment_id]
            bill = Bill(appointment)
            self.bills[appointment_id] = bill
            
            print("Bill generated successfully!")
            return appointment_id
            
        except Exception as e:
            print(f"Error generating bill: {e}")
            return None
    
    def add_service_to_bill(self, appointment_id: str, service_name: str, fee: float) -> bool:
        """Add additional service to a bill"""
        try:
            if appointment_id in self.bills:
                bill = self.bills[appointment_id]
                if bill.add_service(service_name, fee):
                    print(f"Service '{service_name}' added to bill successfully!")
                    return True
                else:
                    print("Invalid service fee!")
                    return False
            else:
                print("Bill not found! Generate bill first.")
                return False
        except Exception as e:
            print(f"Error adding service: {e}")
            return False
    
    def view_patient_details(self, patient_id: str) -> None:
        """View patient details"""
        try:
            if patient_id in self.patients:
                patient = self.patients[patient_id]
                print(patient.view_profile())
            else:
                print("Patient not found!")
        except Exception as e:
            print(f"Error viewing patient details: {e}")
    
    def view_doctor_details(self, doctor_id: str) -> None:
        """View doctor details"""
        try:
            if doctor_id in self.doctors:
                doctor = self.doctors[doctor_id]
                print(doctor.view_schedule())
            else:
                print("Doctor not found!")
        except Exception as e:
            print(f"Error viewing doctor details: {e}")
    
    def view_appointment(self, appointment_id: str) -> None:
        """View appointment details"""
        try:
            if appointment_id in self.appointments:
                appointment = self.appointments[appointment_id]
                print(appointment.display())
            else:
                print("Appointment not found!")
        except Exception as e:
            print(f"Error viewing appointment: {e}")
    
    def view_bill(self, appointment_id: str) -> None:
        """View bill/receipt"""
        try:
            if appointment_id in self.bills:
                bill = self.bills[appointment_id]
                print(bill.generate_receipt())
            else:
                print("Bill not found! Generate bill first.")
        except Exception as e:
            print(f"Error viewing bill: {e}")
    
    def list_all_patients(self) -> None:
        """List all patients"""
        if not self.patients:
            print("No patients registered.")
            return
        
        print("\n=== ALL PATIENTS ===")
        for patient_id, patient in self.patients.items():
            print(f"ID: {patient_id} | {patient.name} | Age: {patient.age} | Gender: {patient.gender}")
    
    def list_all_doctors(self) -> None:
        """List all doctors"""
        if not self.doctors:
            print("No doctors registered.")
            return
        
        print("\n=== ALL DOCTORS ===")
        for doctor_id, doctor in self.doctors.items():
            print(f"ID: {doctor_id} | {doctor.name} | Specialty: {doctor.specialty} | Gender: {doctor.gender}")
    
    def list_all_appointments(self) -> None:
        """List all appointments"""
        if not self.appointments:
            print("No appointments scheduled.")
            return
        
        print("\n=== ALL APPOINTMENTS ===")
        for appointment_id, appointment in self.appointments.items():
            print(f"ID: {appointment_id} | Patient: {appointment.patient.name} | Doctor: {appointment.doctor.name} | Date: {appointment.date} | Time: {appointment.time} | Status: {appointment.status}") 


    def is_available(self, doctor_id: str, date: str, time: str) -> bool:
        """Check if a doctor is available at a specific date and time"""
        try:
            if doctor_id in self.doctors:
                doctor = self.doctors[doctor_id]
                return doctor.is_available(date, time)
            else:
                print("Doctor not found!")
                return False
        except Exception as e:
            print(f"Error checking availability: {e}")
            return False