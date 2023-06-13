n=input("Enter your name: ")
sn=input("Enter your School name: ")
s1=int(input("Enter your Java marks: "))
s2=int(input("Enter your C++ marks: "))
s3=int(input("Enter your JSP marks: "))
s4=int(input("Enter your Python marks: "))
s5=int(input("Enter your JS marks: "))
s6=int(input("Enter your Go marks: "))
print("Name: ",n)
print("School Name: ",sn)

if(s1>=30 and s1<60): 
    print("Java = ",s1,"/100: Grade B")
elif(s1>=60 and s1<90):
    print("Java = ",s1,"/100: Grade A")
elif(s1>=90):
    print("Java = ",s1,"/100: Grade A+")
else:
    print("Java = ",s1,"/100: Grade C")


if(s2>=30 and s2<60): 
    print("C++ = ",s2,"/100: Grade B")
elif(s2>=60 and s2<90):
    print("C++ = ",s2,"/100: Grade A")
elif(s2>=90):
    print("C++ = ",s2,"/100: Grade A+")
else:
    print("C++ = ",s2,"/100: Grade C")


if(s3>=30 and s3<60): 
    print("JSP = ",s3,"/100: Grade B")
elif(s3>=60 and s3<90):
    print("JSP = ",s3,"/100: Grade A")
elif(s3>=90):
    print("JSP= ",s3,"/100: Grade A+")
else:
    print("JSP = ",s3,"/100: Grade C")


if(s4>=30 and s4<60): 
    print("Python = ",s4,"/100: Grade B")
elif(s4>=60 and s4<90):
    print("Python = ",s4,"/100: Grade A")
elif(s4>=90):
    print("Python= ",s4,"/100: Grade A+")
else:
    print("Python = ",s4,"/100: Grade C")

if(s5>=30 and s5<60): 
    print("JS = ",s5,"/100: Grade B")
elif(s5>=60 and s5<90):
    print("JS = ",s5,"/100: Grade A")
elif(s5>=90):
    print("JS= ",s5,"/100: Grade A+")
else:
    print("JS = ",s5,"/100: Grade C")

if(s6>=30 and s6<60): 
    print("Go = ",s6,"/100: Grade B")
elif(s6>=60 and s6<90):
    print("Go = ",s6,"/100: Grade A")
elif(s6>=90):
    print("Go = ",s6,"/100: Grade A+")
else:
    print("Go = ",s6,"/100: Grade C")

print("Total: ",s1+s2+s3+s4+s5+s6)
print("Percentage: ",((s1+s2+s3+s4+s5+s6)/600)*100,"%")

if((s1+s2+s3+s4+s5+s6)>=30 and (s1+s2+s3+s4+s5+s6)<60): 
    print("Overall Grade = B")
elif((s1+s2+s3+s4+s5+s6)>=60 and (s1+s2+s3+s4+s5+s6)<90):
    print("Overall Grade = A")
elif((s1+s2+s3+s4+s5+s6)>=90):
    print("Overall Grade = A+")
else:
    print("Overall Grade =  C")







