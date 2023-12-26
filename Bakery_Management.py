import pandas as pd

class BakeryManagementSystem:
    def __init__(self):
        self.customers= pd.DataFrame(columns=['Customer ID','Name','Contact Number','Email'])
    
    def add_customer(self,name,contact_number,email):
        customer_id= len(self.customers)+1
        new_customer=pd.Series({'Customer ID': customer_id,
                                'Name': name,
                                'Contact Number': contact_number,
                                'Email': email})
        self.customers=self.customers.append(new_customer, ignore_index=True)
        print(f"Customer added successfully. Customer id is {customer_id}")
        
    def export_to_excel(self, filename='bakery_customers.xlsx'):
        try:
           self.customers.to_excel(filename, index=False) 
           print(f"Data exported to {filename} successfully.")
        except Exception as e:
            print(f"Error exporting data to excel: {e}.")
            
def main():
    bakery_system= BakeryManagementSystem()
    
    while True:
        
        print("\n Bakery Management System Menu : ")
        print("1. Add Customer")
        print("2. Export Data to Excel")
        print("3. Exit")
        
        Choice= input("Enter your choice (1/2/3): ")
        
        if Choice=='1':
            name=input("Enter customer name: ")
            contact_number=input("Enter contact number: ")
            email= input("Enter the email: ")
            bakery_system.add_customer(name, contact_number, email)
            
        elif Choice=='2':
            filename= input("Enter filename for export: ").strip()
            if not filename:
                filename='bakery_customers.xlsx'
            bakery_system.export_to_excel(filename)
            
        elif Choice=='3':
            print("Exiting bakery management system. ")
            break
          
        else:
            print("Invalid choice. Please enter 1, 2 or 3. ")
            
if __name__=="__main__":
    main()