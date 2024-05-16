import click
import time
from ape import project
from ape.cli import ConnectedProviderCommand, account_option


@click.command(cls=ConnectedProviderCommand)
@account_option()
def cli(account):
    account.set_autosign(enabled=True)

    taco_application = project.dependencies["nucypher-contracts"][
        "main"
    ].TACoApplication.at("0x329bc9Df0e45f360583374726ccaFF003264a136")

    # TODO: calculate the rewards to be pushed
    authorized = taco_application.authorizedOverall()
    last_update_time = taco_application.lastUpdateTime()
    time_elapsed = time.now() - last_update_time
    # push_rewards = authorized * 0.0375 /

    print(time_elapsed)

    # contract.pushReward(100, sender=account)
