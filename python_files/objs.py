# Python functions to return a object value (datetime, list, str, etc.)
from typing import Literal
from datetime import datetime
from python_files.constants import PARTICIPANTS, DATE_FORMAT, KEYPHRASES

MessageType = Literal["message", "file", "poll", "location"]


def get_participant(message: str) -> str | None:
    """
    Get the participant that sent a message.

    Args:
        message (str): The message to check.

    Returns:
        str: The participant that sent the message.
    """

    participant = list(filter(
        lambda participant: message.startswith(f"{participant}: "),
        PARTICIPANTS
    ))

    return participant[0] if participant else None


def get_datetime(date: str) -> datetime | None:
    """
    Get a datetime object from a string.

    Args:
        date (str): The string to convert.

    Returns:
        datetime: The datetime object.
    """

    try:
        return datetime.strptime(date, DATE_FORMAT)
    except ValueError:
        return None


def get_message_type(message: str) -> MessageType | None:
    """
    Get the type of message.

    Args:
        message (str): The message to check.

    Returns:
        MessageType: The type of message.
    """

    if message == KEYPHRASES["poll"]:
        return "poll"
    if message == KEYPHRASES["location"]:
        return "location"
    if message.endswith(KEYPHRASES["file"]):
        return "file"
    if message in (KEYPHRASES["delete"], KEYPHRASES["view_once"]):
        return None
    return "message"
