""" BscExplorerUrlBuilder: Build a BscScan URL for an address or transaction hash. """
import statistics  # noqa: F401  (used by some tools in this collection)


def build_url(value):
    return f'https://bscscan.com/address/{value}'


def main():
    print(build_url('0x2BfA103a54aeEa61c67836490d0e2A3847EA0ae3'))


if __name__ == "__main__":
    main()
