Title: ROFF - the Raven Object File Format reverse engineered
date: 2010-07-27 19:45
modified: 2015-04-08 15:15
author: mrwonko
tags: Blender, Jedi Academy, Modelling, Programming, broken link
:category: Programming
slug: roff-the-raven-object-file-format-reverse-engineered
summary: Today I've had a closer look at the ROFF file format used in some older Raven Software games...

Did you know that Raven Software included information on the Ghoul 2
model and animation file format in the Jedi Knight 2: Jedi Outcast SDK?
I didn't until yesterday or so.

I was looking for information on the format because I'd like to write
im- and exporters for Blender. As you may or may not know I'm a Jedi
Knight: Jedi Academy  modder and I've been one since it first came out.
That's how I came to be a programmer actually, because they released
their multiplayer sourcecode.

Anyway, once I had the information on Ghoul 2 GLM & GLA I was pretty
happy. "What file formats do I not know about yet?", I asked myself. The
.efx effect files are pretty straight-forward since they're plain text.
The same applies for the botroute .wnt files. Compiled scripts, .ibi
files, are a little harder since they're binary, but I can just write a
lot of scripts and analyze the compiler's output. But I didn't know what
to do with the .rof files.

ROFF, or Raven Object File Format, contains complex animations for level
geometry. A couple of older Raven Software games, including Jedi Knight:
Jedi Academy and Jedi Knight 2: Jedi Outcast, use it e.g. for rolling
rocks, flying spaceships and camera paths.

There's an exporter for 3D Studio Max 4 & 5 which exports ROFF
animations, Raven released that. But I don't have 3D Studio Max, and if
I had it, I wouldn't have such an old version. I prefer
[Blender](http://www.blender.org) though, it's free and open source.

So I looked at the .rof files using a hexeditor, the [hex editor
plugin](http://sourceforge.net/projects/npp-plugins/files/Hex%20Editor/)
for [Notepad++](http://notepad-plus-plus.org/) to be precise. The
beginning, "ROFF", was obviously the identifier. Guessing that the
following integer 2 was the version wasn't that hard, either. I wasn't
sure, but I supposed the next integer would be the total number of
frames since it was bigger when the file was bigger. Using some basic
math I could prove my theory and calculate a size of 20 bytes for the
header and 32 bytes per frame.

So what are the remaining 8 bytes in the header? The first 4 are the
time per frame in milliseconds as an integer, e.g. 50 (ms) for 20 fps. I
still don't know what the other 4 bytes in the header are, but I didn't
worry about them since they're always the same. Instead I looked at the
remaining 32 bytes. Since they were supposed to represent movement I
suspected them to be floats. Thus I wrote a little python script to read
them as floats and save them in a csv. I could then look at them in
[OpenOffice.org](http://www.openoffice.org/) Calc. The last two rows
were always `nan` and `0`. They're probably actually ints, at least `-1`
makes more sense to me than `nan`. I still can't tell what they are, but
I don't really care.

Instead I looked at the remaining 6 floats. They should be position and
rotation, and they were. Once I saw these values in the 6th row of one
file I was pretty sure it was a rotation:

```
30.1187744141
-329.881225586
30.1187744141
```

I thought they were absolute positions and 360° = 0°. It later turned
out that they were actually relative movements since the last frame, but
I had to write the exporter and do a test export to notice that. And
that's what I did next, writing the im- and exporter. The order of the
rows turned out to be deltaLocationX, deltaLocationY, deltaLocationZ,
deltaRotationY, deltaRotationZ and deltaRotationX.

So eventually I was done and the result can be downloaded [on this very
website](../downloads/view.php?id=22). There's an [example on
youtube](http://www.youtube.com/watch?v=t6JISk-h1cs).

And I'm happy.

Willi

**Appendix**

I just found out that the Elite Force SP Mod Code contains the source to
the ROFF format. ROFF is actually an abbreviation for "Rotation, Origin
File Format" and the number of frames was a float in version 1, but that
is apparently no longer the case. The header used to be only 12 bytes
long so I still don't know about the last 8 bytes, and there's no
information on the last 8 bytes of the frames either.

**Appendix 2**

Since Jedi Academy's source code has since been released, I urge anybody looking for information on the file format to consult that instead.
