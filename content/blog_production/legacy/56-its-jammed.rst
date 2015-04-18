It's jammed!
############
:date: 2014-04-01 13:05
:author: mrwonko
:category: Mixed
:tags: Programming, University
:type: blog
:slug: its-jammed
:summary: I went to a game jam and wrote a (de)serialization library.

So I did not write this update on Saturday. What happened?

The InnoGames Game Jam happened. I joined a group of artists and spent
Saturday morning to Sunday noon coding nonstop. 3.3KLOC later we had `a
simple platformer <https://github.com/mrwonko/IGJam6Platformer>`__.

It only came together in the last hours and still lacked the enemies and
collectibles. Why? Because I still haven't really looked into premade
engines, instead resorting to coding everything myself. I either need a
personal codebase that I can reuse or get into some engine.

But on the bright side I finally got to write a component based entity
system, something I had wanted to do for quite a while. Worked out okay,
but I'm wondering if something like Haskell's Typeclasses might be
better. With C++14 and Concepts something similar may be possible, but
I'm not sure what to think about template-based entities... Either way
gamejams are a great place to do these weird experiments.

So I got to use some C++11, especially Lambdas and std::function for
callbacks and unique\_ptr and shared\_ptr - although I probably overused
the latter to "fix" my order-of-destruction problems. And I already made
extensive use of another C++11 feature last week: Variadic templates.

How so? I wrote a small library for function call
serialization/deserialization, which I dubbed
`SimpleRPC <https://github.com/mrwonko/SimpleRPC>`__. It doesn't care
about endianness because it's meant for local inter-process
communication.

Why would I need that? Because the GPL is impractical. I see its point
and kind of support it - in a perfect world it would be the ideal
license. But we don't live in a perfect world and some functionality is
only available in proprietary, GPL-incompatible libraries. In order to
be able to use those inter-process communication is necessary. It's
still against the spirit of the GPL I suppose... Oh well. For the most
part I was just interested in coding the library, I don't know if I'll
actually use it.

So what's next? I still have some Uni work to finish this week, and next
week I'll go to A MAZE in Berlin. If I have time for anything else I'll
probably continue my work on OpenJK cleanup.

So long,

Willi
