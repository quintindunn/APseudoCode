"""
Author: Quintin Dunn
Date: 1/9/24
"""
import metadata


def version() -> str:
    """
    Returns the version of the CSP interpreter for the CLI.
    :return: str of version of the CSP interpreter
    """

    return f"CSP V{metadata.VERSION_S}"


if __name__ == '__main__':
    import argparse

    args = argparse.ArgumentParser()
    args.add_argument("-V", "--version", help="Prints out the current version of the CSP interpreter.",
                      action="store_true")

    args = args.parse_args()

    if args.version:
        print(version())
        exit()