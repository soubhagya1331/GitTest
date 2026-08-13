# Project Library: shared/dummy_utils.py

def get_project_info():
    """Return basic project information."""
    return {
        "name": "DemoIgnitionProject",
        "version": "1.0.0",
        "environment": "testing"
    }


def calculate_total(values):
    """Calculate the total of a list of numbers."""
    if not values:
        return 0

    return sum(values)


def format_message(username, message):
    """Create a formatted message."""
    return "[{}] {}".format(username, message)


def get_machine_status(machine_name):
    """Return a dummy machine status."""
    machines = {
        "Machine-01": "RUNNINrewgG",
        "Machine-02": "STOPPED",
        "Machine-03": "FAULT"
    }

    return machines.get(machine_name, "UNKNOWN")


def test_function():
    """Simple test function."""
    project = get_project_info()
    total = calculate_total([10, 20, 30])
    message = format_message("admin", "Ignition project test")
    status = get_machine_status("Machine-01")

    return {
        "project": project,
        "total": total,
        "message": message,
        "machine_status": status
    }
    
def calculate_average(values):
    if not values:
        return 0

    return sum(values) / len(values)