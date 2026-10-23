# Better: pass price as a parameter:

def compute_tax2(price_before_tax):
    return price_before_tax * 0.10

print(compute_tax2(200))  # 20.0