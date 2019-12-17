import sys 
import re 

# Find out the counts of YES recommendation for each traveller type to see which type recommends Delta airline the most
for line in sys.stdin:
    line = line.strip()
    line = re.sub(r'[^a-zA-Z]', ' ', line)
    line = line.lower()
    words = line.split()
    if words[-1] == "yes":
        if len(words) == 3:
            print('%s\t%s' % (words[0]+ " " + words[1], 1))
        elif len(words) == 2:
            print('%s\t%s' % (words[0], 1))