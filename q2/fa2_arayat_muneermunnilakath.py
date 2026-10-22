class Patient:
    def __init__ (self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_bill_amount(self):
        return self.bill_amount
        
    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount
        
    def calculate_bill(self):
        return self.bill_amount
        
class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount()*0.80
        
class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount()*0.85
        
regular_patient = Patient("Juan",10000)
senior_patient = SeniorPatient("Dela",10000)
philhealth_patient = PhilHealthPatient("Cruz",10000)

print("---HOSPITAL BILL---")
print(f"\nPatient name: {regular_patient.get_name()}")
print(f"Original Bill: {regular_patient.get_bill_amount()}")
print(f"Final Bill: {regular_patient.calculate_bill()}")

print(f"\nPatient name: {senior_patient.get_name()}")
print(f"Original Bill: {senior_patient.get_bill_amount()}")
print(f"Final Bill: {senior_patient.calculate_bill()}")

print(f"\nPatient name: {philhealth_patient.get_name()}")
print(f"Original Bill: {philhealth_patient.get_bill_amount()}")
print(f"Final Bill: {philhealth_patient.calculate_bill()}")
