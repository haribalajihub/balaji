def firstDigit(n) :

    while n >= 10:  

        n = n / 10; 

    return int(n) 


def lastDigit(n) : 

    return (n % 10) 


n = int(input()); 

print(firstDigit(n)+lastDigit(n))  

