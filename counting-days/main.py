from datetime import datetime, timedelta
from typing import Any

from .event import Event
from .lang.en import DAYS_AFTER_STR, DAYS_BEFORE_STR, TODAY_STR

data: list[dict[str, str | bool]] = [
    {"fulldate": "2026-01-01", "title": "New Year's Day"},
    {"fulldate": "2026-02-03", "title": "Special"},
    {"fulldate": "2026-07-04", "title": "Independence Day"},
    {"fulldate": "2026-12-25", "title": "Christmas Day"},
    {"fulldate": "1998-09-30", "title": "My Birthday", "yearly": True},
]


def parse_data(events: list[dict[str, Any]]) -> list[Event]:
    today = datetime.now().date()
    enriched_events: list[Event] = []
    for e in events:
        date = datetime.fromisoformat(e["fulldate"]).date()
        title = e["title"]
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


def check_anniversary_since(event: Event) -> int:
    if event.tdelta.days >= 0 or event.yearly:
        return -1
    if (
        event.date.month == datetime.now().month
        and event.date.day == datetime.now().day
    ):
        years = datetime.now().year - event.date.year
        return years
    return -1


def check_hundreds_days_since(event: Event) -> int:
    if event.tdelta.days >= 0 or event.yearly:
        return -1
    if event.tdelta.days % 100 == 0:
        hundreds = abs(event.tdelta.days) // 100
        return hundreds
    return -1


def list_events(events: list[Event]) -> None:
    events.sort(
        key=lambda e: (
            e.tdelta if e.tdelta.days != 0 else timedelta.min,
            e.title,
        )
    )
    for event in events:
        if event.tdelta.days == 0:
            print(TODAY_STR.format(title=event.title))
        else:
            if event.tdelta.days < 0:
                print(
                    DAYS_AFTER_STR.format(
                        title=event.title, days=abs(event.tdelta.days)
                    )
                )
            else:
                print(
                    DAYS_BEFORE_STR.format(
                        title=event.title, days=event.tdelta.days
                    )
                )


def main() -> None:
    enriched_events = parse_data(data)
    list_events(enriched_events)


if __name__ == "__main__":
    main()
