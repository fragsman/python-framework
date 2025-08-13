# - For the following tests we will be using Python Comprehension expressions. 
# - Comprehension in Python provides a concise and readable way to create new list, sets, etc based on existing 
# iterables (like lists, tuples, or strings). It offers a more compact syntax compared to traditional for loops 
# for common list creation and manipulation tasks
# - Example Syntax is variable = {expression for item in iterable if condition}

def test_if_number_is_in_primes_set():        
    assert 37 in {
        num #expression
        for num in range(2, 50) #for item in iterable
        if not any(num % div == 0 for div in range(2, num)) #if condition
    }
    ##It will iterate from 2,49 and it will try to perfectly divide between numbers 2 and num-1
    #if is not perfectly divided by anyone of them then it will be added to the set
    #then if 37 is in that set, then is prime

#Capitalize all names and include in the set, then verify if a name is in that set
def test_if_name_is_in_capitalized_set():
    names = ["Anna", "DorK", "PAUL"]
    assert "Paul" in { name.capitalize() for name in names }

#Get a list of first letter of name and surname. Ej: John Doe = JD
def test_if_initials_are_in_set():
    names = ["John Doe", "Crash Bandicot", "Paul Walkter"]
    assert "JD" in {
        name.split()[0][0]+name.split()[1][0] #grabs from the first split(0) the first(0) letter and from the second split(1) the first(0) letter
        for name in names
        if len(name.split())==2
    }

#Get the even numbers
def test_list_filtered_by_even_numbers():
    even_list = [num for num in range(10) if num % 2 == 0]
    expected_list = [0,2,4,6,8]
    assert even_list == expected_list

#Get the words that start by 'y' and end in 'a'
def test_names_filtered_by_multi_condition():
    words = ["year", "yulia", "mika", "yamila"]
    processed_words = [word for word in words 
                        if len(word)>=2
                        if word[0]=="y"
                        if word[-1]=="a"] #-1 is last index, -2 is pre-last, etc.
    expected_words = ["yulia", "yamila"]
    assert processed_words == expected_words

#Categorize numbers by even or odd
def test_categorize_numbers():
    numbers = [2,4,5,6] #even, even, odd, even
    categories = ["even" if(num % 2 == 0) else "odd" for num in numbers]
    expected_categories = ["even","even","odd","even"]
    assert categories == expected_categories

def double(number):
    return number * number

#Modify a value in a dictionary using a own function (like 'double', see above function)
def test_modify_value_in_dictionary():
    original_dic = [("a",1),("b",2),("c",3)]
    dicc = {k: double(v) for k,v in original_dic}
    expected_dic = {"a":1,"b":4,"c":9}
    assert dicc == expected_dic
