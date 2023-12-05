import re

def filereader(file_path : str):
    with open(file_path, "r") as infile:
        for in_line in infile:
            yield in_line


def first_and_last_number(in_str: str):
    values = ["1","2","3","4","5","6","7","8","9","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    first_current_index = len(in_str)
    last_current_index = -1
    for num in values:

        first_new_index = in_str.find(num)
        last_new_index = in_str.rfind(num)

        if first_new_index < first_current_index and first_new_index != -1 :
            first_number = num
            first_current_index = first_new_index

            
        if last_new_index > last_current_index and last_new_index != -1 :
            last_number = num
            last_current_index = last_new_index
    first_number = convert_text_to_number(first_number)
    last_number = convert_text_to_number(last_number)
	
    return int(f"{first_number}{last_number}")

def convert_text_to_number(in_str: str):
    if in_str == "one": return "1"
    if in_str == "two": return "2"
    if in_str == "three": return "3"
    if in_str == "four": return "4"
    if in_str == "five": return "5"
    if in_str == "six": return "6"
    if in_str == "seven": return "7"
    if in_str == "eight": return "8"
    if in_str == "nine": return "9"
    else: return in_str


final_value = 0
for line in filereader("day1\day1_data.txt"):
    final_value += first_and_last_number(line)

print(final_value)

