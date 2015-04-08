screwing up Windows
###################
:date: 2011-10-24 19:13
:author: mrwonko
:category: Mixed
:tags: Computer, Programming, University, GTA
:slug: screwing-up-windows
:summary: I fiddle with Windows' registry. I break stuff. I install Ubuntu and try to fix stuff. I should code Tetris.

As you may or may not know, getting Windows to not boot anymore is not
hard. Doing it accidentally is a little harder, but I managed to do it
nonetheless.

One of the [STRIKEOUT:current] last (this post is taking longer than
expected and I keep getting sidetracked) Weekend Deals on Steam
[STRIKEOUT:is] was the GTA complete Pack for 5 pounds. Needless to say I
bought it (i.e. got a British friend to buy it for me - it's neither
available in Germany, nor is it as cheap in €), despite 1 and 2 being
available for free and already owning 4. I was later shocked to find out
that its being uncut reportedly depends on the system language - Germans
get the cut version.

In theory that's easily fixed, of course: Change the language to
English. I meant to do that for quite some time since I like English.
Trying it once again I remembered why I didn't already do it - you need
Windows 7 Ultimate to be allowed to. But you can circumvent this by
downloading the language package and changing the registry - I changed
the registry first since that's obviously less legally questionable,
then looked for a way of legally acquiring the language pack and didn't
find one.

So I looked for other ways of acquiring an English Windows - an Upgrade
to Ultimate would cost me €190, as opposed to $140 in the US - almost as
unfair a pricing difference as Steam's other Weekend Deal, Alice:
Madness Returns, which costs €25 as opposed to $15. (Needless to say I
acquired it through a US contact.) Even $140 is too much for my liking
though, since I really don't need any of the other features Ultimate
has.

Then I remembered I'm a student now. There are special student deals.
Unluckily no Home Premium -> Ultimate upgrades, but I could get a
Professional upgrade for as little as €35, though I don't know if that's
available in English. (Incomprehensibly the US price is $65 and not
something ridiculously cheap as one might expect after the previous
differences...)  Actually, since the FH Wedel takes part in the MSDNAA
program, I can get it for free. In English, if I want. I do, of course.
So once I've got some spare time at College, I'll probably get that.

Forgetting about the registry change I later shut my PC down, only to
find it not booting yesterday since it was looking for a non-existing
language pack. Whoops. I could've partially reset the registry to an
earlier state but I didn't like the possibility of unforeseen
consequences. Besides, I knew exactly what I needed to change. But the
regedit live CD I found online wouldn't start properly.

Oh well, my 40GB Windows partition was getting awfully full anyway.
Besides it's on the Samsung HDD and I already lost two of those, one of
them the exact same model (the current one being the replacement), so
I'd rather reinstall Windows on my 2TB Western Digital HDD.

But first I needed to make some space. Here, let's shrink this 500GB
partition by 110GB, of which we will use 25 for Ubuntu, 65 for Windows 7
and 20 for Windows XP in case I ever need to use that printer with no
recent drivers or replay Sam & Max Season 1 or 2 or anything else that
doesn't work on 7. And on the old ex-Windows partition I could install
this copy of Snow Leopard I've recently gotten from someone who got a
Mac and uses Windows on it. I hope I'll be able to get it to run, there
are some promising guides on
`hackintosh.com <http://www.hackintosh.com>`__.

For the partitioning I used a GParted Live CD, though I should've used
an Ubuntu Live CD which not only includes GParted, but also a browser
and some other stuff to pass time. Because resizing/moving partitions
takes forever. Well, not forever, but over 12 hours in my case and that
sure feels like forever. So I wasn't done with that until today.

The first thing I installed was Ubuntu. I still had an old 8.10 CD
from... probably 3 years ago, so I figured I could install that and use
automatic updates. Turns out automatic updates only bring you to the
next version, so I'd have to do six incremental upgrades. And 8.10 is no
longer supported, so getting updates is hard. In the end I just
downloaded 11.10 and did a fresh install.

For some reason I'm feeling a sudden urge to play Devil May Cry 4 right
now. Yes, that is totally unrelated and I'm pretty confused about where
it came from. I'm ignoring it.

Everything worked pretty much out of the box, except for sound on any
other than the left and right speaker. No showstopper. And the ATI
drivers wouldn't let me save changes, I had to recreate the X11
configuration file `as described
here <http://askubuntu.com/questions/70108/dual-view-monitors-for-one-desktop-on-ati>`__
to get my multi monitor setup to work.

I experienced the only other problems so far during writing this blog
entry - in the default settings, some accessibility features are
enabled, most annoyingly mouse keys (i.e. moving the mouse cursor using
the numpad, as opposed to writing numbers) and sticky keys. (Pressing
e.g. shift once keeps it active until after another key is pressed. The
only time I let go of shift before writing something is when I
reconsider and conclude I'd rather write in lowercase. Sticky keys make
me write in uppercase instead. Wonderful. No. Infuriating. Luckily
togglable.)

Later I told fellow Jedi Academy Coders on
irc://irc.arloria.net/#jacoders about my registry woes. They told me
about linux registry editing tools, `this
one <http://pogostick.net/~pnh/ntpasswd/>`__ in particular. I rejoiced
and fixed my registry. Windows is working again. I should still move it
to the 64GB partition and install XP some day, but for now, I have more
important things to do.

This programming assignment being the most important important thing at
the moment. I have until next monday to code a console Tetris in Pascal,
adhering to a couple of rules, otherwise I'll have to do the programming
assignments this semester, learning interesting things like if
conditions and loops. I'd rather not, especially since that's the only
subject I have on monday. So being relieved means free mondays. Yay!

So long,

Willi
