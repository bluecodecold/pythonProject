price = float(input("请输入应收金额"))
money = float(input("已收金额为:"))

if price > 100:
    price *= 0.9
    if price < money:
        back_money = money - price
        print(f"应该找回{back_money}元")
    else:
        back_money = price - money
        print(f"还差{back_money}元")
else:
    if price < money:
        back_money = money - price
        print(f"应该找回{back_money}元")
    else:
        back_money = price - money
        print(f"还差{back_money}元")