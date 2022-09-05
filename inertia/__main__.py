""" Placeholder for additional command line flags. """
from playwright.__main__ import main as pw_main


def main() -> int:
    """
    Entrypoint for binary acquisition (if desired).  This is a wrapper around playwrights binary
    acquisition with some additional functionality.
    :return:
    """
    pw_main()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
