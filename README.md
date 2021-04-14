# Minimize

Minimize is a command line utility for optimizing the size of MicroPython projects, allowing you to write clean and
readable code occupying minimal memory when deployed to micro-controller

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install minimize.

```bash
pip install python-minimize
```

## Usage

Minimize provides a simple command-line utility which runs size reduction recursively over all files under the working directory

```bash
minimize
```

The command also accepts an arbitrary number of glob patterns, enabling fine-grained control over which files are minimized

```bash
minimize big-files/**.py huge-files/**.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

A full [contribution guide](CONTRIBUTING.md) and [code of conduct](CODE_OF_CONDUCT.md) are supplied with the repository. In essence, update the unit tests and changelog, and treat fellow users with respect!


## License
[Apache Software License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
