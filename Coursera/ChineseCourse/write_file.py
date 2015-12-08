#write src.txt's content to dest.txt and add two more line in the begin of file

f = open(r'src.txt', 'r')
content = f.read()

f1 = open(r'dest.txt', 'a')
str = "How many roads must a man walk down\n\nBefore they call him a man\n\n"
f1.write(str)
f1.write(content)