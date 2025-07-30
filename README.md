# LeetCode Python Solutions

This repository contains Python solutions for LeetCode problems, organized by problem number.

## Problems

| # | Title | Difficulty | Status | Solution |
|---|-------|------------|--------|----------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | 🔴 Not Implemented | [Solution](problems/1.py) |

## Legend

- 🔴 Not Implemented - Shell function created, solution pending
- 🟡 In Progress - Solution being worked on
- 🟢 Completed - Solution implemented and tested

## Project Structure

```
leetcode-python/
├── problems/          # Problem solutions
│   ├── __init__.py
│   └── 1.py          # Two Sum
├── tests/            # Test files
│   └── test_1.py     # Tests for Two Sum
└── README.md         # This file
```

## Running Tests

To run tests for a specific problem:

```bash
pytest tests/test_1.py -v
```

To run all tests:

```bash
pytest tests/ -v
```

## Contributing

1. Create a new problem file in the `problems/` directory
2. Create corresponding tests in the `tests/` directory
3. Update this README with the new problem entry
4. Follow the coding guidelines in the workspace rules 