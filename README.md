# CSV to JSON Converter with Logging Decorator

A Python script that reads a CSV file, converts it to JSON, and logs every
function call using a custom decorator.

## Features

- Reads any CSV file into a list of dictionaries
- Converts and writes the data to a JSON file
- Custom `@log_call` decorator that logs:
  - Function name and arguments called
  - Execution time for each call

## Files

- `csv_to_json.py` — main script
- `WineQT.csv` — input dataset (Wine Quality dataset, 1143 rows)
- `WineQT.json` — generated output (created after running the script)

## How it works

The `log_call` decorator wraps `read_csv()` and `convert_to_json()`. Each
time one of these functions is called, the decorator prints:

```
[LOG] Calling read_csv('WineQT.csv')
[LOG] read_csv finished in 0.0138s
[LOG] Calling convert_to_json([...], 'WineQT.json')
[LOG] convert_to_json finished in 0.0021s
```

## Usage

1. Place `WineQT.csv` in the same folder as `csv_to_json.py`
2. Run:
   ```bash
   python csv_to_json.py
   ```
3. Output is saved as `WineQT.json` in the same folder

## Example decorator

```python
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}(...)")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[LOG] {func.__name__} finished in {elapsed:.4f}s")
        return result
    return wrapper
```
