import ply.lex as lex

tokens = (
  'VERB'
  )

def t_VERB(token):
  r'is|am|are|were|was|be|being|been|do|does|did|will|would|should|can|could|has|have|had|go'
  return token

t_ignore = r' '


print("ply.lex masquerading as lex")