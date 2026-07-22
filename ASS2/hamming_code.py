# this function calculates parity bits
def calculate_parity(m):
    r = 0
    while (2**r) < (m+r+1):
        r += 1
    return r



# this function is used for the generating the hamming code
def generate_hamming_code(data):
    m = len(data)

    #this is where we are finding out the parity bits
    r = calculate_parity(m)

    total_bits = m + r

    # create array to store the bits
    hamming = ['0']*(total_bits + 1)    
    # here we are deciding position of parity bits
    data_index = m - 1
    for position in range(total_bits, 0 ,-1):
        # if not power of 2 then it is data bit
        if (position & (position - 1)) != 0:
            hamming[position] = data[data_index]
            data_index -= 1

    parity_position = 1
    while parity_position <= total_bits:
        parity = 0

        for position in range(1, total_bits + 1):
            #checking if curr posistion is belonging to this parity bit
            if position & parity_position: 
                parity ^= int(hamming[position]) #here we are doing XOR operation
            
        hamming[parity_position] = str(parity)
        parity_position *= 2 # here we are taking for next parity postion 

    #displaying hamming code
    print("\n")
    print("Number of Data Bits   :", m)
    print("Number of Parity Bits :", r)
    print("--------------------------------------")

    print("Generated Hamming Code : ", end="")

    code = ""

    for position in range(total_bits,0,-1):
        print(hamming[position],end = "")
        code += hamming[position]
    
    print()
    return code



# this function is useful for detecting and correcting error
def detect_and_correct(received):
    total_bits = len(received)

    #creation of array at the receiver side
    code = ['0']*(total_bits + 1) 

    # storing received bits
    index = 0

    for position in range(total_bits, 0, -1):
        code[position] = received[index]
        index += 1

    # checking parity bits again 
    error_position = 0
    parity_position = 1

    while parity_position <= total_bits:
        parity = 0

        for position in range(1, total_bits + 1):
            if position & parity_position:
                parity ^= int(code[position]) #taking XOR at the receiver side

        if parity != 0:        
            error_position += parity_position
            
        parity_position *= 2 # here we are taking for next parity postion 

    # displaying result   
    if error_position == 0:
         print("\nNo Error Found!")
    else:
        print("\nError Found at Position :", error_position)

        # now correct error occured position

        if code[error_position] == "0":
            code[error_position] = '1'
        else:
            code[error_position] = '0'
        

        print("Corrected Hamming Code : ", end="")

        for position in range(total_bits, 0, -1):

            print(code[position], end="")

        print()



# this function is used to validate the binary input 
def is_bin(binary_string):
    for bit in binary_string:
        if bit != '0' and bit != '1':
            return False

    return True 



# main function
def main():
    while True:
        print("Hamming code program")
        print("1. Generate Hamming Code")
        print("2. Detect and Correct Error")
        print("3. Exit")

        choice = input("\nEnter your choice : ")

        if choice == "1":
            data = input("\nEnter Binary Data: ")
            if is_bin(data):
                generate_hamming_code(data)

            else:
                print("\nInvalid Input!")
                print("Please enter only 0 and 1.")
        
        elif choice == "2":
            received = input("\nEnter Received Hamming Code : ")

            if is_bin(received):
                detect_and_correct(received) 
            else:
                print("\nInvalid Input!")
                print("Please enter only 0 and 1.")
        elif choice == "3":
            print("Exiting this program!!!")
            break
        else:
            print("\nInvalid choice!")



if __name__ == "__main__":
    main()