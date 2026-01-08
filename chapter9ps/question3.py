# Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.
def generate_tables(num):
    tabel = ""
    for i in range(1, 11):
        tabel += f"{num} X {i} = {num*i}\n"

        with open(f"tables/table_of_{num}.txt","w") as file:
            file.write(tabel + "\n")

for i in range(2, 21):
    generate_tables(i)