title: Leitern - mal anders
date: 2008-04-06
type: tutorials
author: mrwonko
category: mapping
tags: Leiter, FIXME
modified: 2015-04-12

Das Problem an [der anderen Leiter]({filename}leitern.md) ist ja, dass man verdammt schnell rauf läuft, da Jedi Knight zur Geschwindigkeitskalkulation lediglich die horizontal, nicht jedoch die vertikal zurückgelegte Strecke nutzt, und man läuft ja sehr wenig vorwärts.

Bei meiner Leiter klettert man nach oben, wenn man hoch guckt, und runter, wenn man runter guckt.

Bei einem Trigger_multiple kann man einstellen, dass er nur anspringt, wenn man in eine bestimmte Richtung guckt, indem man ein Häkchen bei Facing macht.

Wir bauen also 2 `trigger_multiple`, einen für hoch und einen für runter. Wir drücken jeweils <kbd>N</kbd>, um in die Eigenschaften zu kommen. Beide kriegen ein Häkchen bei facing und eines bei Multiple, damit mehrere gleichzeitig auf der Leiter sein können. Beim einen klicken wir auf den `DN` Knopf, das steht für "Down", also "runter". Der andere kriegt `UP`, also rauf.

Jetzt bauen wir 2 `target_push`. Die geben ihrem Benutzer einen Schupps in Richtung ihres targets bzw. ihrer angle. Beide kriegen ein `constant`-Häkchen, weil wir mit konstanter Geschwindigkeit die Leiter klettern wollen. Der eine bekommt wieder `DN`, der andere entweder `UP`, oder man nimmt einen target_position als target, der Hoch und ein wenig richtung Leiter zeigt, sodass man beim hochklettern noch ein wenig gegen die Leiter gedrückt wird, damit man am Ende die Leiter automatisch verlässt und nicht doof in der Luft hochhüpft.

Man muss noch den speed anpassen, ich fand 50 für runter und 70 für hoch ganz in Ordnung, aber wenn euch das zu langsam/schnell ist, könnt ihr ja ein wenig rumprobieren.

Dann werden die Trigger via <kbd>strg + k</kbd> (siehe z.B. Lift m. Button Tutorial FIXME) mit den entsprechenden `target_push`s verbunden. Den Runter-Trigger kann man ein wenig kleiner machen, sodass er weiter über dem Boden beginnt, damit man am Ende nicht in den Boden gedrückt wird sondern unbeeinflusst steht.

![image]({filename}leitern-mal-anders-1.jpg)

Dann werden die beiden `trigger_multiple` vor die Leiter geschoben und fertig.

![image]({filename}leitern-mal-anders-2.jpg)

[Download der Beispiel Map]({filename}examples/mrw_ladder.zip)

_Anmerkung_: Die BSP Datei sowie verwendete Texturen in der Beispielmap stammen aus Jedi Academy. Ich weiß nicht, ob dieses Tutorial auf JK2 anwendbar ist, möglicherweise gibt es keinen `target_push`. Im Singleplayer muss man außerdem zuerst hüpfen, damit es aufwärts geht.

_Anregung_: Der Leiter noch einen Klettersound (`target_speaker`) verpassen, der ebenso wie der `target_push` mit den Trigger verbunden wird.
