class Visitor:
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        method = getattr(self, method_name, None)
        if method is None:
            raise NotImplementedError(f'No visit_{type(node).__name__} method')
        return method(node)

    def visit_Malware(self, node):
        return 'malware'

    def visit_Phis(self, node):
        return 'phish'

    def visit_Conceal(self, node):
        return 'conceal'

    def visit_Worm(self, node):
        return 'worm'

    def visit_Ddos(self, node):
        return 'ddos'

    def visit_Deepfake(self, node):
        return 'deepfake'

    def visit_Generate(self, node):
        return 'generate'

    def visit_Table(self, node):
        return 'table'

    def visit_From(self, node):
        return 'from'

    def visit_Attack(self, node):
        return 'attack'

    def visit_Defend(self, node):
        return 'defend'

    def visit_String(self, node):
        return node.value

    def visit_Number(self, node):
        return node.value

    def visit_Identifier(self, node):
        return node.value
