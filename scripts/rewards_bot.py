import click
from ape import project
from ape.cli import ConnectedProviderCommand, account_option


@click.command(cls=ConnectedProviderCommand)
@account_option()
def cli(account):
    account.set_autosign(enabled=True)

    contract = project.dependencies["nucypher-contracts"]["main"].TACoApplication.at(
        "0x329bc9Df0e45f360583374726ccaFF003264a136"
    )

    push_rewards = 100  # TODO: calculate the rewards to be pushed

    # contract.pushReward(100, sender=account)
