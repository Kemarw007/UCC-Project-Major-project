from abc import abstractmethod


class Person:
    """Base class for all persons in the hospital system"""
    
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def _generate_id(self) -> str:
        """Generate unique ID for the person"""
        pass
    
    def validate(self) -> bool:
        """Validate person data"""
        try:
            if not self.name or len(self.name.strip()) == 0:
                raise ValueError("Name cannot be empty")
            if self.age <= 0 or self.age > 150:
                raise ValueError("Age must be between 1 and 150")
            if self.gender.lower() not in ['male', 'female', 'other']:
                raise ValueError("Gender must be male, female, or other")
            return True
        except Exception as e:
            print(f"Validation error: {e}")
            return False
    
    def display(self) -> str:
        """Display person information"""
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}" 