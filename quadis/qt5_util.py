def plainToHTML(text, align='left', font_size=12, bold=False, italic=False,
                underline=False, color=0x000000):
    boldSettings = 'font-weight:600; ' if bold else ''
    italicSettings = 'font-style:italic; ' if italic else ''
    underlineSettings = 'text-decoration:underline; ' if underline else ''
    richText = ('<html><head/><body><p align="'+align+
               '"><span style=" font-size:'+font_size+'pt; '+boldSettings+
               italicSettings+underlineSettings+'color:#'+color+';">'+text+
               '</span></p></body></html>')
    return richText
