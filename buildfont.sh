#!/bin/sh

~/code/scfbuild/bin/scfbuild -c scfbuild-osx.yml -v -o dist/LapisLegit.ttf -g ./src/svg -s ./src/svg
./generatetestpage.py > testpage.html