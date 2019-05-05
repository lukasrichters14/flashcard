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
    

def is_simple(line):
    '''Returns True if the line is simple, false otherwise.'''
    
    if ("-" in line) and (line[-1] != "-"):
        return True
    
    elif (":" in line) and (line[-1] != ":"):
        return True
    
    elif ("?" in line) and (line[-1] != "?"):
        return True
    
    else:
        return False


def is_complex(line):
    '''Returns True if the line is complex, false otherwise.'''
    
    if "-" == line[-1]:
        return True
    
    elif ":" == line[-1]:
        return True
    
    elif "?" == line[-1]:
        return True
    
    else:
        return False


def is_neither(line):
    '''Returns True if the line is neither complex nor simple, false otherwise.'''
    
    if(not is_complex(line)) and (not is_simple(line)):
        return True
    else:
        return False

    
def organize_data(file_list):
    '''Takes the file list and returns a dictionary of all of the questions as
    keys and answers as values.'''
    
    file_list = file_list
    q_a_dict = {}
    question = ""
    answer = ""
    
    true_index = 0   # Keeps track of the index of the most recent line.
    
    # Loop through the file list.
    for i, line in enumerate(file_list):
        if i == true_index:
            if "-" in line:
                # Question is one line, answer is another.
                if is_complex(line):
                    question = line.strip()
                    answer = ""
                    
                    # Continues to add lines to the answer until a new question
                    # is found.
                    while is_neither(file_list[true_index]):
                        answer += file_list[true_index].strip() + "/n"
                        true_index += 1
                    
                    true_index -= 1  # Makes sure not to skip the next line.
                    
                # Question and answer are on the same line.
                else:
                    split_index = find_last_of(line, "-")
                    question = line[:split_index].strip()
                    answer = line[split_index + 1:].strip()
                
                q_a_dict[question] = answer
            
            elif ":" in line:
                # Question is one line, answer is another.
                if is_complex(line):
                    question = line.strip()
                    answer = ""
                    
                    # Continues to add lines to the answer until a new question
                    # is found.
                    while is_neither(file_list[true_index]):
                        answer += file_list[true_index].strip() + "/n"
                        true_index += 1
                    
                    true_index -= 1  # Makes sure not to skip the next line.
                
                # Question and answer are on the same line.
                else:
                    split_index = find_last_of(line, ":")
                    question = line[:split_index].strip()
                    answer = line[split_index + 1:].strip()
                
                q_a_dict[question] = answer

            elif "?" in line:
                # Question is one line, answer is another.
                if is_complex(line):
                    question = line.strip()
                    answer = ""
                    
                    # Continues to add lines to the answer until a new question
                    # is found.
                    while is_neither(file_list[true_index]):
                        answer += file_list[true_index].strip() + " & "
                        true_index += 1
                    
                    true_index -= 1  # Makes sure not to skip the next line.
                
                # Question and answer are on the same line.
                else:
                    split_index = find_last_of(line, "?")
                    question = line[:split_index].strip()
                    answer = line[split_index + 1:].strip()
                
                q_a_dict[question] = answer
            
            # Basic message to use to signify that there is not a '-', ':', or 
            # '?' character in the given line.
            else:
                print("Unrecognized symbol in line " + str(i + 1) + ".")
                print("Line is:", line)
        
        true_index += 1
    
    return q_a_dict


def output_data(file_dict, out_file):
    '''Takes the dictionary of questions and answers and then writes them to
    the output file.'''
    
    file_dict = file_dict
    out_file = out_file
    
    # Writes the question and answer to the output file. No formatting...yet.
    for q, a in file_dict.items():
        print("{}@{}".format(q, a), file = out_file)

    
def main():
    '''This is the overall program.'''
    # Open the two files.
    read_file, write_file = open_files()
    
    # Get all the lines in the file.
    file_list = extract_data(read_file)
    
    file_dict = organize_data(file_list)
    
    output_data(file_dict, write_file)
                
    read_file.close()
    write_file.close()


if __name__ == "__main__":
    main()
