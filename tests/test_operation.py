from itertools import count
from brownie import Wei, reverts
from useful_methods import  genericStateOfVault,genericStateOfStrat
import random
import brownie
# TODO: Add tests here that show the normal operation of this strategy
#       Suggestions to include:
#           - strategy loading and unloading (via Vault addStrategy/revokeStrategy)
#           - change in loading (from low to high and high to low)
#           - strategy operation at different loading levels (anticipated and "extreme")



def test_weth_del(web3, chain, Vault, Strategy, live_dai_vault, live_dai_strategy, whale, gov, dai,weth, samdev):
    live_strategy = live_dai_strategy
    live_vault = live_dai_vault

    live_vault.setDepositLimit(1e28, {"from": gov})
    live_vault.updateStrategyDebtLimit(live_strategy, 1e28, {"from": gov})

    #increase balance of dai vault
    

    #deploy new strat
    weth_vault = samdev.deploy(
        Vault, weth, samdev, samdev, "", ""
    )

    weth.approve(weth_vault, 2 ** 256 - 1, {"from": whale} )

    strategy = samdev.deploy(Strategy, weth_vault)

    weth_vault.addStrategy(strategy, 2 ** 256 - 1, 2 ** 256 - 1, 50, {"from": samdev})

    deposit_amount = Wei('100 ether')
    weth_vault.deposit(deposit_amount, {"from": whale})


    print("\n******* Harvest Weth ******")
    strategy.harvest({'from': samdev})

    print("\n******* Weth ******")
    genericStateOfStrat(strategy, weth, weth_vault)
    genericStateOfVault(weth_vault, weth)
    print("\n******* Dai ******")
    genericStateOfStrat(live_strategy, dai, live_vault)
    genericStateOfVault(live_vault, dai)




    print("\n******* Harvest Dai ******")
    live_strategy.harvest({'from': samdev})

    print("\n******* Weth ******")
    genericStateOfStrat(strategy, weth, weth_vault)
    genericStateOfVault(weth_vault, weth)
    print("\n******* Dai ******")
    genericStateOfStrat(live_strategy, dai, live_vault)
    genericStateOfVault(live_vault, dai)

