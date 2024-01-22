y={'John':40,'Alex':2,'Benny':32,'Danny':3}
l=list(y.items())
l.sort()
print("ascending order is",l)
l=list(y.items())
l.sort(reverse=True)
print("descending order is",l)
