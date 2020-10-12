# -*- coding: utf-8 -*-
"""


@author: kalyan
"""

def isprime(n):
    #Optimized code to find whether a number is prime
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
     
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True




def find_prime_fib():
    # Dynamic programming solution to find the prime numbers
    dp = [1,1,2,3,5,8,13,21]
    
    s = [1,1,2,3,5,8,1,3,2,1]
    
    n = 8
    flag = 0
    c = 0
    res = []
    while True:
        
        temp = dp[n-1]+dp[n-2]
        dp.append(temp)
        #print(dp)
        n+=1
        for i in str(temp):
            #print(i)
            a = (int(''.join([str(k) for k in s])))
            
            #print(1)
            s.pop(0)
            s.append(int(i))
            if isprime(a):
                c+=1
                print("Found "+str(c)+" prime number")
                # if c == 1:
                #     print(a)
                #     break
                if c == 44722:
                    res.append(a)
                if c == 53215:
                    res.append(a)
                    flag = 1
                    break
        if flag == 1:
            break
        
    return res

def specialcode(n):
    # Helper function to crack the code
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {}
    res = ""
    for i in range(len(alpha)):
        d[i] = alpha[i]
    #print(d)
    c = 0
    for i in range(2,len(n)+1,2):
        temp = int(n[c:i])
        if temp>=26:
            temp = temp%26
        res+=d[temp]
        c+=2
    return res
            
    
res = find_prime_fib()
print("The code for 44722 ten digit prime number is:"+ specialcode(str(res[0]))) #MUTED
print("The code for 53215 ten digit prime number is:"+ specialcode(str(res[1]))) #VALET

    
        
        