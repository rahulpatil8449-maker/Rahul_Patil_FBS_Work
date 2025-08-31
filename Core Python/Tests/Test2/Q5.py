p1 = float(input("Enter price of product1: "))
p2 = float(input("Enter price of product2: "))
p3 = float(input("Enter price of product3: "))
p4 = float(input("Enter price of product4: "))
p5 = float(input("Enter price of product5: "))

total_price = p1 + p2 + p3 + p4 + p5
gst = 0.18 * total_price

total_bill = total_price + gst

print("Total price before adding GST = Rs.", total_price)
print("18% on the total bill = Rs.", gst)
print("Total Bill Amount = Rs.", total_bill)