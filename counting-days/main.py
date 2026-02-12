import sys
from datetime import timedelta

from .display_events import list_events, notify_events
from .get_events import read_events_from_file

if __name__ == "__main__":
    if len(sys.argv) > 1:
        events = read_events_from_file(sys.argv[1])
    else:
        print("Usage: python main.py <events_file>")
        sys.exit(1)

    events.sort(
        key=lambda e: (
            e.tdelta,
            e.title,
        ),
        reverse=True,
    )
    notify_events(events)
    list_events(events)
