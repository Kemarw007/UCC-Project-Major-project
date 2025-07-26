import random
from patient import Patient
from doctor import Doctor

class Appointment:
    """Appointment class to manage patient-doctor appointments"""
    
    def __init__(self, patient: Patient, doctor: Doctor, date: str, time: str):
        self.appointment_id = self._generate_appointment_id()
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.status = "Scheduled"
        self.consultation_fee = 3000  # JMD$ 3000
    
    def _generate_appointment_id(self) -> str:
        """Generate unique appointment ID"""
        return f"A{random.randint(100000, 999999)}"
    
    def confirm(self) -> bool:
        """Confirm the appointment"""
        try:
            if self.status == "Scheduled":
                self.status = "Confirmed"
                return True
            return False
        except Exception as e:
            print(f"Error confirming appointment: {e}")
            return False
    
    def cancel(self) -> bool:
        """Cancel the appointment"""
        try:
            if self.status in ["Scheduled", "Confirmed"]:
                self.status = "Cancelled"
                return True
            return False
        except Exception as e:
            print(f"Error cancelling appointment: {e}")
            return False
    
    def display(self) -> str:
        """Display appointment details"""
        appointment_info = f"\n=== APPOINTMENT DETAILS ===\n"
        appointment_info += f"Appointment ID: {self.appointment_id}\n"
        appointment_info += f"Patient: {self.patient.name} (ID: {self.patient.patient_id})\n"
        appointment_info += f"Doctor: {self.doctor.name} (ID: {self.doctor.doctor_id})\n"
        appointment_info += f"Date: {self.date}\n"
        appointment_info += f"Time: {self.time}\n"
        appointment_info += f"Status: {self.status}\n"
        return appointment_info 