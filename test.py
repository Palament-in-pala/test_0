import pyupbit

access = "VCVGul6BAQiJHalEFcsamaUC32K0sxQ3hlMxoZL6"          # 본인 값으로 변경
secret = "gUMENAh2fQqSqKcvejy9eCcVHCax0MA85ImrvVmg"          # 본인 값으로 변경
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

print(f"ETH 가격: {ETH_price}원")
print(f"ETH 수량: {ETH_hold}개")
print(f"ETH 자산: {ETH_asset}원")
print(f"원화 자산: {KRW_asset}원")

