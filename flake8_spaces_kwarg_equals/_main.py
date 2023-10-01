import ast

__version__ = '0.1.0'


class NoSpaceAroundEqualsChecker:
    name = 'flake8-spaces-kwargs-equals'
    version = __version__

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.keyword):
                source = ast.get_source_segment(node)
                if '=' in source and ' =' not in source and '= ' not in source:
                    yield (
                        node.value.lineno,
                        node.value.col_offset,
                        "E999 No space around equals sign for keyword argument",
                        NoSpaceAroundEqualsChecker,
                    )


def get_no_space_around_equals_checker(tree, filename):
    return NoSpaceAroundEqualsChecker(tree)
