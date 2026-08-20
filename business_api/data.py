HALLS = [
    {
        "id": "H001",
        "name": "Grand Ballroom",
        "capacity": 500,
        "event_types": ["Wedding", "Corporate", "Conference"],
        "parking_spaces": 200,
        "air_conditioned": True,
        "description": "A large elegant ballroom suitable for weddings and corporate events."
    },
    {
        "id": "H002",
        "name": "Royal Hall",
        "capacity": 300,
        "event_types": ["Wedding", "Birthday", "Corporate"],
        "parking_spaces": 120,
        "air_conditioned": True,
        "description": "A premium hall suitable for medium-sized events."
    },
    {
        "id": "H003",
        "name": "Garden Hall",
        "capacity": 150,
        "event_types": ["Wedding", "Birthday", "Outdoor Event"],
        "parking_spaces": 80,
        "air_conditioned": False,
        "description": "An outdoor-style venue suitable for intimate events."
    }
]


STAFF = [
    {
        "id": "EMP001",
        "name": "Kasun Perera",
        "role": "Events Manager",
        "department": "Events",
        "email": "kasun@example.com"
    },
    {
        "id": "EMP002",
        "name": "Nimali Fernando",
        "role": "Sales Executive",
        "department": "Sales",
        "email": "nimali@example.com"
    },
    {
        "id": "EMP003",
        "name": "Ravindu Silva",
        "role": "Operations Manager",
        "department": "Operations",
        "email": "ravindu@example.com"
    }
]


LEAVE_BALANCES = {
    "EMP001": {
        "annual_leave": 14,
        "used_annual_leave": 5,
        "remaining_annual_leave": 9,
        "casual_leave": 7,
        "used_casual_leave": 2,
        "remaining_casual_leave": 5
    },
    "EMP002": {
        "annual_leave": 14,
        "used_annual_leave": 8,
        "remaining_annual_leave": 6,
        "casual_leave": 7,
        "used_casual_leave": 3,
        "remaining_casual_leave": 4
    },
    "EMP003": {
        "annual_leave": 21,
        "used_annual_leave": 10,
        "remaining_annual_leave": 11,
        "casual_leave": 7,
        "used_casual_leave": 1,
        "remaining_casual_leave": 6
    }
}


APPOINTMENTS = [
    {
        "id": "APT001",
        "staff_id": "EMP001",
        "date": "2026-09-15",
        "time": "10:00",
        "customer_name": "Amal Perera"
    },
    {
        "id": "APT002",
        "staff_id": "EMP002",
        "date": "2026-09-15",
        "time": "14:00",
        "customer_name": "Nadeesha Silva"
    }
]


INQUIRIES = []