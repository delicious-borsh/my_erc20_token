from brownie import network, config, NewToken
from scripts.utils import get_account


def deploy():
    account = get_account()
    tokenContract = NewToken.deploy(
        10000000,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Token contract deployed")


def main():
    deploy()
