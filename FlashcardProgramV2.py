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


def extract_data(file):
    '''Takes a file as input and puts each line into a list.'''
    return_list = []
    
    for line in file:
        return_list.append(line)
    
    # Appends a $ to the end of the list so that the end of the document can be
    # easily found.
    return_list.append("$")
    
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
    
    line = line.strip()
    
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
    
    line = line.strip()
    
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
    
    line = line.strip()
    
    if (not is_complex(line)) and (not is_simple(line)):
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
    
    # Loops through the file list.
    for i, line in enumerate(file_list):
        if i == true_index:
            true_index += 1
            if "-" in line:
                # Question is one line, answer is another.
                if is_complex(line):
                    # Removes the last character and excess whitespace.
                    question = line[:-1].strip()
                    answer = ""
                    
                    # Continues to add lines to the answer until a new question
                    # is found or the end of the list is found.
                    while is_neither(file_list[true_index]) and file_list[true_index] != "$":
                        answer += file_list[true_index].strip() + "\n"
                        true_index += 1
                    
                    answer = answer[:-1]
                    
                # Question and answer are on the same line.
                else:
                    # Finds where the question ends and answer begins, then
                    # seperates them.
                    split_index = find_last_of(line, "-")
                    question = line[:split_index].strip()
                    answer = line[split_index + 1:].strip()
                
                # Adds the questions and answers to a dictionary.
                q_a_dict[question] = answer
            
            elif ":" in line:
                # Question is one line, answer is another.
                if is_complex(line):
                    # Removes the last character and excess whitespace.
                    question = line[:-1].strip()
                    answer = ""
                    
                    # Continues to add lines to the answer until a new question
                    # is found or the end of the list is found.
                    while is_neither(file_list[true_index]) and file_list[true_index] != "$":
                        answer += file_list[true_index].strip() + "\n"
                        true_index += 1
                    
                    answer = answer[:-1]
                    
                # Question and answer are on the same line.
                else:
                    # Finds where the question ends and answer begins, then
                    # seperates them.
                    split_index = find_last_of(line, ":")
                    question = line[:split_index].strip()
                    answer = line[split_index + 1:].strip()
                
                # Adds the questions and answers to a dictionary.
                q_a_dict[question] = answer

            elif "?" in line:
                # Question is one line, answer is another.
                if is_complex(line):
                    # Removes the last character and excess whitespace.
                    question = line[:-1].strip()
                    answer = ""
                    
                    # Continues to add lines to the answer until a new question
                    # is found or the end of the list is found.
                    while is_neither(file_list[true_index]) and file_list[true_index] != "$":
                        answer += file_list[true_index].strip() + "\n"
                        true_index += 1
                    
                    answer = answer[:-1]
                
                # Question and answer are on the same line.
                else:
                    # Finds where the question ends and answer begins, then
                    # seperates them.
                    split_index = find_last_of(line, "?")
                    question = line[:split_index].strip()
                    answer = line[split_index + 1:].strip()
                
                # Adds the questions and answers to a dictionary.
                q_a_dict[question] = answer
            
            # Keeps the end of list character from interfering with normal
            # operations.
            elif line == "$":
                pass
            
            # Basic message to use to signify that there is not a '-', ':', or 
            # '?' character in the given line.
            else:
                print("Unrecognized symbol in line " + str(i + 1) + ".")
                print("Line is:", line)
    
    return q_a_dict


def output_data(file_dict, out_file):
    '''Takes the dictionary of questions and answers and then writes them to
    the output file.'''
    
    file_dict = file_dict
    out_file = out_file
    
    # Writes the question and answer to the output file. This has the basic
    # formatting, only enough to differentiate the question and answer and
    # seperate cards.
    for q, a in file_dict.items():
        print("{}@{}~!".format(q, a), file = out_file)

    
def main():
    '''This is the overall program.'''
    # Opens the read and write files.
    read_file, write_file = open_files()
    
    # Gets all the lines in the file.
    file_list = extract_data(read_file)
    
    # Gets a dictionary of all of the questions and answers.
    file_dict = organize_data(file_list)
    
    # Writes to the write file.
    output_data(file_dict, write_file)
                
    read_file.close()
    write_file.close()


if __name__ == "__main__":
    main()
