N = int(input())
hours = int(N / 3600)
minutes = int((N % 3600) / 60)
seconds = (N % 3600 % 60)

print("{}:{}:{}".format(hours, minutes, seconds))

# n = int(input())
# hours = n//3600
# n = n - hours*3600
# minutes = n//60
# n = n- minutes*60
# print(str(hours)+":"+str(minutes)+":"+str(n))