subjects = []

def add_subject(name, hours=0):
    subjects[name] = hours
    print(f"Added: {name} with {hours} hours")

add_subject("Python", 5)
add_subject("DSA", 10)
add_subject("Maths", 4)
print(subjects)