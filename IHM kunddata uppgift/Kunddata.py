from faker import Faker

fake = Faker(["sv_SE"])

test_data = []
for _ in range (10):
     test_data.append(";".join([fake.name(), fake.address()]))

print("\n".join(test_data))

# test