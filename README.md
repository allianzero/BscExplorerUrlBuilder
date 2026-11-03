# BscExplorerUrlBuilder

Build a BscScan URL for an address or transaction hash.

## Features

- Small, dependency-free Python tool (standard library only).
- Pure function in `main.py` that is easy to import and reuse.
- Runnable example: `python main.py`.
- Unit test in `test_main.py`.

## Installation

Requires Python 3.10 or newer. No third-party dependencies.

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Example:

```python
from main import build_url

result = build_url('0x2BfA103a54aeEa61c67836490d0e2A3847EA0ae3')
print(result)
```

## Safety

This tool performs local calculations only. It never sends funds, never
stores a seed phrase or private key, and never makes network requests.
Validators in this collection check format only; never paste a real
seed phrase or private key into any tool you do not fully trust.

## License

BSD-3-Clause — see `LICENSE`.
