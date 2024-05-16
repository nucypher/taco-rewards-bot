import click
from ape import project, Contract
from ape.cli import ConnectedProviderCommand, account_option


@click.command(cls=ConnectedProviderCommand)
@account_option()
def cli(account):
    contract = project.dependencies["nucypher-contracts"]["main"].TACoApplication.at(
        "0x329bc9Df0e45f360583374726ccaFF003264a136"
    )
