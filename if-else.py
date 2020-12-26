x = 50
y = 50

if x < y:
    print(x, "je manje od", y)
elif x > y:
    print(x ,"je vece od", y)
else:
    print("brojevi su jednaki")


unos1 = input("unesi prvi broy: ")
unos2 = input("unesi drugi broy: ")

print("-" * 60)

if unos1 < unos2:
    print("prvi broj manji od drugog")
elif unos1 > unos2:
    print("prvi broj veci od drugog")
else:
    print("brojovi su jednaki")
