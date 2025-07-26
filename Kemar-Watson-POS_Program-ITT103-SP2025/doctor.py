import random
from person import Person

class Doctor(Person):
    """Doctor class inheriting from Person"""
    
    def __init__(self, name: str, age: int, gender: str, specialty: str):
        super().__init__(name, age, gender)
        self.doctor_id = self._generate_id()
        self.specialty = specialty
        self.schedule = []
        self._initialize_schedule()
    
    def _generate_id(self) -> str:
        """Generate unique doctor ID"""
        return f"D{random.randint(1000, 9999)}"
    
    def _initialize_schedule(self):
        """Initialize default schedule"""
        self.schedule = [
            "09:00", "10:00", "11:00", "14:00", "15:00", "16:00"
        ]
    
    def is_available(self, date: str, time: str) -> bool:
        """Check if doctor is available at given date and time"""
        try:
            # Check if time is in schedule
            if time in self.schedule:
                return True
            return False
        except Exception as e:
            print(f"Error checking availability: {e}")
            return False
    
    def view_schedule(self) -> str:
        """View doctor's schedule"""
        schedule_info = f"\n=== DOCTOR SCHEDULE ===\n"
        schedule_info += f"Doctor ID: {self.doctor_id}\n"
        schedule_info += f"Name: {self.name}\n"
        schedule_info += f"Specialty: {self.specialty}\n"
        schedule_info += f"Available Times: {', '.join(self.schedule)}\n"
        return schedule_info 