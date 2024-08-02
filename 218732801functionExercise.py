#problem 1

def list_check(nums):
    
    pattern = [0, 2, 3]

    # Loop through the list with range up to where the pattern can still fit
    for i in range(len(nums) - len(pattern) + 1):
        if nums[i:i + len(pattern)] == pattern:
            return True
    
    return False

               
print(list_check([1,0,2,3,1]))         
                        


         
    

#problem2


def string_bits(name): 
    new_name = name[::2]  
    return new_name

print(string_bits("heeololeo"))

#problem 3




def end_check(name,name_2):
    if(name[-3].lower() == "a" and name[-2].lower() == "b"and name[-1].lower() == "c"):
        if(name_2[-3].lower() == "a" and name_2[-2].lower() == "b"and name_2[-1].lower() == "c"):
            return True
    else:
            return False

print(end_check( "rafab", "rateabc"))

#problem 4


def double_char(new_string):
     result = ""
     for i in range(len(new_string)):
        result += new_string[i] *2

     return result

print(double_char("hello"))

#problem 5

def no_teen_sum(a,b,c):
    sum = 0
    sum = a+b+c
    return sum

print(no_teen_sum(1,2,1))

def fixed_teen(n):
    if n >= 13 and n <= 19:
        n = 0



#problem 6


def even_intergers(even):
    count = 0
    for num in even:
         
         if num % 2 == 0:
             count += 1

    return count

print(even_intergers([1,8,4,5,7,8]))