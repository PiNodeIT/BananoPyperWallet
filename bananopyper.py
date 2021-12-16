print("IT IS HIGHLY RECOMMENDED TO USE THIS SCRIPT OFFLINE")
input("Press Enter to continue...")

from nanolib import generate_seed
from nanolib import generate_account_id

nwall = int(input("How many wallet i must generate? :\n"))
name = input("Save as (no extension) :\n")
for _ in range(nwall):
    seed = generate_seed()
    account_id = generate_account_id(seed, 0)
    address = account_id.replace("xrb_", "ban_")
    f = open((name)+".txt", 'a')
    f.write("seed: "+(seed)+", Address: "+(address)+("\n"))
