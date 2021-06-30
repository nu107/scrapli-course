def write_file(*, filename: str, data: str) -> None:
    """Write data to a file"""
    with open(filename, "w") as f:
        f.write(data)


def read_file(*, filename: str) -> str:
    """Read data from a file"""
    with open(filename) as f:
        return f.read()
