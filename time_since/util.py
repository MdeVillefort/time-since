import os
import datetime
from dataclasses import dataclass

from time_since import HERE

@dataclass
class Delta:
    days: int
    hours: int
    minutes: int
    seconds: int
    
    def __str__(self):
        return f"Days: {self.days}; Hours: {self.hours:02}; Minutes: {self.minutes:02}; Seconds: {self.seconds:02}"

def read_time(datetime_file: str = os.path.join(HERE, "datetime.txt")) -> datetime.datetime:
    """Reads iso-formatted time string from file"""
    with open(datetime_file) as f:
        start = datetime.datetime.fromisoformat(f.read().strip())
    return start

def calculate_delta(start: datetime.datetime) -> Delta:
    """Calculates time elapsed since start and returns a Delta"""
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    delta = now - start
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return Delta(days, hours, minutes, seconds)
