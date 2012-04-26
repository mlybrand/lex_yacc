import ply.lex as lex

tokens = (
  'VERB',
  'NONVERB',
  'DEFAULT'
  )

t_ignore = ' '

def t_VERB(token):
  r'is|am|are|were|was|be|being|been|do|does|did|will|would|should|can|could|has|have|had|go'
  print(token.value + " is a verb")
  return token

def t_NONVERB(token):
  r'[a-zA-Z]+'
  print(token.value + " is not a verb")
  return token

def t_DEFAULT(token):
  r'.|\n'
  print(token.value)
  return token

def t_error(token):
  token.lexer.skip(1)

example1 = 'did I have fun?'

lexer = lex.lex()
lexer.input(example1)
while True:
  tok = lexer.token()
  if not tok: break
  #print(tok)

