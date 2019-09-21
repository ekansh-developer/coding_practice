name=input("enter name of the student :")
college=input("enter the name of college :")
phy=int(input("enter marks in physics :"))
chem=int(input("enter marks in chemistry :"))
math=int(input("enter marks in maths :"))
bio=int(input("enter marks in biology :"))
eng=int(input("enter marks in english :"))
total_marks=phy+chem+math+bio+eng
total_aggrigate = phy+chem+math
print(name, "total in physics, chemistry, maths is",total_aggrigate)
print()
per=total_aggrigate/3
print(name,"your percentage in physics, chemistry, maths is:",per)
total_percentage= total_marks/5
print(name,"your total percentage is :",total_percentage)
print()
if per>65 and total_percentage>=70:
    print(name,"your percentage in physics, chemistry, maths is",per,"and your total percentage is",total_percentage,"you are eligible for science")
    print()
    if bio>=60:
        print(name,"you score",bio,"in biology you can also take biology")
    else:
        print(name,"you can't take biology because your marks in biology is less than 60")

if 60<=per<=65 and 60<=total_percentage<70:
    print(name, "your percentage in physics, chemistry, maths is", per,"and your total percentage is",total_percentage,"you are eligible for commerce")
    print()
    if bio>=60:
        print(name,"you score",bio,"in biology you can also take biology")
    else:
        print(name,"you can't take biology because your marks in bio less than 60")
if total_percentage<60:
    print("sorry you are not eligible for science and commerce")
    print()
    if bio>=60:
        print(name,"you score",bio,"in biology you can take biology")
    else:
        print(name,"try for any other course")