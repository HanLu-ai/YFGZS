print("本程序由御风工作室编写。")
product_name = input("商品名称：")
unit_price = eval(input("商品单价："))
quantity = eval(input("数量："))
received = int(input("实收："))
due_amount = unit_price * quantity
due_amount = round(due_amount, 2)
change = received - due_amount
change = round(change, 1)
print(f"Python超市购物小票")
print("商品名称\t"+"单价\t"+"数量")
print(f"{product_name}\t{unit_price}\t{quantity}")
print(f"应付：{due_amount}")
print(f"实收：{received}")
print(f"找零：{change}")