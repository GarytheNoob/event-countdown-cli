import argparse
import sys

from .config import read_config
from .display_events import filter_events, list_events, notify_events
from .event import Event
from .get_events import read_events_from_file


def handle_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Event notifier and lister")
    parser.add_argument("events_file", help="Path to the events file")
    parser.add_argument(
        "-n",
        "--notify",
        action="store_true",
        help="Notify events. If not set, events will be listed instead.",
    )

    parser.add_argument(
        "--dev-today", help="Override today's date (YYYY-MM-DD)"
    )
    return parser.parse_args()


def load_events_with_args(args: argparse.Namespace) -> list[Event]:
    loaded_events = read_events_from_file(args.events_file)
    if args.dev_today:
        from datetime import datetime

        try:
            dev_today = datetime.fromisoformat(args.dev_today).date()
        except ValueError:
            print(
                f"Invalid date format for --dev-today: {args.dev_today}\n"
                "Expected format: YYYY-MM-DD"
            )
            sys.exit(1)
        for e in loaded_events:
            e.checkin(today=dev_today)
    return loaded_events


def main():
    config = read_config()
    args = handle_args()

    # NOTE: events are loaded from args, not config, currently.
    # TODO: read events from config if no events file is provided in args
    events = load_events_with_args(args)
    shortlisted_events = filter_events(events, config.option)
    if args.notify:
        notify_events(shortlisted_events)
    else:
        list_events(shortlisted_events)


if __name__ == "__main__":
    main()
