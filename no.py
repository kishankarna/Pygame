import p

num=int(input("Enter number for calculation"))

print("make selection...:")
print("1 for multiply by self number...:")
print("2 for divide by number 2........:")

sel=int(input("Enter selection.........:"))
ob=p.calculate()

if sel==1:

        k=ob.mult(num)
        print(k)
elif sel==2:
        ob2=ob.div(num)
        print(ob2)