import datetime as dt

def age_from_dob():
    while True:
        dob_str = input("Enter you date of birth (DD-MM-YYYY or YYYY/MM/DD): ")

        formats =   [
                    "%Y-%m-%d", "%d-%m-%Y",
                    "%Y/%m/%d", "%d/%m/%Y",
                    "%d.%m.%Y", "%Y.%m.%d",
                    "%d:%m:%Y", "%Y:%m:%d"
                    ]

        dob = None
        for f in formats:           
            try:
                dob = dt.datetime.strptime(dob_str, f).date()
                break
            except ValueError:
                continue

        if dob is None:
            print("Invalid format. Try again with a proper date.\n")
            continue
        
        today = dt.date.today()
                
        if dob > today:
            print("Date of birth can't be in the future. Try Again.\n")
            continue

        years = today.year - dob.year
        months = today.month - dob.month 
        days = today.day - dob.day

        if days < 0:
            months -= 1

        if months < 0:
            years -= 1
            months += 12

        print(f"You are {years} years and {months} months old.")
        break
        
age_from_dob()



