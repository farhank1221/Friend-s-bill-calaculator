price = {"shisha": 15, "tea": 5, "juice": 8}


def calculateindividual(name1, name2, name3):
    totalbill = 0
    print("Enter the things" + " " + name1 + " " + "ate:")
    shisha = int(input("Shisha:"))
    tea = int(input("tea:"))
    juice = int(input("juice:"))
    cost1 = shisha * price["shisha"] + juice * price["juice"] + tea * price["tea"]
    discounted1 = cost1 / 10
    cost1 -= discounted1
    print("bill for"+" "+name1+" "+":%s"%cost1)

    print("Enter the things" + " " + name2 + " " + "ate:")
    shisha = int(input("Shisha:"))
    tea = int(input("tea:"))
    juice = int(input("juice:"))
    cost2 = shisha * price["shisha"] + juice * price["juice"] + tea * price["tea"]
    discounted2 = cost2 / 10
    cost2 -= discounted2
    print("bill for"+" "+name2+" "+":%s"%cost2)


    print("Enter the things" + " " + name3 + " " + "ate:")
    shisha = int(input("Shisha:"))
    tea = int(input("tea:"))
    juice = int(input("juice:"))
    cost3 = shisha * price["shisha"] + juice * price["juice"] + tea * price["tea"]
    discounted3 = cost3 / 10
    cost3 -= discounted3
    print("bill for"+" "+name3+" "+":%s"%cost3)
    totalbill = cost1+cost2+cost3
    print("Totalbill:%s"%totalbill)


calculateindividual("tony", "yousuf", "farhan")

