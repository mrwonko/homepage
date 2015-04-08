I've been silent - because I was busy.
######################################
:date: 2010-10-02 09:37
:author: mrwonko
:category: Mixed
:tags: Blender, Modelling, Programming, School, Valve
:slug: ive-been-silent-because-i-was-busy
:summary: I've been busy: Creating a music video, programming a wildfire simulation and planning a class trip...

As you may or may not have noticed I didn't write anything for over a
month. That may partially be due to my lazyness, but it's also because I
was busy (i.e. not lazy).

On September 1st, Valve started a
`contest <http://www.midnight-riders.com/videocontest/index.html>`__:
Create a music video for the song "Save me Some Sugar" by the (fictional)
Band "the Midnight Riders". That's right, Valve invented a band, and
they actually wrote and performed songs for the band. And now they let
the fans create music videos. I was one of those who did that.

I had actually lost motivation half-way through when many good entries
started appearing and Darksiders arrived. Then, on the 28th September,
Chet Faliszek, a Valve employee, wrote this:

    Damn, these are getting really good as we near the finish. Remember
    the contest ends the 1st. With this many great entries I think we
    are going to have to give away more than just one prize. Will have
    to see if the Riders left anything else behind...

That motivated me to try and finish my video. I barely had any time
left, so I started cutting the song to shorten it. In the end I barely
finished and learned quite some things. For example that render time
shouldn't be underestimated, that you should check that all objects are
set to be rendered before rendering 1000 frames (luckily I could get
away with only re-rendering the missing object, a spotlight) and that
playing Darksiders is way more fun than creating a video. More on
Darksiders once I've finished it.

Anyway, here's the video:

.. raw:: html

   <p>
   <object width="425" height="344">
   <embed src="http://www.youtube.com/v/BYRtfJ5iShI?hl=de&amp;fs=1" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="425" height="344">
   </embed>
   </object>
   </p>

At least I didn't have to do any homeworks this week (don't let my
teachers hear that, I think I was supposed to do them anyway...) because
I participated in the "Mathematische Modellierungswoche" (roughly
translates as "mathematical modelling week") and couldn't/didn't have to
go to school.

The goal of the Modellierungswoche is to solve one of 4 given problems
by creating a mathematical model. The problems available were:

-  How to fight wildfires using swaths
-  How to rate decathlons
-  Planning a wind farm
-  Should you turn the heating off during the night?

We picked the first one. I liked it because I thought I could program a
fire simulation and that's what I did. That doesn't include swaths, but
Bernd did some swath related calculations as well.

The simulation is simplified, of course, and the values used may not be
close to reality, but it works and you can watch fires spread. It's
written in Lua, using SFML via luabind.

It's great how many things can be easily done in Lua, on the other hand
the dynamic typing can be a PITA, especially when debugging. Well, I got
the job done and there are no bugs I know of. (Of course that doesn't
necessarily mean there are no bugs.)

The Fire Simulation `can be downloaded
here <http://mrwonko.de/downloads/view.php?id=23>`__.

Next week I'll be in Amsterdam with my class. We're going to visit
museums and stuff, but I'm looking forward most to my planned visit to
the Blender Foundation. I'll write more about that once I'm back.
