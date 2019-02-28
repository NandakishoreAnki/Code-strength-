from pycparser import c_parser, c_ast, parse_file

ast = parse_file(r"C:\nandu\work\output_file.c", use_cpp=True, cpp_args=r'-Iutils\fake_libc_include')

class FuncDefVisitor(c_ast.NodeVisitor):
    def visit_FuncDef(self, node):
        self.func_name = node.decl.name
        self.start_line = (str(node.decl.coord)).split(":")
        print self.func_name, self.start_line[-2]
v = FuncDefVisitor()
v.visit(ast)