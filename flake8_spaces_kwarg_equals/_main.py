import ast

__version__ = '0.1.0'


class NoSpaceAroundEqualsChecker:
    name = 'flake8-plugin-kwargs-spaces'
    version = __version__

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    def run(self):
        with open(self.filename, 'r', encoding = 'utf-8') as file:
            source = file.read()

        for node in ast.walk(self.tree):
            if isinstance(node, ast.keyword):
                segment = ast.get_source_segment(source, node)
                if (
                    '=' in segment and
                    ' =' not in segment and
                    '= ' not in segment
                ):
                    yield (
                        node.value.lineno,
                        node.value.col_offset,
                        (
                            "CE101 No space around equals sign "
                            "for keyword argument"
                        ),
                        NoSpaceAroundEqualsChecker,
                    )


def get_no_space_around_equals_checker(tree, filename):
    return NoSpaceAroundEqualsChecker(tree, filename = filename)
