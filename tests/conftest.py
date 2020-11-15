import pytest
from brownie import Wei, config

@pytest.fixture
def live_dai_vault(Vault):
    yield Vault.at('0x9B142C2CDAb89941E9dcd0B6C1cf6dEa378A8D7C')

@pytest.fixture
def live_dai_strategy(Strategy):
    yield Strategy.at('0x4C6e9d7E5d69429100Fcc8afB25Ea980065e2773')

@pytest.fixture
def vault(gov, rewards, guardian, currency, pm):
    Vault = pm(config["dependencies"][0]).Vault
    vault = guardian.deploy(Vault, currency, gov, rewards, "", "")
    yield vault

@pytest.fixture
def Vault(pm):
    Vault = pm(config["dependencies"][0]).Vault
    yield Vault


@pytest.fixture(scope='session')
def samdev(accounts):
    yield accounts.at('0xC3D6880fD95E06C816cB030fAc45b3ffe3651Cb0', force=True)


@pytest.fixture
def andre(accounts):
    # Andre, giver of tokens, and maker of yield
    yield accounts[0]


@pytest.fixture
def token(andre, Token):
    yield andre.deploy(Token)


@pytest.fixture
def gov(accounts):
    # yearn multis... I mean YFI governance. I swear!
    yield accounts.at('0x846e211e8ba920b353fb717631c015cf04061cc9', force=True)

@pytest.fixture
def rewards(gov):
    yield gov  # TODO: Add rewards contract


@pytest.fixture
def guardian(accounts):
    # YFI Whale, probably
    yield accounts[2]


@pytest.fixture
def vault(gov, rewards, guardian, token, Vault):
    vault = guardian.deploy(Vault, token, gov, rewards, "", "")
    yield vault


@pytest.fixture
def strategist(accounts):
    # You! Our new Strategist!
    yield accounts[3]


@pytest.fixture
def keeper(accounts):
    # This is our trusty bot!
    yield accounts[4]


@pytest.fixture
def strategy(strategist, keeper, vault, Strategy):
    strategy = strategist.deploy(Strategy, vault)
    strategy.setKeeper(keeper)
    yield strategy



@pytest.fixture
def weth(interface):
  
    yield interface.ERC20('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')

@pytest.fixture
def dai(interface):
    yield interface.ERC20('0x6b175474e89094c44da98b954eedeac495271d0f')

@pytest.fixture
def whale(accounts, history, web3):
    #big binance7 wallet
    #acc = accounts.at('0xBE0eB53F46cd790Cd13851d5EFf43D12404d33E8', force=True)
    #big binance8 wallet
    #acc = accounts.at('0xf977814e90da44bfa03b6295a0616a897441acec', force=True)
    #lots of weth account
    acc = accounts.at('0x767Ecb395def19Ab8d1b2FCc89B3DDfBeD28fD6b', force=True)
    yield acc