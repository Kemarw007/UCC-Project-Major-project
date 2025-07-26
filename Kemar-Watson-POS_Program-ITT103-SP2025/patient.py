import random
from person import Person

class Patient(Person):
    """Patient class inheriting from Person"""
    
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)
        self.patient_id = self._generate_id()
        self.appointment_list = []
    
    def _generate_id(self) -> str:
        """Generate unique patient ID"""
        return f"P{random.randint(10000, 99999)}"
    
    def book_appointment(self, appointment) -> bool:
        """Book an appointment for the patient"""
        try:
            if appointment not in self.appointment_list:
                self.appointment_list.append(appointment)
                return True
            return False
        except Exception as e:
            print(f"Error booking appointment: {e}")
            return False
    
    def view_profile(self) -> str:
        """View patient profile"""
        profile = f"\n=== PATIENT PROFILE ===\n"
        profile += f"Patient ID: {self.patient_id}\n"
        profile += f"{super().display()}\n"
        profile += f"Total Appointments: {len(self.appointment_list)}\n"
        return profile 