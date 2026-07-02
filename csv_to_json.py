"""
CSV to JSON Converter with Call Logging
----------------------------------------
Reads WineQT.csv, converts it to JSON, and logs every function call
(name, arguments, and time taken) using a custom decorator.
"""

import csv
import json
import time
import functools


def log_call(func):
    """Decorator that logs the function name, arguments, and execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arg_str = ", ".join(
            [repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()]
        )
        print(f"[LOG] Calling {func.__name__}({arg_str})")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[LOG] {func.__name__} finished in {elapsed:.4f}s")
        return result
    return wrapper


@log_call
def read_csv(file_path):
    """Read a CSV file and return a list of dictionaries (one per row)."""
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


@log_call
def convert_to_json(data, output_path):
    """Write a list of dictionaries to a JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return output_path


def main():
    input_file = "WineQT.csv"
    output_file = "WineQT.json"

    rows = read_csv(input_file)
    convert_to_json(rows, output_file)

    print(f"\nDone. Converted {len(rows)} rows -> {output_file}")


if __name__ == "__main__":
    main()
