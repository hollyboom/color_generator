import re

pattern = re.compile( '\s+' )
file = open( 'rgb.txt' ) 
lines = file.readlines()
row = 0
col = 0 
print "<html><table >" ;
print "<tr>"
for line in lines:
   line = line.strip()
   list = pattern.split( line , 3 ) 
   list[0] = int( list[0] ) 
   list[1] = int( list[1] ) 
   list[2] = int( list[2] )
   print "<td bgcolor='#%02x%02x%02x'><center>%s</td>" % ( int(list[0]) , int(list[1]), int(list[2]) , list[3] ) 
   col = col + 1 
   if col % 8 == 0 :
      print "</tr><tr>" 
      pass
print "</tr>"


