s = int(input())
h_s = int(s/100)
t_s = int((s/10)%10)
o_s = int(s%10)
count=0
if h_s == 1:
    count+=1
if t_s == 1:
    count+=1
if o_s == 1:
    count+=1
print("{}".format(count))
