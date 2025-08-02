import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('my_record.db')
cursor = conn.cursor()

# Drop old table for clean start
cursor.execute('DROP TABLE IF EXISTS my_record')

# Create table with composite primary key
cursor.execute('''
    CREATE TABLE my_record (
        Enrollment INTEGER,
        name TEXT NOT NULL,
        Subject TEXT NOT NULL,
        Mark INTEGER NOT NULL,
        PRIMARY KEY (Enrollment, Subject)
    )
''')
conn.commit()

# Updated Student records for Abhinay
my_record = [
    (92400133174, 'Abhinay', 'PWP', 98),
    (92400133174, 'Abhinay', 'ICE', 95),
    (92400133174, 'Abhinay', 'DMGT', 92),
    (92400133174, 'Abhinay', 'DSC', 89),
    (92400133174, 'Abhinay', 'SS', 86),
    (92400133174, 'Abhinay', 'COA', 84)
]
cursor.executemany('''
    INSERT INTO my_record (Enrollment, name, Subject, Mark) 
    VALUES (?, ?, ?, ?)
''', my_record)
conn.commit()

# Fetch all records
cursor.execute('SELECT * FROM my_record')
rows = cursor.fetchall()
print("All Student Subjects Records:")
for row in rows:
    print(row)

# Subjects with Marks > 90
cursor.execute('SELECT name, Subject, Mark FROM my_record WHERE Mark > 90')
high_marks = cursor.fetchall()
print("\nSubjects with Marks greater than 90:")
for subject in high_marks:
    print(subject)

# Update Mark for COA
cursor.execute('''
    UPDATE my_record 
    SET Mark = 98 
    WHERE Enrollment = 92400133174 AND Subject = 'COA'
''')
conn.commit()

# Verify the update
cursor.execute('''
    SELECT Subject, Mark FROM my_record 
    WHERE Enrollment = 92400133174 AND Subject = 'COA'
''')
updated = cursor.fetchone()
print(f"\nUpdated Mark for COA: {updated[1]}")

# Delete marks for 'SS' subject
cursor.execute('''
    DELETE FROM my_record 
    WHERE Enrollment = 92400133174 AND Subject = 'SS'
''')
conn.commit()

# Verify deletion
cursor.execute('''
    SELECT * FROM my_record 
    WHERE Enrollment = 92400133174 AND Subject = 'SS'
''')
deleted = cursor.fetchone()
if deleted is None:
    print("\n' SS ' subject record has been successfully deleted")

# Calculate the average Mark
cursor.execute('''SELECT AVG(Mark) FROM my_record''')
avg_mark = cursor.fetchone()[0]

print(f"\nThe average mark of students is: {avg_mark:.2f}")

# Close the connection
conn.close()
