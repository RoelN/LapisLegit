#! /usr/bin/env python

import os
import random

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
            svgContent = myfile.readlines()
            glyphs[code]['content'] = ''.join(svgContent)
            glyphs[code]['desc'] = svgContent[-2].strip()

# Create a test block for each glyph
html = ''
for key in sorted(glyphs):
    html += '<div>'
    html += '<span class="glyph">'+ glyphs[key]['char'] +'</span>'
    html += '<img class="image" src="'+ glyphs[key]['file'] +'">'
    html += glyphs[key]['content']
    html += '<span class="info">'+ key +': '+ glyphs[key]['desc'] +'</span>'
    html += '</div>'
    html += "\n"

# Barf out the HTML for the test page
print """
<!DOCTYPE html>
<html>
<head>
  <title>LapisLegit!</title>
  <meta charset="utf-8">
  <style type="text/css">
  @font-face {
    font-family: LapisLegit;
    src: url("dist/LapisLegit.ttf?v=""" + repr(random.random()) + """");
  }
  div {
    margin: 20px;
  }
  .glyph {
    font-family: LapisLegit, monospace;
    font-size: 3em;
    line-height: 1;
    margin-right: 20px;
  }
  svg,
  .image {
    width: 3em;
    vertical-align: bottom;
    margin-right: 20px;
  }
  </style>
</head>
<body>
<h1>LapisLegit, a font to test the OpenType SVG table</h1>
<p>By <a href="https://twitter.com/pixelambacht">Roel Nieskens</a>. More info on <a href="https://github.com/RoelN/LapisLegit">Github</a>!</p>
<p>Order of images: font glyph, SVG as image tag, SVG inlined.</p>
<hr>
"""

print (html)

print """
</body>
</html>
"""