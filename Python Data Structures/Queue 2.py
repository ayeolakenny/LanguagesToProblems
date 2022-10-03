from Queue1 import queueclass
qu = queueclass()
choice = 0

while choice<4:
    print(" ----- Queue ----- ")
    print("   1 - Enqueue")
    print("   2 - Dequeue")
    print("   3 - Search")
    print("   4 - Exit")
    choice  = int(input("Enter choice ="))

    if choice == 1:
        ele = int(input("Enter element to enqueue ="))
        qu.enqueue(ele)
        print("\nUpdated Queue =",qu.display(),"\n")

    elif choice == 2:
        ele = qu.dequeue()
        if ele == -1:
            print("Underflow")
        else:
            print("Element deleted =",ele)
            print("\nUpdated Queue =",qu.display(),"\n")

    elif choice == 3:
        ele = int(input("Enter element to search ="))
        k = qu.search(ele)
        if k == -1:
            print("Queue empty")
        elif k == -2:
            print("Element absent")
        else:
            print("Element at index =",k)

    else:
        break
