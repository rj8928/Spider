import re

pattern = re.compile(r"\w+")

str = "hello 123, hello 456"

m = pattern.sub("hello world",str)
print m