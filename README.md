# LapisLegit, a font to test the OpenType SVG table

LapisLegit is a font to test implementations of the [OpenType 'SVG ' table](https://www.microsoft.com/typography/otspec/svg.htm) with. It's not an actual typeface, but contains characters that try (to break) different features of SVG in OpenType. Use this to check for bugs or performance issues in software that implements OpenType's SVG table.

## How to use

Run `./buildfont.sh` to generate the font and an HTML test page. It uses [scfbuild](https://github.com/eosrei/scfbuild/) to generate the font, and some high tech computer science to generate the HTML. Open the page in your browser: on the left is the SVG-in-OpenType glyph, followed by the original SVG image, followed by a short description of what's happening in that glyph.

## What does "LapisLegit" mean?

Lapis legit is a frigging [delicious cake made of colorful layers](https://www.google.com/search?tbm=isch&q=lapis+legit)!

## License

LapisLegit is released under the [MIT license](https://github.com/RoelN/LapisLegit/blob/master/LICENSE.md).
