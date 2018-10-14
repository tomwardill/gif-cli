# GIF-CLI

A tool for searching [giphy](giphy.com) from the cli, returning a random
result from the first page of results.

## Installation

The easiest method of installing `gif-cli` on Ubuntu or other systems that
support [snapd](snapcraft.com) is to use it.

### Snap installation

```bash
snap install gif-cli
gif-cli
```

### Source installation

The project is not currently released on pypi, as such the only other
supported method of installation is via a python3 virtualenv.

```bash
virtualenv -p python3 env
env/bin/python3 setup.py install
env/bin/gif-cli
```

## Usage

Run the app with any number of search terms.

```bash
gif-cli alpaca
```

## Notes

The giphy search is otherwise performed with the default parameters, as such
the age rating defaults to 'g'.
