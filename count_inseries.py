def get_num_count(numeral, n1, n2):

    """
    Function calculate number of specified digits {numeral} in numbers from {n1} to {n2}
    """    
    
    numeral_str = str(numeral)
      
    # Convert numbers from {n1} to {n2} to string number_string 
    number_string = ''.join(map(str, range(n1,n2+1)))  
    
    # Create list containing desired {numeral} by mask
    list_of_desired_numbers = list(filter(lambda numbers: any(char == numeral_str for char in numbers), number_string)) 

    return len(list_of_desired_numbers)