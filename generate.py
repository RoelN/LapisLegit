#! /usr/bin/env python

import os

svgPath = './src/svg/'

glyphs = {}

# Loop over SVG files and extract info
for filename in os.listdir(svgPath):
    if os.path.isfile(svgPath + filename):
        code = os.path.splitext(filename)[0]
        glyphs[code] = {}

        # Path and filename
        glyphs[code]['file'] = svgPath + filename

        # Character for its unicode value
        uniCode = "\u"+code
        glyphs[code]['char'] = uniCode.decode('unicode-escape')

        # Get comment describing the SVG
        with open (svgPath + filename, 'r') as myfile:
            desc = myfile.readlines()
            glyphs[code]['desc'] = desc[-2].strip()

html = ''


# <div>
#   <span class="glyph">A</span>
#   <img src="./src/svg/0041.svg">
#   <span class="info">Default glyph image: Square consisting of rows red, yellow, green, blue</span>
# </div>

for key in sorted(glyphs):
    html += '<div>'
    html += '<span class="glyph">'+ glyphs[key]['char'] +'</span>'
    html += '<img src="'+ glyphs[key]['file'] +'">'
    html += '<span class="info">'+ glyphs[key]['desc'] +'</span>'
    html += '</div>'
    html += "\n"

print """
<!DOCTYPE html>
<html>
<head>
  <title>color!</title>
  <meta charset="utf-8">
  <style type="text/css">
  @font-face {
    font-family: testfont;
    src: url("testfont.ttf");
  }

  body {
    font-family: testfont, monospace;
  }
  .glyph {
    font-size: 3em;
    line-height: 1;
  }
  div img {
    max-height: 3em;
    vertical-align: bottom;
  }
  </style>
</head>
<body>
"""

print (html)

print """
</body>
</html>
"""