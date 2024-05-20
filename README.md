# taco-rewards-bot
A bot that periodically transfers the ongoing TACo rewards to TACoApp contract to be distributed

This should be executed periodically with a
[`rewardDuration`](https://github.com/nucypher/nucypher-contracts/blob/main/contracts/contracts/TACoApplication.sol#L205)
frequency.

### Running fork for development purposes

.env file:

```
WEB3_INFURA_PROJECT_ID=deaxxxxxxxxxxxxxxxxxxxxxxxxxxe1c
```

```
export APE_ACCOUNTS_rewards-distributor_PASSPHRASE=xxxxxx
ape run rewards_bot --account rewards-distributor --network ethereum:sepolia-fork:foundry
```
