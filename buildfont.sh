#!/bin/sh

~/code/scfbuild/bin/scfbuild -v -o testfont.ttf -g ./src/svg -s ./src/svg
./generatetestpage.py > testpage.html