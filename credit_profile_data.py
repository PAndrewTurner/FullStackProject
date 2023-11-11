import random
import csv

class FinancialData:
    def education_level(self, credit_score):
        # determine education level based on credit score
        if credit_score > 700:
            return random.choice(['Bachelor', 'Master', 'PhD'])
        elif credit_score > 600:
            return random.choice(['High School', 'College'])
        else:
            return 'High School'

    def self_employed(self):
        return random.choice(['Yes', 'No'])

    def annual_income(self, credit_score):
        # generate random annual income based on credit score
        if credit_score > 700:
            return random.randint(50000, 200000)
        elif credit_score > 600:
            return random.randint(30000, 100000)
        else:
            return random.randint(10000, 50000)

    def loan_amount(self, credit_score):
        return random.randint(10000, 300000)

    def credit_score(self):
        return random.randint(300, 850)

    
    def assets(self, credit_score):
        # generate asset values based on credit score
        if credit_score > 700:
            real_estate = random.randint(50000, 500000)
            commercial = random.randint(10000, 200000)
            bank = random.randint(5000, 150000)
        elif credit_score > 600:
            real_estate = random.randint(20000, 200000)
            commercial = random.randint(5000, 100000)
            bank = random.randint(2000, 50000)
        else:
            real_estate = random.randint(0, 100000)
            commercial = 0
            bank = random.randint(0, 20000)

        total_asset = real_estate + commercial + bank

        # if total assets exceed 1 million, scale down proportionally
        if total_asset > 1000000:
            scale_factor = 1000000 / total_asset
            real_estate = int(real_estate * scale_factor)
            commercial = int(commercial * scale_factor)
            bank = int(bank * scale_factor)
            total_asset = real_estate + commercial + bank

        return real_estate, commercial, bank, total_asset

# generate data for 20 users
users = []
financial_data_generator = FinancialData()
for _ in range(20):
    credit_score = financial_data_generator.credit_score()
    real_estate, commercial, bank, total_asset = financial_data_generator.assets(credit_score)
    user = {
        'number_of_dependents': random.randint(0, 5),
        'education': financial_data_generator.education_level(credit_score),
        'self_employed': financial_data_generator.self_employed(),
        'annual_income': financial_data_generator.annual_income(credit_score),
        'loan_amount': financial_data_generator.loan_amount(credit_score),
        'credit_score': credit_score,
        'real_estate_asset': real_estate,
        'commercial_asset': commercial,
        'bank_asset': bank,
        'total_asset': total_asset
    }
    users.append(user)

    
# print
for user in users:
    print(user)
# export as csv file
filename = "user_financial_data.csv"

# open the file in write mode
with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=users[0].keys())

    # Write the header (field names)
    writer.writeheader()

    # Write the user data
    for user in users:
        writer.writerow(user)
