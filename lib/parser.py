import pyparsing as pp

# define grammar
id = pp.Word(pp.alphas + '_', pp.alphanums + '_')
keyword = pp.oneOf('malware phish conceal worm ddos deepfake')
string = pp.QuotedString('"')
number = pp.pyparsing_common.number
generate = pp.Keyword('generate')
table = pp.Keyword('table')
from_ = pp.Keyword('from')
attack = pp.Keyword('attack')
defend = pp.Keyword('defend')
comment = pp.cppStyleComment
expr = pp.Forward()
expr << (id | string | number) + pp.ZeroOrMore((generate | table | from_ | attack | defend) + expr)
statement = expr + pp.Optional(comment)
program = pp.ZeroOrMore(statement)

# define parser
parser = program.parseString
