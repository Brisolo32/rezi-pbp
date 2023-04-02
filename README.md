# PBP-Rezi

A plugin for [PBP]() that gets data from Rezi

## How to use it:

**Command Line**: `Rezi-PBP "query" "cache location"`

**PBP**: Install the plugin and select it on the search page

## Building:

You will need:

- [Python 3](https://python.org)
- [Nuitka](https://github.com/Nuitka/Nuitka)

First, install the dependencies with `pip install -r requirements.txt`

Then, to build you run `nuitka3 --onefile --quiet --disable-console --output-filename=Rezi-PBP.exe main.py`. If you want it to be verbose then you can replace the `--quiet` flag with `--verbose`

## How it works:

It gets the most recent release from the [rezi-backend](https://github.com/Brisolo32/rezi-backend) repo, then it parses the csv and gets the games which contains the name in the query

## Why?:

This has been made to use with PBP although you can use it with another program since it outputs to an json file. I have not made Rezi.
