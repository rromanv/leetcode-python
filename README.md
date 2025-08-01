# LeetCode Python Solutions

This repository contains Python solutions for LeetCode problems, organized by problem number.

## Problems

| Problem | Solution | Tests | Difficulty |
|---------|----------|-------|------------|
| [1. Two Sum](https://leetcode.com/problems/two-sum/) | [problem_1.py](problems/problem_1.py) | [test_1.py](tests/test_1.py) | ![Easy](https://img.shields.io/badge/-Easy-green) |
| [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [problem_9.py](problems/problem_9.py) | [test_9.py](tests/test_9.py) | ![Easy](https://img.shields.io/badge/-Easy-green) |
| [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [problem_20.py](problems/problem_20.py) | [test_20.py](tests/test_20.py) | ![Easy](https://img.shields.io/badge/-Easy-green) |
| [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | [problem_49.py](problems/problem_49.py) | [test_49.py](tests/test_49.py) | ![Medium](https://img.shields.io/badge/-Medium-orange) |
| [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | [problem_56.py](problems/problem_56.py) | [test_56.py](tests/test_56.py) | ![Medium](https://img.shields.io/badge/-Medium-orange) |
| [3136. Valid Word](https://leetcode.com/problems/valid-word/) | [problem_3136.py](problems/problem_3136.py) | [test_3136.py](tests/test_3136.py) | ![Easy](https://img.shields.io/badge/-Easy-green) |


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