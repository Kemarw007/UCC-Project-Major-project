import datetime

from appointment import Appointment

class Bill:
    """Bill class to handle billing and receipts"""
    def __init__(self, appointment: Appointment):
        self.appointment = appointment
        self.consultation_fee = appointment.consultation_fee if appointment.status != "Cancelled" else 0
        self.additional_services = {}
        self.total_amount = self.consultation_fee
    
    def add_service(self, service_name: str, fee: float) -> bool:
        """Add additional service to the bill"""
        try:
            if fee > 0:
                self.additional_services[service_name] = fee
                self.total_amount += fee
                return True
            return False
        except Exception as e:
            print(f"Error adding service: {e}")
            return False
    
    def generate_receipt(self) -> str:
        """Generate formatted receipt"""
        receipt = "\n" + "="*50 + "\n"
        receipt += "           UCC HOSPITAL CENTER\n"
        receipt += "              Medical Services\n"
        receipt += "="*50 + "\n"
        receipt += f"Receipt Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        receipt += f"Appointment ID: {self.appointment.appointment_id}\n"
        receipt += f"Patient: {self.appointment.patient.name}\n"
        receipt += f"Doctor: {self.appointment.doctor.name}\n"
        receipt += f"Date: {self.appointment.date} at {self.appointment.time}\n"
        receipt += f"Status: {self.appointment.status}\n"
        receipt += "-"*50 + "\n"
        receipt += "SERVICES:\n"
        receipt += f"  Consultation Fee: JMD$ {self.consultation_fee:,.2f}\n"
        
        for service, fee in self.additional_services.items():
            receipt += f"  {service}: JMD$ {fee:,.2f}\n"
        
        receipt += "-"*50 + "\n"
        receipt += f"TOTAL AMOUNT: JMD$ {self.total_amount:,.2f}\n"
        receipt += "="*50 + "\n"
        receipt += "Thank you for choosing UCC Hospital Center!\n"
        receipt += "="*50 + "\n"
        return receipt 