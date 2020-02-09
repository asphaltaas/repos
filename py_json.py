import csv
import json
f = open( 'data.csv', 'r' )
reader = csv.DictReader( f, fieldnames = ( "subject","branch","book","chapter","encode","l1","l2","l3","l4" ) )
out = json.dumps( [ row for row in reader ] )
print out
