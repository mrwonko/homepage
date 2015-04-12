title: How to build a rotating construction
type: tutorials
author: Joza
date: 2009-04-03
category: english - mapping

In this basic tutorial you'll learn how to make a brush/a construction of multiple brushes which rotates. 
It also works with multiple brushes, of course.

First of all, build the brush/es that will rotate. 

Then make another brush which is 2x2 units tall (grid 8) and apply the texture "system/origin".

![screenshot 1](http://joza.jo.funpic.de/images/rot_screen1.jpg)

Now select both your rotating brush/es AND the origin brush, press the right mouse button and select *func -> func_rotating*.

Press `N` to open the entity window and activate `start_on` if you want your brush to begin rotating as the map starts.

If `start_on` is not checked, the `func_rotating` must be triggered, e.g. by a `func_button` or a `trigger_multiple`.

By default, your brushes now rotate around the Z axis. To change this, either check `x_axis` or `y_axis` in the entity window. To find out which axis is the desired one, look at the information in the upper left corner of the 2d windows.

The `speed` and `dmg` (damage) keys are pretty self-explanatory.

![screenshot 2](http://joza.jo.funpic.de/images/rot_screen2.jpg)