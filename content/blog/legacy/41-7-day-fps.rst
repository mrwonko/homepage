7 Day FPS
#########
:date: 2012-10-07 21:44
:author: mrwonko
:category: Programming
:tags: Programming, Vlambeer, 7DFPS
:slug: 7-day-fps
:summary: My experience with 7dfps

Just though I'd write a quick post about my 7dfps Challenge experience.
One week in June, based on an idea by Indie Jwaaaap of Vlambeer, people
were challenged to create a First Person Shooter in 7 days, and I
participated. Evidently I didn't make it.

Let's start from the beginning. I started thinking about a possible
project beforehand - my first idea was a Razer Hydra motion control
based shooter where your hand movement would be mapped to weapon
control, allowing you to shoot around corners, over cover, dual wield
pistols or do the actual shotgun reloading motion. I decided to use my
WIP Jedi Academy recoding project - a lot of the things I'd need for
that FPS were things I'd need anyway, like 3D rendering and physics. And
I thought if I wanted to have any chance at getting the actual game done
within a week I should get some of the systems in a working shape
beforehand, like the rendering or the physics.

So naturally I did none of that and spent most of the week coding 3D
rendering. But my plans had changed: In the 7dfps IRC channel I had
jokingly suggested a turn-based FPS, then thought about it and realized
I was talking about `Frozen Synapse <http://www.frozensynapse.com/>`__
in first person, which seemed awesome on paper: A shooter where
everybody simultaneously records their input for the next 3 or so
seconds and then it's all evaluated. I wanted to prototype that for
7dfps.

But alas I still needed 3D rendering and physics. The rendering I got in
a working shape within that week once I realized I didn't need
animations or such fancy things, but the physics are where I got stuck.
I wanted to write a character controller from scratch to get good player
physics because restricting a rigid body (e.g. to stay upright) comes
with all kinds of problems so it's probably best to write the physics
yourself, just using the collision detection part of your physics engine
(Bullet, in my case). And that was somewhat scary.

Months later I read the following in an `interview with Valve's Erik
Wolpaw <http://www.rockpapershotgun.com/2012/09/07/story-time-with-valves-erik-wolpaw-pt-1/>`__:

    Someone at Valve said recently, “If you’re not doing something that
    scares you, you may not be doing the right thing.” At some
    fundamental level, you should be doing something that feels kinda
    scary. Like, I could fail at this.

That's true. If I want to grow I must not stick to my comfort zone,
because it consists of things I already know. So it's disappointing that
I haven't done any more work on this since then. My Jedi Academy
recoding project has not progressed in months. Which is sad. Especially
since I promised Jwaaaap, who was in the IRC channel as well, to finish
that prototype since he was eager to play it.

On the other hand writing everything from scratch *is* a lot of work.
Maybe I should prototype my ideas as mods, for example for the Source
Engine.
