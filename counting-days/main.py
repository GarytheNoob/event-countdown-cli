from datetime import datetime, timedelta
from typing import Any

from .event import Event

data: list[dict[str, str | bool]] = [
    {"fulldate": "2026-01-01", "event": "New Year's Day"},
    {"fulldate": "2026-02-03", "event": "Special"},
    {"fulldate": "2026-07-04", "event": "Independence Day"},
    {"fulldate": "2026-12-25", "event": "Christmas Day"},
    {"fulldate": "1998-09-30", "event": "My Birthday", "yearly": True},
]


def parse_data(events: list[dict[str, Any]]) -> list[Event]:
    today = datetime.now().date()
    enriched_events: list[Event] = []
    for e in events:
        date = datetime.fromisoformat(e["fulldate"]).date()
        title = e["event"]
        yearly = e.get("yearly", False)
        if yearly:
            date = date.replace(year=today.year)
            if date < today:
                date = date.replace(year=today.year + 1)
        tdelta = date - today
        enriched_events.append(
            Event(date=date, title=title, tdelta=tdelta, yearly=yearly)
        )
    return enriched_events


def list_events(events: list[Event]) -> None:
    events.sort(
        key=lambda e: (
            e.tdelta if e.tdelta.days != 0 else timedelta.min,
            e.title,
        )
    )
    for event in events:
        if event.tdelta.days == 0:
            print(f"    Today is {event.title}!")
        else:
            if event.tdelta.days < 0:
                print(f"Days after  {event.title:<20}: {-event.tdelta.days:>4}")
            else:
                print(f"Days before {event.title:<20}: {event.tdelta.days:>4}")


def main() -> None:
    enriched_events = parse_data(data)
    list_events(enriched_events)


if __name__ == "__main__":
    main()
