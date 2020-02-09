from cStringIO import StringIO
from tokenize import generate_tokens
STRING = 1
list(token[STRING] for token 
     in generate_tokens(StringIO('Asphalt Tech 23042014 2+24*48/32').readline)
     if token[STRING])
