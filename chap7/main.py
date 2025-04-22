def admit_card(name, roll_num, center, time, day):

    """ Generate Admit car throgh function"""

    card = f"""
========================
GIAIC Admit Card
========================
Name: {name}
Roll number: {roll_num}
Center: {center}
Time: {time}
Day: {day}
=======================
Instructions:
=======================
1. Please arrives at least fifteen minute early
2. Bring your ID card for verification
"""
    return card

id_card = admit_card("Huzaif", 89470, "G-House", "9am to 12pm", "Friday")
print(id_card)