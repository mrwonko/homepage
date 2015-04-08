Sometimes I can't think of a good title.
########################################
:date: 2011-12-08 23:44
:author: mrwonko
:category: Mixed
:tags: Blender, Jedi Academy, Jedi Academy: Renaissance, Modelling, Programming, University, Videogames, Trine 2, MD3View
:slug: sometimes-i-cant-think-of-a-good-title

What am I up to recently? Quite a lot, apparently, judging from `my
Github profile <https://github.com/mrwonko/>`__.

I wrote a console based `Tetris in
Pascal <https://github.com/mrwonko/willis-pascal-tetris>`__ for Uni -
that keeps me from having to do the programming lessons, which means
free Mondays. No particularly big project, but probably the one with
the most obvious effect.

Then there's some Jedi Academy stuff. The community may be dying, but
it's not quite dead yet. Almost, but not quite. Won't keep me from
working on it though. In particular I've been trying to model a sword in
Blender 2.6a. I had to fix some bugs in an `md3
exporter <http://www.mrwonko.de/downloads/view.php?id=33>`__ and
`md3view <https://github.com/mrwonko/MD3View>`__ (`whose sources I
luckily acquired last
year <http://sandervanrossen.blogspot.com/2010/05/md3view.html>`__)
first, but I did make it eventually.

The latter - md3view - is required for converting the md3 to a ghoul 2
model (.glm) as used by Raven's Quake 3 engine based games. It would be
much simpler if you could directly export those from Blender, and `I've
been working on that as
well <https://github.com/mrwonko/Blender-2.6-Ghoul-2-addon>`__. So far I
can import the complete format but the exporter is a work in progress at
best. I'm writing it with my Renaissance project in mind - it could be
used to import a model, UV map it again (so there's no mirroring) and
create a hipoly version for normal/height baking. Because I'd like to
eventually add normal- and parallax occlusion mapping to my engine.

Once he heard `I had compiled GTK Radiant
1.6 <http://www.mrwonko.de/downloads/view.php?id=28>`__, Darth-Arth
requested I did some changes. We're still working on Spirits of the
Sith, a Jedi Academy SP mod, after all. Actually, I'm hardly
contributing at the moment, so anything coding related is the least I
can do. (My ghoul 2 importer already was of use, too.) So `I made some
changes <http://www.mrwonko.de/downloads/view.php?id=30>`__, and while I
have no problem with making my sources available anyway I did not even
have a choice here once I published binaries, it's GPL after all. `So my
changes are available on
sourceforge <https://sourceforge.net/p/gtkradiantfork/home/Home/>`__. (I
did not want to put such a huge project on Github, I think my space
there is limited.)

The thing that's most important to me is me working on Jedi Academy:
Renaissance again, though. I won't get this done if I don't work on it.

Well, I don't suppose working on a .ibi to lua converter is the correct
way of getting it done when you don't even have a menu system yet, but I
keep doing little things, tech demos pretty much, because those are more
interesting than designing a menu system.

Luckily, I've just thought of an interesting "side project" that will
actually be useful for creating the menu system - a new renderer. So
far, I'm using `SFML <http://www.sfml-dev.org>`__'s graphic part, which
has pretty nice 2D rendering features - sprites, including image
loading, and texts are the things I need in my engine as well. I've
already written my own font/text rendering using Jedi Academy's image +
.fontdat format though (even if it currently is an extension to SFML,
extending its classes and using its renderer) and I need multitexture
fragment shaders - I'm not sure I can do that using SFML. Besides, I'd
like to be able to use all that in GTK as well (writing e.g. a
modelviewer using my renderer so it looks just like ingame).

So I'll be rewriting the rendering, mostly using pure OpenGL 2.0 with
some GLU and GLEW mixed in. I'll start by trying to replicate Quake 3's
"shaders" using fragment shaders, which should be both faster and more
powerful. Since it'll probably take me over a week to get the renderer
in a usable state, I'll need a backup of my engine in case I want to use
it for Ludum Dare next weekend. That's right, there's another "make a
game this weekend, here's the theme" contest incoming.

So I looked into git tagging and branching. I started by tagging the
current version as the LD22Fallback, but then I found out I actually
want branches. From what I learned so far, they're damn powerful,
allowing you to change the state of your current working directory with
a single command (git checkout <branchname>). So I'll be working in a
new branch "renderer" while leaving the master branch untouched for
Ludum Dare. Actually, I'll probably start a Ludum Dare branch. You can
probably synchronize commits between changes, e.g. pulling a bugfix or
new feature from the master branch to the renderer branch and in general
this seems perfect for trying out different things in a safe
environment.

Oh, and I got a Razer Hydra when they were on sale during the Black
Friday weekend - I'll have to do some coding with them, too. Using them
to play "ordinary" games works reasonably well, but games made for them
is where they'll shine. (I'm using plural since there are two
controllers.)

And I got myself Trine 2, which once again had beautiful music. To get
it, I needed to first unpack the archive, then use two converters
(ww2ogg and revorb) and batch rename the resulting files
(\*.ogg\_conv.ogg) - the bash proved very useful for this. (I'm using
the git bash on Windows - I have to fix my MBR and boot into Ubuntu to
test my Engine there some time soon though.)

So that's what I've been up to. In the coming weeks I'll probably be
working on Renaissance, the Ghoul 2 exporter for Blender and possibly
some other Jedi Academy related tools

So long,

Willi
