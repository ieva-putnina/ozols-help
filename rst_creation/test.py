from html2rest import html2rest
from io import BytesIO as StringIO
stream = StringIO()
f = open("test.txt", "r")
html = f.read()
#stream = ""
html2rest(html, writer = stream)

rst = stream.getvalue().decode("utf8")
print(rst)
