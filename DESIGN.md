# counting-days: a CLI/TUI app for displaying countdown and coutup to/from specific dates in terminal

## Features

### Backend

Accept both local and remote sources.

Both sources are in JSON format as below:

```json
[
    {
        "type": "tag",
        "name": "Friends' Birthdays",
        "color": "cyan",
        "content": [
            {
                "type": "event",
                "name": "Alice's Birthday",
                "date": "1990-05-15",
            },
            {
                "type": "event",
                "name": "Bob's Birthday",
                "date": "1988-11-22",
            }
        ]
    },
    {
        "type": "tag",
        "name": "Holidays",
        "color": "green",
        "content": [
            {
                "type": "event",
                "name": "New Year's Day",
                "date": "2024-01-01",
            },
            {
                "type": "event",
                "name": "Independence Day",
                "date": "2024-07-04",
            }
        ]
    }
]
```

### CLI

Can be run as a script, displaying the events if today is a relevant date.

Can be provided with parameters to query and list events.

Can be put on the top of a shell config and display countdowns/countups on 
terminal startup. For this usage, an optional cache can be used to avoid 
displaying the same content at every startup within a certain time 
frame(normally, a day).

### TUI

When executed, displays a terminal user interface with the following features:

- Lists all tags and their associated events.
- Color-coded tags based on the specified color.
- For each event, shows the number of days until or since the event date.
- Navigation through tags and events using keyboard inputs.
- Searching and filtering capabilities to quickly find specific events.
- Option to mark events as important or favorite.
- Ability to add, edit, or delete events directly from the TUI.

### Remarks

All the counting is based on local time, and is carried out during runtime.
