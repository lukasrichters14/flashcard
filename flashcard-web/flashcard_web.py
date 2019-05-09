# Developed By: Lukas Richters
# 5/9/2019
#
# Flashcard Maker
# Version 1.0
# Latest Update: 5/9/19

def open_file(f_name):
    '''Open a file given by the user.'''
    
    f_name = f_name
    
    read_file = open(f_name)
    
    return read_file


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


def output_data(file_dict):
    '''Takes the dictionary of questions and answers and then creates a string
    for output.'''
    
    file_dict = file_dict
    
    out_str = ""
    
    # Creates a string for output. This has the basic
    # formatting, only enough to differentiate the question and answer and
    # seperate cards.
    for q, a in file_dict.items():
        out_str += "{}@{}~!".format(q, a)
        out_str += "\n"
    
    # Takes off the last "\n" character.
    out_str = out_str[:-1]
    
    return out_str

    
def main(f_name):
    '''This is the overall program.'''
    
    f_name = f_name
    
    # Opens the read file.
    read_file = open_file(f_name)
    
    # Gets all the lines in the file.
    file_list = extract_data(read_file)
    
    # Gets a dictionary of all of the questions and answers.
    file_dict = organize_data(file_list)
    
    # Gets a string for the output.
    out_str = output_data(file_dict)
                
    read_file.close()
    
    return out_str
