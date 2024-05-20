import click
import time
from ape import project
from ape.cli import ConnectedProviderCommand, account_option

YEAR_IN_SECONDS = 31536000
TACo_APP_ADDRESS = "0x329bc9Df0e45f360583374726ccaFF003264a136"


@click.command(cls=ConnectedProviderCommand)
@account_option()
@click.option(
    "--apy",
    "-a",
    help="Staking rewards APY in %. Used to estimate the rewards to be pushed",
    default=3.75,
    required=True,
    type=click.FLOAT,
)
def cli(account, apy):
    account.set_autosign(enabled=True)

    taco_application = project.dependencies["nucypher-contracts"][
        "main"
    ].TACoApplication.at(TACo_APP_ADDRESS)

    authorized_overall = taco_application.authorizedOverall()
    last_update_time = taco_application.lastUpdateTime()

    rewards_to_be_pushed = int(
        authorized_overall
        * (apy / 100)
        * (int(time.time()) - last_update_time)
        / YEAR_IN_SECONDS
    )

    # TODO: check error
    taco_application.pushReward(rewards_to_be_pushed, sender=account)

    # TODO: use logger instead of print
    print(int(rewards_to_be_pushed))
