def test_string_formatting():
    expected_msg = "Buenos dias Federico. Felices 41!"
    name = "Federico"
    birthday = 41
    #the following f at the begining of the string is for formatting and will evaluate the variables
    formatted_msg = f"Buenos dias {name}. Felices {birthday}!"
    assert expected_msg == formatted_msg

def test_enumerate_function():
    #enumerate is often useful to avoid the idx++ in every loop (if we compare with Java)
    arreglo = [ "f", "e", "d", "e"]
    final_name = ""
    for idx, val in enumerate(arreglo):
        final_name += str(idx) +val
    assert final_name == "0f1e2d3e"
