# todo-app

A small command-line to-do list in pure Python. Tasks are saved to a plain text
file so they survive after the program closes.

No frameworks, no external libraries, no AI — just the standard language.

## Why this exists

This is a learning project. The goal was to build something real using only
concepts I'd actually studied: functions, loops, conditionals, dictionaries,
lists, string methods, and file handling.

## Status

🚧 **Work in progress.**

| Function | State |
|---|---|
| `show_tasks(tasks)` | ✅ Working |
| `save_tasks(tasks, filename)` | ✅ Working |
| `load_tasks(filename)` | 🔧 In progress |
| Interactive menu | ⬜ Not started |

## How it stores data

One task per line in `tasks.txt`, status and title separated by a pipe:

```
0|قرا Python
1|شري الخبز
```

`0` = not done, `1` = done. The file is written with `encoding="utf-8"` so
non-Latin titles are preserved.

`tasks.txt` is gitignored — it's personal data, not part of the program.

## Running it

```bash
python todo.py
```

Requires Python 3.12 or newer.

## Author

Bouraq Abdelwahab — [@abbq14](https://github.com/abbq14)
