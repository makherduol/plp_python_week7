plp-python-week7/
│
├── list_warmup.py
├── shopping_list.py
├── list_report.py
├── screenshots/
│   ├── warmup_output.png
│   ├── shopping_list_session.png
│   └── report_output.png
└── README.md


# PLP Python Week 7 Assignment: Shopping List Manager

- **list_warmup.py**: Demonstrates basic list creation, indexing, appending, removing, and length checking.
- **shopping_list.py**: An interactive console application allowing users to add, remove, view, and exit a shopping list session safely.
- **list_report.py**: Generates a numbered list report, counts items with names longer than four letters, and evaluates the longest item name.

### Why is it safer to check `in` before calling `.remove()`?
Checking if an item exists in the list using the `in` keyword prevents the program from throwing a `ValueError` crash when attempting to remove an element that isn't present. It ensures a smoother, more predictable user experience by gracefully handling missing entries.
