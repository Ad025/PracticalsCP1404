products = [["phone",340 , False],["pc",1420.95, True],["plant",24.5,True]]
for product in products:
    sections = product.strip().split(',')
    if sections[3] == True:
        print("Yaya")


