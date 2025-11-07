mycur.execute('''create database yep;''')
mycur.execute('''use yep''')

mycur.execute('''
    create table medmgmt(
        Medicine_ID int(10) primary key,
        Medicine varchar(100),
        Manufacturer varchar(100),
        Date_of_Manufacture date,
        Date_of_Expiry date,
        Quantity int(10),
        Price int(10)
    )
''')

conn.commit()

sample_data = (
    (1, "Paracetamol", "PharmaCorp", "2023-01-01", "2025-01-01", 100, 5.50),
    (2, "Ibuprofen", "HealthMeds", "2022-12-10", "2025-06-10", 150, 10.00),
    (3, "Amoxicillin", "BioLife", "2023-03-15", "2025-09-15", 200, 15.75),
    (4, "Cetirizine", "WellnessPharm", "2023-07-01", "2024-07-01", 75, 7.20),
    (5, "Metformin", "GoodHealth", "2023-04-20", "2026-04-20", 120, 12.50),
    (6, "Atorvastatin", "VitalMeds", "2023-02-15", "2026-02-15", 50, 8.30),
    (7, "Aspirin", "MediCare", "2023-05-25", "2025-05-25", 90, 3.40),
)

sql = "insert into medmgmt values(%s,%s,%s,%s,%s,%s,%s);"
mycur.executemany(sql, sample_data)

# TABLE CREATED
