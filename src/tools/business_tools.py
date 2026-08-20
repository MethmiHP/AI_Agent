import requests


API_BASE_URL = "http://127.0.0.1:8000"


def get_halls():
    """Get all banquet halls available in the business."""

    print("🔧 TOOL CALLED: get_halls()")

    response = requests.get(
        f"{API_BASE_URL}/api/halls"
    )

    response.raise_for_status()

    return response.json()


def get_hall_details(hall_id: str):
    """Get detailed information about a specific banquet hall."""

    print(f"🔧 TOOL CALLED: get_hall_details(hall_id={hall_id})")

    response = requests.get(
        f"{API_BASE_URL}/api/halls/{hall_id}"
    )

    response.raise_for_status()

    return response.json()


def check_hall_availability(
    hall_id: str,
    date: str
):
    """Check whether a banquet hall is available on a specific date."""

    print(
        f"🔧 TOOL CALLED: "
        f"check_hall_availability(hall_id={hall_id}, date={date})"
    )

    response = requests.get(
        f"{API_BASE_URL}/api/halls/{hall_id}/availability",
        params={"date": date}
    )

    response.raise_for_status()

    return response.json()