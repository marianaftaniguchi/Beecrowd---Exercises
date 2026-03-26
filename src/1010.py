product1_code, product1_quantity, product1_price = input().split()
product1_code = int(product1_code)
product1_quantity = int(product1_quantity)
product1_price = float(product1_price)

product2_code, product2_quantity, product2_price = input().split()
product2_code = int(product2_code)
product2_quantity = int(product2_quantity)
product2_price = float(product2_price)

total_value = (product1_quantity * product1_price) + (product2_quantity * product2_price)

print(f"VALOR A PAGAR: R$ {total_value:.2f}")
