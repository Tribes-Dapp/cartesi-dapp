"""
Code for the Tribe Contract generator
"""

PROXY_ADDR = ''
CONTRACT_BYTECODE = ''


def _set_bytecode(bytecode: bytes):
    """Set the current bytecode for new Tribe contracts

    Parameters
    ----------
    bytecode : bytes
        Tribe bytecode
    """
    global CONTRACT_BYTECODE
    CONTRACT_BYTECODE = bytecode


def _set_proxy_addr(addr: str):
    """Set the current proxy address for deploying new contracts

    Parameters
    ----------
    addr : str
        New address for proxy contract
    """
    global PROXY_ADDR
    PROXY_ADDR = addr


def get_tribe_bytecode() -> bytes:
    """Generate and return the bytecode for the new Tribe Contract to be
    deployed

    Returns
    -------
    bytes
        The compiled bytecode for the new contract
    """
    # Currently only return the current cached bytecode. In the future, this
    # can be used to create files from templates and compile the contract with
    # specific needs
    return CONTRACT_BYTECODE
