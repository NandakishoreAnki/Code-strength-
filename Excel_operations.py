from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
from xlwt import easyxf # http://pypi.python.org/pypi/xlwt
import xlwt
import os
from file_operations import File_Operations
import xlsxwriter
from pycparser import c_parser, c_ast, parse_file

class Excel_Operations():
    def __init__(self,path_x,path_c,folder):
        instance = File_Operations()# call the File_operations class in the file_operations
        ast = parse_file(path_c + '\\output_file.c', use_cpp=True, cpp_args=r'-Iutils\fake_libc_include')
        instance.visit(ast)
        func_names, no_of_lines, file_names , no_lines = instance.files(path_c)#capture the return lists in to the given variables
        wb = xlwt.Workbook()
        w_sheet = wb.add_sheet('Result')
        w_sheet.write(0, 0, 'Directory Name')
        w_sheet.write(0 , 1 , 'S.No')
        w_sheet.write(0 , 2, 'File Name')
        w_sheet.write(0, 3, 'Function name')
        w_sheet.write(0, 4, 'No of line in function')
        w_sheet.write(0 , 5 , 'Total lines of code')
        w_sheet.write(1,0, folder)
        for row_index in range(len(file_names)):
            w_sheet.write(row_index +2, 1 , row_index+1)#write the S.No
            w_sheet.write(row_index +2, 2, file_names[row_index])#Write the .c file name
            w_sheet.write(row_index + 2, 5, no_lines[row_index])  # Write the count of lines of code
            for index in range(len(func_names)):
                w_sheet.write(row_index + 2, 3, func_names[index])  # Write the .c file name
                w_sheet.write(row_index + 2, 4, no_of_lines[index])  # Write the .c file name
        wb.save(path_x)#save the excel

#start the cpnvertion