# Python functions that return boolean values
from datetime import datetime
from python_files.constants import PARTICIPANTS, DATE_FORMAT


def check_sent_by_participant(message: str) -> bool:
    """
    Check if a message was sent by a participant.

    Args:
        message (str): The message to check.

    Returns:
        bool: True if the message was sent by a participant, False otherwise.
    """
    participant = list(filter(
        lambda participant: message.startswith(f"{participant}: "),
        PARTICIPANTS
    ))

    return bool(participant)


def is_datetime(date: str) -> bool:
    """
    Check if a string is a valid datetime.

    Args:
        date (str): The string to check.

    Returns:
        bool: True if the string is a valid datetime, False otherwise.
    """
    try:
        datetime.strptime(date, DATE_FORMAT)
        return True
    except ValueError:
        return False

