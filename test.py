import pyupbit

access = "0x123"          # 본인 값으로 변경
secret = "0x23"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

# print(pyupbit.get_tickers())
# print(pyupbit.get_tickers(fiat="KRW"))
# print(pyupbit.get_current_price("KRW-BTC"))
# print(pyupbit.get_current_price(["KRW-BTC", "KRW-XRP"]))
# print(upbit.get_balances())

KRW_asset = upbit.get_balance("KRW")
ETH_price = pyupbit.get_current_price("KRW-ETH")
ETH_hold = upbit.get_balance("KRW-ETH")
ETH_asset = ETH_hold * ETH_price

print(f"ETH price: {ETH_price}won")
print(f"ETH amount: {ETH_hold}")
print(f"ETH value: {ETH_asset}won")
print(f"KWR value: {KRW_asset}won")

