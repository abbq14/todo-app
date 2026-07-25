# todo-app

A small command-line to-do list in pure Python. Tasks are saved to a plain text
file so they survive after the program closes.

Built on the standard language, with [`rich`](https://github.com/Textualize/rich)
for a colored table interface.

## Why this exists

This is a learning project. The goal was to build something real using only
concepts I'd actually studied: functions, loops, conditionals, dictionaries,
lists, string methods, and file handling.

## Status

✅ **Working.**

| Feature | State |
|---|---|
| Show tasks (colored table) | ✅ Working |
| Add a task | ✅ Working |
| Mark a task done | ✅ Working |
| Save / load from file | ✅ Working |

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
pip install rich
python todo.py
```

Requires Python 3.12 or newer.

## Author

Bouraq Abdelwahab — [@abbq14](https://github.com/abbq14)
