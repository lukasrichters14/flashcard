def open_files():
    '''Open a file specified by the user and open a file to write the data.'''
    # Get a file name.
    file_name = input("Enter the name of the file to open: ")
    valid_file = False
    # Make sure it is a valid file and continue to prompt if it isn't.
    while not valid_file:
        try:
            read_file = open(file_name)
            # The write file name is the name of the open file with
            # "-Finished.txt" appended to the end. The initial file extension
            # is removed for the write file.
            write_file_name = file_name[:file_name.index(".")] + "-Finished.txt"
            write_file = open(write_file_name, "w+")
            valid_file = True
        
        # Reprompt if the file name is incorrect.
        except FileNotFoundError:
            file_name = input("Sorry, this file cannot be found. Please try again: ")
    
    return read_file, write_file

def format_simple(line, split_char):
    line = line
    split_char = split_char
    # Find where the question ends.
    question_end = find_last_of(split_char, line) + 1
    # Split string into question and answer.
    question = line[:question_end].lower().strip().capitalize()
    answer = line[question_end:].lower().strip().capitalize()
    
    # If the last character of the answer is not a period, add a period.
    if answer[-1] != ".":
        answer += "."
        
    # Capitalize each letter after a period in the question.
    for ind, ch in enumerate(question):
        if ch == "." and ind != (len(question)-1):
            question = question[:ind+1] + " " + question[ind+2].capitalize() + question[ind+3:]
        
    # Capitalize each letter after a period in the answer.
    for ind2, ch2 in enumerate(answer):
        if ch2 == "." and ind2 != (len(answer)-1):
            answer = answer[:ind2+1] + " " +answer[ind2+2].capitalize() + answer[ind2+3:]            
    
    # Add an @ symbol to the end of the question to differentiate between
    # question and answer on quizlet.
    question += "@"
    
    # Put everything back together to output.
    final_output = question + answer
        
    return final_output

def extract_data(file):
    '''Takes a file as input and puts each line into a list.'''
    return_list = []
    
    for line in file:
        return_list.append(line)
    
    return return_list

def find_last_of(string, char):
    '''Finds the last instance of the given char in the given string. Returns
    the index of the last instance of the character.'''
    char = char
    string = string
    
    index = 0
    
    for i, c in enumerate(string):
        if c == char:
            index = i
    
    return index

def format_complex(file_list, q_end_char):
    '''Takes the part of the file list that is a valid question and answer and
    formats the output.'''
    file_list = file_list
    
    print(file_list)
    
    answer = ""
    for e in file_list:
        end_of_qestion = False
        
        if e == q_end_char:
            end_of_question = True
        
        if not end_of_question:
            question += e
        else:
            answer += e
    
    question = question.lower().strip().capitalize()
    answer = answer.lower().strip().capitalize()
    
    final_output = question + "@" + answer
    
    return final_output
    
        
    

def get_complex(file_list):
    '''Takes a piece of the file list and determines where the answers end.'''
    file_list = file_list
    return_list = []
    return_list.append(file_list[0])
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    bullet_symbol = file_list[1][0]
    
    # Find the end of the answer.
    for i, e in enumerate(file_list[1:]):
        e.strip()
        if e[0].lower() in alphabet:
            if ("?" in e) or ("-" in e) or (":" in e):
                end_of_answer = i - 1
                break
            elif e == "\n":
                end_of_answer = i - 1
                break
        elif e[0] != bullet_symbol:
            end_of_answer = i - 1
            break
        
    # Place all the parts of the answer into the return list.
    for e in file_list[1:end_of_answer]:
        return_list.append(e)
        
    return return_list
    

def main():
    '''This is the overall program.'''
    # Open the two files.
    read_file, write_file = open_files()
    
    # Get all the lines in the file.
    file_list = extract_data(read_file)
    
    for i, line in enumerate(file_list):
        if line[-1] == "?":
            complex_qa = get_complex(file_list[i:])
            output = format_complex(complex_qa)
            print(output, file=write_file)
        elif line[-1] == '-':
            complex_qa = get_complex(file_list[i:])
            output = format_complex(complex_qa)
            print(output, file=write_file)
        elif line[-1] == ":":
            complex_qa = get_complex(file_list[i:])
            output = format_complex(complex_qa)
            print(output, file=write_file)
        # If there isn't an end-of-question identifier at the end of the line.
        else:
            if "?" in line:
                output = format_simple(line, "?")
                print(output, file=write_file)
            elif "-" in line:
                output = format_simple(line, "-")
                print(output, file=write_file)
            elif ":" in line:
                output = format_simple(line, ":")
                print(output, file=write_file)
            else:
                print("There is no conversion for this line:")
                print(line)
            
                
    read_file.close()
    write_file.close()


if __name__ == "__main__":
    main()
