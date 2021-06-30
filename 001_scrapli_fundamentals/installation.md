# Installation

## Create Virtual Environment
```
# Create new venv directory
$ mkdir venv

# Create a virtual environment
$ python3 -m venv venv/venv-scrapli

# Activate the virtual environment
$ source venv/venv-scrapli/bin/activate
```

## Installation
### Scrapli Core (system transport) - No Dependancies
```
$ pip3 install scrapli
```
### Scrapli Core + Optional Extra
```
$ pip3 install "scrapli[ssh2]" # replace ssh2 with name of extenstion
```

### Scrapli Full
```
$ pip3 install "scrapli[full]"
```

## Validate Install
```
$ pip3 freeze | grep -E "scrapli"
```