import json
from collections import Counter
from pathlib import Path

LOG_FILE = Path("/home/ubuntu/cowrie/var/log/cowrie/cowrie.json")

source_ips = Counter()
usernames = Counter()
commands = Counter()
event_types = Counter()

with LOG_FILE.open("r", encoding="utf-8") as log:
    for line in log:
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue

        event_id = event.get("eventid")
        src_ip = event.get("src_ip")
        username = event.get("username")
        command = event.get("input")

        if event_id:
            event_types[event_id] += 1

        if src_ip:
            source_ips[src_ip] += 1

        if username:
            usernames[username] += 1

        if event_id == "cowrie.command.input" and command:
            commands[command] += 1


def print_top(title, counter, limit=10):
    print(f"\n{title}")
    print("-" * len(title))

    for value, count in counter.most_common(limit):
        print(f"{value:<35} {count}")


print_top("Event Types", event_types)
print_top("Top Source IPs", source_ips)
print_top("Top Usernames", usernames)
print_top("Top Commands", commands)
