import glob, os
from Code_strength import CodeStrength
from pycparser import c_parser, c_ast, parse_file

class File_Operations(c_ast.NodeVisitor):
    def __intit__(self):
        pass

    def visit_FuncDef(self, node):
        self.func_name = node.decl.name
        self.start_line = (str(node.decl.coord)).split(":")
        print self.func_name, self.start_line
        # return self.func_name, self.start_line

    def files(self,path_c):
        self.path = path_c#raw_input("Enter the file path")#enter the path of directory of .c files manually
        os.chdir(self.path) # add the path to child directory
        file_names = []
        no_lines = []
        for file in glob.glob("*.c"):#find all the .c files in the given directory
            if file != 'output_file.c':# ignore the output_file.c
                path = self.path + '\\' + file #path of the file along with name of the .c file
                test = CodeStrength(path)#call the CodeStrength class in the Code_strength file
                no_lines_of_code = test.braces_empty_lines(self.func_name, str(self.start_line[-2]))#returns the count of lines of code in the input .c file
                file_names.append(file)#appends the .c file name to the list
                no_lines.append(no_lines_of_code)#appends the count of lines of code to the list
        return self.func_name, str(self.start_line[-2]), file_names, no_lines #return the file names and count to the called function

