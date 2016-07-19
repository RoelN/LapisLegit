# LapisLegit, a font to test the OpenType SVG table

LapisLegit is a font to test implementations of the [OpenType 'SVG ' table](https://www.microsoft.com/typography/otspec/svg.htm) with. It's not an actual typeface, but contains characters that try (to break) different features of SVG in OpenType. Use this to stress-test and check for bugs or performance issues in software that implements OpenType's SVG table.

## See it in action

You can check the [online version of the LapisLegit test page](https://pixelambacht.nl/lapislegit/) to see how your browser handles all these weird SVGs.

## How to use

Run `./buildfont.sh` to generate the font and an HTML test page. It uses [scfbuild](https://github.com/eosrei/scfbuild/) to generate the font, and some high tech computer science to generate the HTML. Open the page in your browser and see the differences in implementation when the SVG is shown as an OpenType glyph, image tag, or inlined SVG document.

## What does "LapisLegit" mean?

Lapis legit is a [frigging delicious cake made of colorful layers](https://www.google.com/search?tbm=isch&q=lapis+legit)!

## License

LapisLegit is released under the [MIT license](https://github.com/RoelN/LapisLegit/blob/master/LICENSE.md).
