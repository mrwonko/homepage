title: Menu Coding - Einbinden und Erklärung von Strings
date: 2008-01-14
type: tutorials
author: opiwahn
category: scripts
tags: Menu
modified: 2015-04-12
slug: menu-strings

# Voraussetzungen

Wenn man Menus wirklich lernen möchte, sollte man sich die Tutorials von Biki anschauen.

Ich werde die Befehle, die in Bikis Tutorials schon erklärt werden, hier auf jeden Fall nicht noch einmal erklären ;)! Also schauts euch an:

*   [BiKis erstes Tut]({filename}menu-basics.md)
*   [Und BiKis zweites Tut]({filename}menu-advanced.md)



# Tutorial

In diesem Tutorial lernen wir das einbinden von Strings.

Die Syntax in der .menu Datei lautet: 

<pre>text     @[String-Datei]_[link in dieser String-Datei]</pre>

Ein Beispiel: `@beispielstring_beispieltext` oder auch: `@meinemod_meintext`

Diese Datei muss in dem Ordner `strings/[sprache]` liegen.

Also zum Beispiel: `strings/english`

Die Datei hat die Dateiendung `.str` und der Inhalt sieht folgendermaßen aus: (Beispiel)

<pre>//BSP.str
//
VERSION             "1"
CONFIG              "W:\bin\stringed.cfg"
FILENOTES           "Text printed at console"

REFERENCE		MEINLINK
LANG_ENGLISH		"Meintext ist voll\n cool!"
ENDMARKER</pre>

Am Anfang muss immer das Ganze mit `VERSION`, `CONFIG` und `FILENOTES` kommen. Und ganz am Ende der Datei der Befehl: `ENDMARKER`

Reference ist sozusagen der Link zum Text. Der Text selber steht in der Zeile mit `LANG_ENGLISH`.

Zeilenumbrüche können mit dem Befehl `\n` erzeugt werden.

Dieses Beispiel zeigt euch, wie so ein Text im Menü aussehen kann:

<pre>itemDef 
{
    name				credits //name des items
    text				@BSP_MEINLINK  //der string "link"
    style				WINDOW_STYLE_EMPTY
    rect				100 200 130 24 
    font				4 
    textscale			1.1
    textalign			ITEM_ALIGN_CENTER
    textstyle			3
    textalignx			65
    textaligny			-1
    forecolor			1 1 1 1
    visible				1
    decoration
}</pre>

Dieser itemDef würde bewirken, dass im fertigen Menü folgendes stehen würde:

<pre>Meintext ist voll
cool!</pre>


Ich hoffe, ich konnte euch helfen ^^

Bei weiteren Fragen oder Anmerkungen, kontaktiert mich bitte einfach ;)

* icq: 332-232-603
* email: opiwahn [at] web . de
