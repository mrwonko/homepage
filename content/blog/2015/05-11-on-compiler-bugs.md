Title: on compiler bugs
date: 2015-05-11 12:40
author: mrwonko
tags: Programming, Perseus, Boost, MSVC
category: Programming
type: blog
slug: on-compiler-bugs
summary: In writing my bachelor thesis I stumble upon a bug in MSVC and lose hours.

There are still numerous older things I want to blog about, but in light of recent events I need to rant a little first.

I've recently started working on my Bachelor thesis: I'm creating a new programming language, [Perseus](https://www.github.com/mrwonko/perseus). It will be a statically typed script language, so similar to AngelScript in that regard. I have big plans for it, but limited time, so for now I'm just working on the very core.

I'll use [Boost.Spirit](http://www.boost.org/doc/libs/1_58_0/libs/spirit/doc/html/index.html) to write the Lexer and the Parser so using [Boost.Test](http://www.boost.org/doc/libs/1_58_0/libs/test/doc/html/index.html) for my unit tests was the natural choice. I quite like unit testing; besides helping to write correct programs it also allows you to see some results before it all comes together, which keeps the motivation up.

And Boost.Test is more powerful than I first thought: Yesterday it suddenly informed me I had memory leaks in my code. I had no idea it could do that, but it can indeed. So the leak hunt began.

I wasted the first couple of hours by misspelling `--detect_memory_leaks` as `--detect-memory-leaks`. How annoying. I ended up filing two bug bug reports regarding that ([one regarding warnings about invalid parameters](https://svn.boost.org/trac/boost/ticket/11279), [one regarding nonsensical parameter combinations](https://svn.boost.org/trac/boost/ticket/11278)); if I lose that much time I'll try to make sure nobody else has to.

So I finally got it to break on the allocation that was leaking. It was in the constructor of `std::vector`. Since all my dynamic memory allocation is handled by the STL (meaning there are no direct `new` or `malloc` (et al) calls) this strongly hinted at a problem with the STL, but I tried not to dismiss the possibility of me being in error too quickly. After all I'm inheritting from `std::vector` in the leaking code; maybe I went wrong somewhere with my move constructors, not calling base constructors correctly or the like.

Cue hours of debugging. You tend to look in all kinds of places when you assume obviously correct code to work. In the end it turned out that the correct code was not actually working; I had stumbled upon a compiler bug. Or so I think, [let's see what comes of it](https://connect.microsoft.com/VisualStudio/feedback/details/1322217).

Running the numbers, I think I actually lost at least 10 hours to this. How annoying, I could have gotten a lot of work done in that time.

Oh well, it's all figured out now. Back to work.

Willi
