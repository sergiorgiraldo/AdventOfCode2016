# Advent of Code 2016 Python

My solutions to [Advent of Code 2016](https://adventofcode.com/2016) done in Python

## Performance

![](https://img.shields.io/badge/day%20📅-24-blue)
 
![](https://img.shields.io/badge/stars%20⭐-30-yellow)

---

# Based on @xavdid's Python Advent of Code Project Template

## Commands

### `./deploy.sh [day]`

### `./start`

#### Usage

> `./start [-h] [--year YEAR] [day]`

Scaffold files to start a new Advent of Code solution

**positional arguments**:

- `day` (optional): Which puzzle day to start, between `[1,25]`. Defaults to the next day _without_ a folder (matching `day_NN`) in the specified year.

**optional arguments**:

- `-h, --help` (optional): show this help message and exit
- `--year YEAR` (optional): Puzzle year. Defaults to current year if December has begun, otherwise previous year.

#### Examples

- `./start`
- `./start 2`
- `./start 3 --year 2019`

