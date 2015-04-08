Review: SFML Game Development
#############################
:date: 2013-11-10 15:19
:author: mrwonko
:category: Programming
:tags: Programming, SFML, Review
:slug: review-sfml-game-development
:summary: I review SFML Game Development. Spoiler: I like it.

A while ago I was contacted by Packt Publishing. They were looking for
"SFML professionals" to review a book they had published and I assume my
activity on the SFML forums and bug tracker convinced them I fit the
bill. So I got a free sample and a request to review it. I don't get
anything except the ebook out of this.

With that out of the way, let's talk about the book! It's aptly called
`SFML Game
Development <http://www.packtpub.com/sfml-game-development/book>`__ and
is about exactly that. So, what is SFML? It's the cross-platform `Simple
and Fast Multimedia Library <http://sfml-dev.org>`__ for C++ that lets
you easily create windows, handle their events, do 2D graphics (while
allowing you to do 3D graphics using OpenGL), sound, networking and
multithreading. I've used it in numerous small projects and some
medium-sized ones and would recommend anyone starting out making games
in C++ to use it. I may personally be switching over to
`Qt <http://qt-project.org/>`__ because it's more powerful, but it's
hardly as Simple and Fast so I don't recommend it to beginners.

So that's SFML. You may want to use it. The book aims to teach you how.
What it does not teach you is C++, and rightly so, because that's a
topic worthy of its own book, and sure enough there are plenty. (I don't
know any beginner's books on C++ though since I've mostly learned
through mentors so I can't recommend any. Once you're intermediate check
out Scott Meyers.) Well, that's not entirely true. C++ recently received
a much appreciated makeover, C++11 (as in 2011). A lot of cool new
features were added and the book introduces some of them where it makes
sense, explaining what they do and why they're useful. I really liked
that since I had not previously looked into C++11 in depth.

But I liked the rest of the book as well. It iteratively adds onto the
same game (a Shmup), resulting in a playable prototype at the end of
each chapter. All of SFML's major components are used and explained, but
you could just read the API documentation to learn about those. No, the
important thing is that you learn how to build a game with them: Yes,
just loading a texture is fairly simple, but how do you manage all the
textures in your level? Drawing a sprite is easy, but what's a
reasonable way of storing them for easy manipulation? How do you make
the keys customizable? How do you manage multiple states like menus, the
game itself and a pause screen? The book's so helpful because it answers
these questions in addition to teaching SFML.

One thing to keep in mind is that there are often multiple solutions to
a given problem. When the book presented Entity hierarchies as the way
to go I thought to myself: "Yes, they work for simple games like this
one, but once the hierarchy grows you run into all kinds of trouble. A
component-based system might be better in some cases." But then sure
enough the next paragraph explained that hierarchies aren't the only way
and mentioned component-based systems as one alternative. And that's not
the only place where the book mentions alternatives, there are multiple
links to further material for those interested. Being aware of ones
limits is important and this book certainly is aware of them and makes
you aware, too. Take shaders, for example: It explains them on a high
level but does not go into explaining the rendering pipeline, that's
simply outside of the book's scope, and that's okay since it's open
about it.

So in conclusion what makes this book valuable is not that it teaches
you how to use SFML, but how to program a game with it. And it's also a
nice introduction to some of C++11. If you know C++ and want to make
games with it, this is probably the book for you.
