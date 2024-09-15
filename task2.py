n = int(input())  
a = list(map(int, input().split()))  

result = [0] * n  
previous_sum = 0  

for i in range(n):  
    if a[i] != -1:  
        current_sum = a[i]  
  
        if i == 0:  
            result[i] = current_sum 
        else:  
            needed = current_sum - previous_sum  
            if needed <= 0:  
                print("NO")  
                exit()  

            result[i] = needed  

        previous_sum = current_sum  
        
    else:  
        if i == 0:  
            result[i] = 1   
        else:  
            result[i] = result[i - 1] + 1  

        previous_sum += result[i]  
  
for i in range(1, n):  
    if result[i] <= result[i - 1]:  
        print("NO")  
        exit()  

print("YES")  
print(" ".join(map(str, result))) 