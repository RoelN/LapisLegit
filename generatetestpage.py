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
    character = glyphs[key]['char']
    if character == "Q":
        # Crashes Firefox, so show safe character
        character = "!"
    html += '<tr>'
    html += '<td class="glyph" contenteditable>'+ character +'</td>'
    html += '<td class="image"><img src="'+ glyphs[key]['file'] +'?v='+ repr(random.random()) +'"></td>'
    html += '<td class="inline">'+ glyphs[key]['content'] +'</td>'
    html += '<td class="info"><a href="'+ glyphs[key]['file'] +'">'+ key +'</a>'
    html += ' ('+ glyphs[key]['char'] +'): '+ glyphs[key]['desc'] +'</td>'
    html += '</tr>'
    html += "\n"

# Barf out the HTML for the test page
print """
<!DOCTYPE html>
<html>
<head>
  <title>LapisLegit, a font to test the OpenType SVG table</title>
  <meta charset="utf-8">
  <style type="text/css">
  @font-face {
    font-family: LapisLegit;
    src: url("dist/LapisLegit.ttf?v=""" + repr(random.random()) + """");
  }
  th {
    text-align: left;
  }
  .glyph,
  .inline,
  .image {
    weidth: 3em;
    padding: 10px 40px 10px 0;
  }
  .glyph {
    font-family: LapisLegit, monospace;
    font-size: 3em;
    line-height: 1;
  }
  .inline svg,
  .image img {
    width: 3em;
    vertical-align: bottom;
  }
  </style>
</head>
<body>
<h1>LapisLegit, a font to test the OpenType SVG table</h1>
<p>By <a href="https://twitter.com/pixelambacht">Roel Nieskens</a>. More info on <a href="https://github.com/RoelN/LapisLegit">Github</a>!</p>
<p>If you see black squares or nothing in the first column, your browser doesn't <a href="https://pixelambacht.nl/2014/multicolor-fonts/">support OpenType SVG</a> yet.</p>
<p><em>At this moment, some glyphs cause browsers to crash. A "!" will be shown instead of the letter. Click and select the cell to enter the characters yourself... if you dare!</em></p>
<hr>
<table>
  <tr>
    <th>Glyph</th>
    <th>Image</th>
    <th>Inline</th>
    <th>Description</th>
  </tr>
"""

print (html)

print """
</table>
</body>
</html>
"""