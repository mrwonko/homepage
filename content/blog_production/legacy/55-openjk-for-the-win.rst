OpenJK for the win!
###################
:date: 2014-03-15 09:31
:author: mrwonko
:category: Mixed
:tags: Jedi Academy, OpenJK, Programming, University
:type: blog
:slug: openjk-for-the-win

Small update on my exams: The remaining results are in and they did
indeed go as smoothly as it seemed at the time. That's good.

But what about my Uni projects? I said I'd like to finish at least one
of them in the past two weeks. In the beginning it went well enough and
progress was made. Then, whilst hanging out in the Jedi Academy Coder
channel #jacoders on the irc.arloria.net IRC server I was reminded that
I had once said I'd be interested in writing a new renderer for
`OpenJK <https://github.com/JACoders/OpenJK/>`__ so there was still a
name reserved for me and I was asked if that was still going to happen.

You may remember how I wrote I'd like to do some graphics programming
last week. So hell yeah, of course I was still going to write that
renderer! Bring it on!

Except OpenJK is not quite in a state where that can happen yet. Well,
it's technically possible, but right now there's still a lot of code in
the renderer that doesn't quite belong there or should at least be
shared between all renderers. Also, the Jedi Academy code base is split
in two, one for SP and one for MP. That's a lot of code duplication, and
this currently extends to the renderer, although the differences are
minimal. In short, some cleanup is due.

And now I'm the one who's cleaning. Which sounds less satisfying than it
is, because the result is worth it. I'm basically working on making
renderers easier to write and having a single one across MP and SP, as
well as getting rid of some Windows-related code in favor of SDL, which
is already used on unix anyway. In the end I'll profit by not having to
write my new renderer twice.

It's just that the uni stuff is not getting done as quickly as I had
hoped. Let's get to that in the coming weeks, eh?

So long,

Willi
