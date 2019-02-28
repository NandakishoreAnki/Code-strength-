import re, os

class CodeStrength():
    def __init__(self, fname):
        "Constructor: Called when the CodeStrength object is created"
        source_code = open(fname, 'r').readlines() # Read all the lines of .c file
        source_code = "\n".join(str(x) for x in source_code) # convert the all the lines into elements of the list
        self.file = open('output_file.c',"r+") #Open an output_file.c file for writing code without comments
        self.removeCCppComment(source_code)#Removes all the comments

    def removeCCppComment(self, text):

        def blotOutNonNewlines( strIn ) :  # Return a string containing only the newline chars contained in strIn
            return "" + ("\n" * strIn.count('\n'))

        def replacer( match ) :
            s = match.group(0)
            if s.startswith('/'):  # Matched string is //...EOL or /*...*/  ==> Blot out all non-newline chars
                return blotOutNonNewlines(s)
            else:                  # Matched string is '...' or "..."  ==> Keep unchanged
                return s

        pattern = re.compile(
            r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
            re.DOTALL | re.MULTILINE
        )
        line = re.sub(pattern, replacer, text) # code without comments is returned
        self.file.write(line)# Write the code without comments to output_file.c
        self.file.close()#close the file
        self.remove_empty_lines('output_file.c')#Removes empty lines

    def remove_empty_lines(self,filename):
        if not os.path.isfile(filename):
            print("{} does not exist ".format(filename))#check for the existance of the file
            return
        with open(filename) as filehandle:
            lines = filehandle.readlines()#read all the lines

        with open(filename , 'w') as filehandle:
            lines = filter(lambda x: x.strip() , lines)#filter out all the new lines
            filehandle.writelines(lines)#write the lines without \n to the output_file.c

    def braces_empty_lines(self, fun_name, no_of_lines):
        braces_empty_count = 0
        num_lines = 0
        file = open('output_file.c','r')#open the output_file.c for the braces count
        for line in file:#loop for each line
            num_lines +=1
            line = line.strip()#removes the spaces from lines
            if line == '};' or line == '}' or line == '{':#find the braces
                braces_empty_count += 1#imcrement the braces count
        return num_lines - braces_empty_count# return the count of lines of code in the input file

    def Get_lines_func(self, func_name, no_of_lines):
        file = open('output_file.c', 'r')  # open the output_file.c for the braces count
        num_lines,num_func_lines = 0
        for i in func_name:
            for line in file:#loop for each line
                num_lines += 1
                if i in line:
                    num_lines
