title: func_breakables respawnen
date: 2008-11-04
type: tutorials/darth-arth
author: mrwonko
category: mapping
tags: Entities
modified: 2015-04-12
slug: entity-func_breakables-respawnen

Man kann zwar `func_breakable` nicht respawnen, wohl aber `func_usable`. Und zwar so:



1.  Zielscheibe zu `func_usable` machen

2.  in den Eigenschaften (<kbd>N</kbd>) einstellen:

    <pre>health     5
target     ziel_off
targetname ziel_on</pre>

3.  `target_delay` erstellen mit den Eigenschaften:

    <pre>targetname ziel_off
target     ziel on
wait       2</pre>

Dann wird bei Zerstörung (= null health) des `func_usable` der `target_delay` aktiviert, der nach 2 Sekunden die `func_usable` wieder einschaltet.
