import html2rest
stream = StringIO()
html2rest('<ul><li>one</li><li>two</li></ul>', writer=stream)

print(stream)