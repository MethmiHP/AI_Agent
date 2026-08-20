from fastapi import FastAPI, HTTPException

from business_api.data import (
    HALLS,
    STAFF,
    LEAVE_BALANCES,
    APPOINTMENTS,
    INQUIRIES
)

from business_api.schemas import (
    InquiryCreate,
    AppointmentCreate
)


app = FastAPI(
    title="EventOps Business API",
    description="Internal business API for EventOps AI",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "EventOps Business API is running"
    }


@app.get("/api/halls")
def get_halls():
    return HALLS


@app.get("/api/halls/{hall_id}")
def get_hall(hall_id: str):

    for hall in HALLS:
        if hall["id"] == hall_id:
            return hall

    raise HTTPException(
        status_code=404,
        detail="Hall not found"
    )


@app.get("/api/halls/{hall_id}/availability")
def check_hall_availability(
    hall_id: str,
    date: str
):

    hall = next(
        (hall for hall in HALLS if hall["id"] == hall_id),
        None
    )

    if not hall:
        raise HTTPException(
            status_code=404,
            detail="Hall not found"
        )

    return {
        "hall_id": hall_id,
        "hall_name": hall["name"],
        "date": date,
        "available": True
    }


@app.get("/api/staff")
def get_staff():
    return STAFF


@app.get("/api/staff/{staff_id}")
def get_staff_member(staff_id: str):

    staff = next(
        (person for person in STAFF if person["id"] == staff_id),
        None
    )

    if not staff:
        raise HTTPException(
            status_code=404,
            detail="Staff member not found"
        )

    return staff


@app.get("/api/staff/{staff_id}/leave")
def get_leave_balance(staff_id: str):

    if staff_id not in LEAVE_BALANCES:
        raise HTTPException(
            status_code=404,
            detail="Leave information not found"
        )

    return {
        "employee_id": staff_id,
        **LEAVE_BALANCES[staff_id]
    }


@app.post("/api/inquiries")
def create_inquiry(inquiry: InquiryCreate):

    new_inquiry = {
        "id": f"INQ{len(INQUIRIES) + 1:03d}",
        **inquiry.model_dump()
    }

    INQUIRIES.append(new_inquiry)

    return {
        "message": "Inquiry created successfully",
        "inquiry": new_inquiry
    }


@app.get("/api/appointments")
def get_appointments():

    return APPOINTMENTS


@app.post("/api/appointments")
def create_appointment(
    appointment: AppointmentCreate
):

    new_appointment = {
        "id": f"APT{len(APPOINTMENTS) + 1:03d}",
        **appointment.model_dump()
    }

    APPOINTMENTS.append(new_appointment)

    return {
        "message": "Appointment booked successfully",
        "appointment": new_appointment
    }