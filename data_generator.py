from faker import Faker
fake = Faker()

for a in range(100):
    a = {
    'name': fake.name(),
    'job':fake.job(),
    'phone_number':fake.phone_number(),
    'address':fake.address(),
    'card_number':fake.credit_card_number(),
    'card_provider':fake.credit_card_provider()
    }
    print(a)