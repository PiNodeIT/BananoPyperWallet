from nanolib import generate_seed
from nanolib import generate_account_id

seed = generate_seed()
account_id = generate_account_id(seed, 0)
address = account_id.replace("xrb", "ban")

print("Seed:", seed)
print("Address:", address)
