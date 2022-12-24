Title: Return to FlatOut 2 modding
author: mrwonko
date: 2022-12-24 10:46
tags: Modding, Programming, Blender, projects, FlatOut 2
category: 
type: blog
summary: After a years long interlude, I've returned to reverse engineering the FlatOut 2 track format.

It turns out that when you spend 40 hours a week building software for a living, you don't have much energy left to do more of it in your spare time. Figures...

And how have I been spending what little precious energy is left? I had the silly idea of building my own Raspberry Pi-based smart lights. As usual, it ended up being more work than anticipated, and isn't much more than an MVP at the moment. Some wheels don't need to be reinvented... I spent a lot of time saving a little money, when I should be doing the opposite. But dipping my toes into PCB design was fun.

Anyway, the lights work well enough for now, and I'm finally returning to projects that benefit people beyond me. Namely, I've returned to a project from my university days: custom FlatOut 2 race tracks.

FlatOut 2 was a mainstay at our private lan-parties when I was a kid, and in my opinion still holds up. But custom tracks have always been elusive, thanks to an elusive proprietary collision data file format. Which I have now returned to trying to reverse engineer, [after 7 years]({filename}../2015/05-15-project-plans.md).

So these last days I've been knee-deep in disassembled machine code, stepping through instruction by instruction using a debugger, slowly understanding the file format and building [a Blender plugin for it](https://github.com/mrwonko/flatout-open-level-editor). If things go well, I'll be done before the year is over.

After that, I could spend more time building a fully fledged user friendly track editor, but my heart wants to return to Jedi Academy. I love the game and its modding community, and I miss writing C++. I want to see what kind of code I can write free of deadlines and commercial interests, unleashing my perfectionism. I don't want my best work to be proprietary.
