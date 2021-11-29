print("==================================")
print("             알바비               ")
print("==================================")

sum=0

weekday=int(input("평일 근무시간 : "))
weekend=int(input("주말 근무시간 : "))
holiday=int(input("연휴 근무시간 : "))

if weekday > 0 :

    sum=weekday * 8720
    print("평일", weekday, "시간", end=" ")

if weekend > 0 :

    sum=sum+(weekend * 10000)
    print("주말", weekend, "시간", end=" ")

if holiday > 0 :

    sum=sum+(holiday * 12000)
    print("연휴", holiday, "시간", end=" ")
    
print()
print("===================================")
print("          급여 명세서              ")
print("===================================")

print("평일:", weekday, "시간")
print("주말:", weekend, "시간")
print("연휴:", holiday, "시간")
print()
print("총급여:",sum,"원")
print("===================================")
print("실수령액: ",sum*0.97,"원")

