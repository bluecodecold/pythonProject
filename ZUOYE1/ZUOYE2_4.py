a_jin =input("输入古代的几斤:")
a_liang =input("输入古代的几两:")
a_total_liang = float(a_jin) * 16 + float(a_liang)
b_jin = a_total_liang //10
b_liang = a_total_liang % 10
print(f"古代的{a_jin}斤，{a_liang}是现代的{b_jin}斤，{b_liang}两")




