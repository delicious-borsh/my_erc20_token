from brownie import Contract, config
from brownie import network, accounts

DECIMALS = 8
STARTING_PRICE = 2000000000

LOCAL_ENVIRONMENTS = ["development", "Ganache-PsinaX"]
FORK_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]


def is_local_environment():
    return network.show_active() in LOCAL_ENVIRONMENTS


def is_fork_environment():
    return network.show_active() in FORK_ENVIRONMENTS


def get_account(index=None):
    if index:
        return accounts[index]
    if is_local_environment() or is_fork_environment():
        return accounts[0]
    else:
        return accounts.load(filename="kekaccount")
