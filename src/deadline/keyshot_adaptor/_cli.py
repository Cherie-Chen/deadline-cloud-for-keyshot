"""Console-script shim for the deprecated ``deadline-cloud-for-keyshot`` PyPI
package.

This module exposes two entry points (``KeyShotAdaptor`` and
``keyshot-openjd``) that print a deprecation notice to stderr and exit with a
non-zero status. It replaces the real adaptor CLIs that used to ship with
0.4.3 so that:

* customer scripts that still invoke either binary do not silently no-op;
* the failure message tells them exactly what to do next.

The message text is deliberately identical to the ``DeprecationWarning`` raised
on ``import deadline.keyshot_adaptor`` so both channels give the same guidance.
"""

import sys

_MESSAGE = (
    "The 'deadline-cloud-for-keyshot' PyPI package is deprecated. "
    "AWS Deadline Cloud for KeyShot is now delivered by the shared "
    "Deadline Cloud submitter installer; a separate PyPI adaptor package "
    "is no longer required. Uninstall this package and follow the AWS "
    "Deadline Cloud User Guide: "
    "https://docs.aws.amazon.com/deadline-cloud/latest/userguide/submitter.html"
)


def main() -> int:
    """Entry-point body for the KeyShot console scripts.

    Prints the deprecation notice to stderr and returns a non-zero exit
    code. Any command-line arguments are ignored.
    """
    print(_MESSAGE, file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
