# Functions with Outputs

# https://stackoverflow.com/questions/8347048/how-to-convert-string-to-title-case-in-python

def format_name(f_name, l_name):
    formatted_f_name = f_name.title() # To convert it to Title case
    formatted_l_name = l_name.title()
    #print(f"Formatted name is {formatted_f_name} {formatted_l_name}")
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("RoHIt","katta"))