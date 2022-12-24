Title: Projects plans
author: mrwonko
date: 2015-05-15
tags: Modding, Programming, Spirits of the Sith, 3D-GET, Blender, 7DFPS, Computer Graphics, Jedi Academy: Renaissance, Perseus, Razer Hydra, Stille Tänzer, projects, FlatOut 2
category: Programming
type: blog
summary: I have a lot of projects I'd like to work on, but I can only work on so many at any time. But here's a list of all of them! 

I'm currently fairly busy with my Bachelor Thesis, writing the core of my programming language [Perseus](https://github.com/mrwonko/perseus). Besides that I also still have to support my legacy projects, in particular I need to update my [Python binding of the Razer Hydra library](https://github.com/mrwonko/PySixense) whenever a new Python version is released.

But that doesn't mean I have no other plans. In fact there are a lot of projects I have started or want to start eventually, and I thought I'd just list them here.

Let's start with the other projects I've already started with:

###	Spirits of the Sith

A new singleplayer campaign for Jedi Knight: Jedi Academy that the modding team 3D-GET worked on roughly from 2002 to 2008. I joined when it was already mostly dead, but it would be a massive shame if the 80% or so that are already done were to go to waste. Most of the remaining work is technical stuff, so right up my alley.

### Blender GLM Exporter

Part of my Jedi Academy Plugin Suite, the exporter could do with some improvements. People regularly struggle to get their models to export because the exporter requires the user to do some preparation that should just be automated.

### Videotutorial on Jedi Academy Player Modelling in Blender

Related to the above, I've previously started recording a video tutorial on playermodel creation from scratch but never even finished modelling - hands are hard. It would be useful to finish those videos before there are no modders left to benefit from them.

### FlatOut 2 Modding

I started [reverse engineering FlatOut 2](https://github.com/mrwonko/fo2re) to [enable more modding](https://github.com/mrwonko/fo2unleashed/); in particular I want to be able to create completely new levels and enable multiple mods to be active simultaneously without interfering with each other.

### Homepage

I have a couple of additional features for this website in mind; besides Metadata for Twitter, Facebook and Google I mainly need proper filtering/searching for downloads, a better way to access old blog posts than pagination and I still need to port the remaining Darth-Arth tutorials.

### Jedi Academy: Renaissance

While I'm a big fan of open source, I don't like copyleft (and the GPL in particular) very much. At least when it prevents me from using e.g. closed source libraries in those projects. So while I'd love to code lots of cool stuff for Jedi Academy, I won't modify its source. Instead I'm recoding it from scratch. Yes, that's crazy. It gets even crazier: It will mostly be written in my own aforementioned programming language Perseus. Which I first have to write.

The reason I'm using my own language is that I want a scripting language (to enable mods), but the existing languages don't satisfy my requirements. Besides, designing a programming language is fun.

---

And then there are a whole lot of planned projects:

### The GhoulKit

I'm not really all that happy with the my Jedi Academy tools for Blender. Or maybe I should say I'm not really all that happy with Blender. At least for creating Jedi Academy models. Blender can do a lot, but that makes it complicated.

I basically feel that a dedicated tool could be much simpler. The GhoulKit would be this tool. Its purpose is creating Jedi Academy armatures, rigging, preparing models for dismemberment, creating the proper hierarchy, handling LODs and previewing the model as it will look in the game.

### Pen & Paper App (working title)

I like playing Pen & Paper RPGs, but looking up rules all the time and erasing & changing your values is somewhat tedious. This could be simplified by doing it digitally, which could also help with visualization and limiting information, as well as letting the DM discreetly check player stats, making hidden rolls etc.

However, I don't want a web app since I may not have internet access; I want a cross-platform native app with networking. So it would probably be made using Qt. An almost automatic side effect of the networking would be the possibility of playing together remotely.

I suppose [CastAR](http://castar.com/) support would make this even cooler. Not that I've ordered one, but I could totally see that happen. Well, I'm really just dreaming at this point, but nothing wrong with thinking big... This is just a list of interesting possible projects, after all, not a concrete plan.

### Map Forge

The [GTK Radiant](http://icculus.org/gtkradiant/) isn't all that modern or simple an editor, I have a couple of ideas for a better Jedi Academy level editor. (Yes, I'm still very much focussed on Jedi Academy, despite hardly having played or modded it for multiple years at this point. Call it nostalgia or affection or something.)

I could just contribute to the GTK Radiant, but why not create my own editor instead? I could use Qt instead of GTK, which I prefer for no apparent reason (despite hardly having used either), use a different license and do things however I want.

I may be experiencing a severe case of [Not Invented Here](http://en.wikipedia.org/wiki/Not_invented_here).

### Browser (working title)

I like the tab groups that Firefox offers and how loads tabs lazily, allowing me to have hundreds of tabs open and still be somewhat organized.

I don't like how it gets super slow when I have hundreds of tabs open, and really I want to have ALL THE TABS and nest them even deeper; why have favorites when you can just unload a tab and keep it open in a different folder?

Chrome seems a lot faster, though I've never had quite as many tabs open in it because it neither supports lazy loading nor does it have tab groups.

I should probably just write the perfect browser for me. With Qt WebEngine it might even be fairly simple while matching Chrome's performance.

### First Person Synapse (working title)

Like Frozen Synapse, except an Ego Shooter.

### Invisibility

A 2D top down multiplayer shooter where everybody is usually invisible.

### Stille Tänzer

[I've written about this before]({filename}../legacy/49-a-mazeing.rst). Multiplayer dancing.

### Rollercoast Tycoon 1/2 clone (working title)

What it says in the title. In 3D, but using the original palette with an isometric view that looks as close to the original as possible. But park exploration and riding rollercoasters in first person are also possible.

Looks like I may not need to write this, I recently found out about [OpenRCT2](https://github.com/IntelOrca/OpenRCT2). It's legally questionable since it doesn't use a [clean room approach](http://en.wikipedia.org/wiki/Clean_room_design) but it's unlikely to get in trouble. I could probably "just" add 3D rendering to that and be happy ever after.

Or just play [Parkitect](http://www.themeparkitect.com/). It may be made in Unity, but my irrational dislike for that has already started to waver thanks to Sir, You Are Being Hunted and Cities: Skylines.

### Graphics Programming

I have a bunch of computer graphics effects I'd love to implement at some point, including: God Rays, Dynamic Lighting (in various flavors of deferred and forward), fog, particles, a material system (in particular a fast version of Jedi Academy's shaders), tesselation, curves using geometry shaders, skinning/skeletal animations, inverse kinematics, VR.

I'll be able to scratch this itch with Jedi Academy: Renaissance, if I ever get anywhere with that.

### Custom Mouse

I may not need to create my dream keyboard/gamepad hybrid since that's probably basically the Logitech G13 (I would possibly have included an analog trigger though), but I'd still like to create my own mouse/gamepad hybrid with lots of buttons, a mouse wheel, an analog stick and an analog trigger.

Should be quite possible by gutting a gamepad, a mouse and a USB hub and creating a fibreglass shell. Or I could go all out with a microprocessor running custom firmware, but I'm not sure writing the firmware and drivers is much fun.

---

So those are the projects I haven't cancelled yet. Let's see which of them come to pass. I hope at least the Browser will, since I'd quite like to use that, and the Pen & Paper App would be nice as well. And Spirits of the Sith has come way to far to be abandoned forever.
