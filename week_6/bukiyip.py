
#from calutils import month_name

def main():
    
    def bukiyip_to_decimal(a):
        """given a number 'a' it converts a bukiyip number to decimal"""
        llen = len(a) 
        power = 1 #Initialize power of base 
        num = 0     #Initialize result 
  
    # Decimal equivalent is str[len-1]*1 +  
    # str[len-2]*base + str[len-3]*(base^2) + ...  
        for i in range(llen - 1, -1, -1): 
          
        # A digit in input number must  
        # be less than number's base  
            if val(str[i]) >= base: 
                print('Invalid Number') 
                return -1
            num += val(str[i]) * 10 
            power = power * 10 
        return num
    
    def decimal_to_bukiyip(a):
        """given a number 'a' it converts a decimal number to bukiyip"""
        remainder_stack = []
        while decimal_number > 0:
            remainder = decimal_number % 3
            remainder_stack.append(remainder)
            decimal_number = decimal_number // 3
        
        bukiyip_digits = []
        while remainder_stack:
        
            bukiyip_digits.append(str(remainder_stack.pop()))
        
            return ''.join(binary_digits)                
    def bukiyip_add(a,b):
        """given two bukiyip numbers 'a' & 'b' it adds them together"""
        ans = bukiyip_to_decimal(a) + bukiyip_to_decimal(b)
        ans = decimal_to_bukiyip(ans)
      
        return ans        
    
    def bukiyip_multipy(a,b):
        """given two bukiyip numbers 'a' & 'b' it multipies them together"""
        ans = bukiyip_to_decimal(a) * bukiyip_to_decimal(b)
        ans = decimal_to_bukiyip(ans)
        
        return ans
    
    ###
    ##MAIN FUNCTIONS
    ###
    
    print("**** Bukiyip test program ****")
    print("Available commands:")
    print("d <number> : converts given decimal number to base-3.")
    print("b <number> : converts given base-3 number to decimal.")
    print("a <number> <number> : add the given base-3 numbers")
    print("m <number> <number> : multiply the base-3 numbers. q : quit")
    
    command = input("Enter a command:\n").split()
    
    if command[0] == "d":
        number = command[1]
        print(bukiyip_to_decimal(number))
    
    elif command[0] == "b":
        number = command[1]
        print(decimal_to_bukiyip(number))
    
    elif command[0] == "a":
        num_one = command[1]
        num_two = command[2]
        print(bukiyip_add(num_one,num_two))
        
    elif command[0] == "m":
        num_one = command[1]
        num_two = command[2]
        print(bukiyip_multipy(num_one,num_two))
         
main()