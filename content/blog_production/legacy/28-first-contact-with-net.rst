first contact with .NET
#######################
:date: 2011-08-27 10:23
:author: mrwonko
:category: Programming
:tags: Programming, Videogames, Razer Hydra, Gamescom
:type: blog
:slug: first-contact-with-net
:summary: The Razer Hydra is supposed to get DirectInput support. Some time this winter. I think I'm faster.

I've just been to the Gamescom. I don't have anything terribly
interesting to tell about that, besides that I lost my key, but that's
not really interesting either.

One of the things I did there was trying the Razer Hydra in the Portal 2
map we all know from the videos. I was able to get the hang of it pretty
quickly so my first impression was good. Maybe I should've done some
more extensive testing, but the more interesting part was a conversation
with someone from Sixense, the people behind the hardware.

I already knew they're working on DirectInput support, i.e. emulating an
ordinary gamepad, but now I got an estimate: This winter. So a couple of
days ago I thought to myself: Gee, I can do that faster, can't I?

Through some googling I found PPJoy, a virtual joystick emulator. After
trying to send data to one of its virtual joysticks without success for
some time I eventually found a working sample. Which means I'll be able
to get PPJoy up and running. That's one part out of three.

The second part is getting Input from the Hydra. Sixense has a free SDK,
available from Steam, which is pretty straight-forward. It doesn't
compile out of the box with MSVC 10 due to the lack of calling
convention definitions but that's easily fixed. The more serious problem
is that I in fact don't yet have a Hydra. I'm waiting for a version
without Portal 2, which is to be released "soon" for 100€. So I depend
on others to test my code. But so far everything seems to work, the SDK
works as expected (mostly). That's part two of three done.

The last part is creating an application that combines PPJoy and the
Sixense SDK and allows the user to configure it easily. Ordinary Windows
windows come to mind. So the time had come to make use of the "Visual"
part of Microsoft *Visual* Studio for the first time: Creating windows
with a visual editor using the .NET Framework.

It's surprisingly easy though I did have to learn about Microsoft's
superset of C++, which introduces garbage collection and new pointer
types for these reference counted objects. Still I'm making good
progress and most of the problems that pop up every now and then are
easily fixed. I might actually get this done this weekend.

`Link to my thread in the Sixense
forums <http://sixense.com/forum/vbulletin/showthread.php?3203-DirectInput-virtual-gamepad-%28version-0-4f%29>`__

So long,

Willi
