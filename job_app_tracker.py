import csv

all_jobs = []

def save_to_csv(jobs_list):
    with open('applications.csv', mode='w', newline='') as file:
        column_headers = ["company", "role", "salary"]
        writer = csv.DictWriter(file, fieldnames=column_headers)
        
        writer.writeheader()
        writer.writerows(jobs_list)
        
    print("\nSuccess: All jobs have been saved to applications.csv!")

def main_menu():
     while True: 
        company_name = input("Enter the company name: ")
        job_role = input("Enter the role you are applying for: ")
        salary_offered = int(input("Enter the salary offered (in INR): "))

        print("\n--- JOB SUMMARY ---")
        print(f"Target: {job_role} at {company_name}")
        print(f"Compensation: ₹{salary_offered}")

        if  salary_offered >= 500000:
             print("Status: High Priority Application")
        else:
             print("Status: Standard Priority")
        job_entry = {
                    "company": company_name,
                    "role": job_role,
                    "salary": salary_offered
                    }
        all_jobs.append(job_entry)
        
        keep_going = input("Do you want to run this again? (yes/no): ")
        if keep_going == 'no':
              break
main_menu()
print("\n--- ALL SAVED JOBS ---")
print(all_jobs)
save_to_csv(all_jobs)
