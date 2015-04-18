coding again
############
:date: 2010-11-24 21:58
:author: mrwonko
:category: Mixed
:tags: Jedi Academy: Renaissance, Programming, Videogames
:type: blog
:slug: coding-again
:summary: I'm working on a new big coding project!

Hello blog readers,

I'm being productive again. I still play games (recently started Mini
Ninjas again - I lost my savegames earlier) and stuff but I'm also
coding some more.

What am I coding? My ultimate goal is recoding Jedi Academy. By now it
seems pretty unlikely Raven/Activision are ever going to release all the
sourcecode and even if they did I'd try a rewrite, since I prefer a
C++/Lua combination over C.

Lua? What's my goal? Having started my coding career as a mapper/modder
I keep modders in mind. I want the game to be highly extendible. At the
moment Jedi Academy MP mods can modify a dll, and since only one dll is
loaded only one such mod can be active at any moment. With Lua many mods
could be active simultaneously.

Besides making it more moddable I'd also like to improve the engine,
adding a physics engine (possibly DMM2 once it's released for free) and
stuff like pixel shaders and all that next gen stuff, but those are
long-term goals and first I'd like to have aa game capable of using
(most of) Jedi Academy's assets with a similar gameplay. (Luckily the mp
gameplay parts of the code are released.)

I've started working on that recode. It's a massive project and I'm not
going to code the whole thing at once. Instead I'll write many
increasingly complex applications, keeping the same framework and
extending it.

Since I also want to look into OpenCL I'll start with a 2-dimensional
gravity simulation, i.e. having a couple of (or many) planets with
gravity. I'm going to implement it both in C++ and in OpenCL so I can
measure the difference - so while I'm at it I might want to code a
profiler, too.

For that simulation I need some more features though. This is what I've
got so far:

-  Keyboard input (Windows) / Event-System
-  PhysFS-based filesystem that can handle mods
-  Lua support
-  CVars (Console Variables)
-  Logging - there aren't many kinds of loggers so far, but I'll add
   more later.

I'll need some more for the simulation:

-  Commands, i.e. the actions that happen when a key is pressed (or its
   name is entered in the console)
-  a window (will use SFML)
-  OpenCL integration of some kind
-  (console)
-  (profiler)

Now that I've listed them - it's not that much actually! I probably
forgot something, but still... May have this done by the end of this
week? Probably not...

In other news, I've managed to fill my 1.25TB of HDD space, only have
about 50GB free space in total left. Instead of doing some cleanup I
bought an additional 2TB and a pc case because the self-built case I
currently use has no space for additional hard disks, or additional
anything really. Will this be my comeback as a casemodder? Time will
tell...

And there's another sale at Steam. I just bought Sam & Max: Season
3, now I only need Season 2 since I'd like to play them in the right
order.

So long,

Willi
