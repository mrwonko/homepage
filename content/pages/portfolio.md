title: portfolio
save_as: portfolio.html
url: portfolio.html
page-order: 20

Here are some of the things I've made.

# This Website

Built using [Pelican](http://blog.getpelican.com/) from [this Github repo](https://github.com/mrwonko/homepage/) with a custom plugin to allow different types of articles (blog, downloads, tutorials) and a custom theme with a Python backend for comments.

# Perseus Compiler & VM

For my Bachelor thesis I wrote a [compiler and virtual machine for a subset of a programming language of my design](https://github.com/mrwonko/perseus) in modern C++ using Boost.Spirit. It currently does little more than integer arithmetic, but with continued work I hope to one day have a useful embedded language for scripts in video games with unique serialization capabilities.

# Various Jedi Knight: Jedi Academy modding

Back in 2003 I got into modding; first with Jedi Knight 2: Jedi Outcast, then its sequel Jedi Academy. Over the years I learned about the basics of level design, scripting, materials, modelling, rigging, animation and eventually coding. The visible results are [a small level here](http://mrwonko.de/jk3files/Jedi%20Academy/Maps/Multiple%20Gamemodes/64416/) and [a new player model there](http://jkhub.org/files/file/5-fluttershy/), but never anything large; the most important result is the broad knowledge I gained, I just had not learned to finish projects at that time.

In any case I found coding to be more to my liking so I started working on tools instead of content. In particular Blender, my modelling tool of choice, lacked support for Jedi Academy's player model and animation formats, but can be extended through Python plugins. So I compiled [a suite of plugins](http://jkhub.org/files/file/1413-blender-264-jedi-academy-plugin-suite/) - some written from scratch, others modified existing scripts - for working with Jedi Academy related formats. I also wrote [a tutorial on using it to create new vehicles](http://jkhub.org/tutorials/article/127-creating-new-vehicles-with-blender/).

Later Jedi Academy's source code was released; I'm now part of a team maintaining it in a project called [OpenJK](https://github.com/JACoders/OpenJK). We aim to fix bugs and enhance the game while maintaining binary compatibility with existing mods.

# Octarine Optimizer - Same Game Solver

Made for a programming competition at university where it placed first, this multithreaded C++ game AI finds high-scoring solutions for [the Same Game](http://www.factmonster.com/games/samegame.html) (albeit with slightly different scoring).

[Github Repo](https://github.com/mrwonko/pwb2015/)

# PPHPBB2 to HTML

While archiving an old PHPBB2 forum I wanted to render it to static HTML; to this end I wrote a small [Python app](https://github.com/mrwonko/phpbb2_to_html) that connects to a MySQL database and renders its contents using Jinja2.

# Razer Hydra DirectInput Virtual Gamepad

The Razer Hydra is a motion controller for the PC. The bundled software allows you to map motions to your mouse and keyboard so games without direct support can still be played with it, but mapping 6 axes (plus trigger and analog sticks, and all of that twice; once for each hand) to only 2 analog axes (mouse movement) and buttons is such a waste.

So I wrote a tool that allows you to map the axes and buttons to a virtual gamepad. It allows you to freely configure which kind of movement should be mapped to which axis (or button, if desired).

[Website](http://sixense.com/forum/vbulletin/showthread.php?3203-DirectInput-virtual-gamepad-%28version-0-4f%29)

# <Watch this space>

I've just started working on a small action platformer; I plan to release a playable prototype by mid-November.

# Github

Also check out my [Github profile](https://github.com/mrwonko) for an assortment of other projects.
