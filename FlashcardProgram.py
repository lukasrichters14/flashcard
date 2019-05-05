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


def main():
    '''This is the overall program.'''
    
    # Open the two files.
    read_file, write_file = open_files()
    
    for i, line in enumerate(read_file):
        
        try:
            # Find where the question ends.
            question_end = line.index("?") + 1
            # Split string into question and answer.
            question = line[:question_end].lower().strip().capitalize()
            answer = line[question_end:].lower().strip().capitalize()
            
            # If the last character of the answer is not a period, add a period.
            if answer[-1] != ".":
                answer += "."
            
            # Capitalize each letter after a period in the question.
            for ind, ch in enumerate(question):
                loop = "QUESTION"
                if ch == "." and ind != (len(question)-1):
                    question = question[:ind+1] + " " + question[ind+2].capitalize() + question[ind+3:]
            
            # Capitalize each letter after a period in the answer.
            for ind2, ch2 in enumerate(answer):
                loop = "ANSWER"
                if ch2 == "." and ind2 != (len(answer)-1):
                    answer = answer[:ind2+1] + " " +answer[ind2+2].capitalize() + answer[ind2+3:]            
            # Add an @ symbol to the end of the question to differentiate between
            # question and answer on quizlet.
            question += "@"
            
            # Put everything back together to output.
            final_output = question + answer
            
            print(final_output, file=write_file)
        
        except IndexError:
            print("There was an index error at line", i, "in the", loop,"loop")
    read_file.close()
    write_file.close()


if __name__ == "__main__":
    main()
