#!/bin/sh

# Create font from SVG files
~/code/scfbuild/bin/scfbuild -c scfbuild-osx.yml -v -o dist/LapisLegit.ttf -g ./src/svg -s ./src/svg

# Add CPAL table
ttx -m dist/LapisLegit.ttf src/cpal.ttx
rm dist/LapisLegit.ttf
mv src/cpal.ttf dist/LapisLegit.ttf

./generatetestpage.py > testpage.html