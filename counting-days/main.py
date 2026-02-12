import sys
from datetime import timedelta

from .display_events import display_events
from .get_events import read_events_from_file

if __name__ == "__main__":
    if len(sys.argv) > 1:
        events = read_events_from_file(sys.argv[1])
    else:
        print("Usage: python main.py <events_file>")
        sys.exit(1)
    events.sort(
        key=lambda e: (
            e.tdelta if e.tdelta.days != 0 else timedelta.min,
            e.title,
        )
    )
    display_events(events)
