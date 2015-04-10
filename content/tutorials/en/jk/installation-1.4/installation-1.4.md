title: Installation JK2 - GTK Radiant Map Editor
category: tutorial/tools
type: tutorial
date: 2009-08-06
authors: Darth Arth (Artur L.), Garen (Jan M.), mrwonko
summary: How to install GTK Radiant 1.4

# Abstract

This tutorial explains how to install the GTK Radiant 1.4 for usage with Jedi Knight II. Installation for Jedi Academy is similar.

You are strongly encouraged to use the GTK Radiant 1.6, whose installation differs.

# Requirements

* Jedi Knight II - Editing Tools
* Installation JK2 Editing Tools I (Tutorial)
* Jedi Knight II - Editing Tools II
* Installation JK2 Editing Tools II (Tutorial)
* GTK - Radiant setup file
* a game which is supported by GtkRadiant

# Tutorial

## 1. starting installation

Start the installation by double-clicking on the installation file.

![Welcome screen]({filename}../../../de/jk/installation-1.4/gtk_step1.jpg)

A dialog should appear. Click "Next" to continue.

## 2. license agreement

![License]({filename}../../../de/jk/installation-1.4/gtk_step2.jpg)

To install GtkRadiant you have to accept the license agreement. You should read the agreement carefully (I don't think anyone does this). If you agree, click "Yes".

Otherwise click "No". In that case the installation will end and you can stop this tutorial.

## 3. program information

![Info]({filename}../../../de/jk/installation-1.4/gtk_step3.jpg)

Now you can see information about the version which you are installing.

Read it and/or click on "Next".

## 4. the program installation path

![Destination]({filename}../../../de/jk/installation-1.4/gtk_step4.jpg)

Choose the path where you want to install the editor and its files. This path doesn't matter as long as it's NOT the folder "GameData", "GameData/base" or "GameData/Tools" of your game.

After choosing the program installation path click "Next" to continue.

## 5. game installation path

Now the programme asks you where games are located. You do _not_ need to choose every path. It **is** important to choose the path of your game. 

So click "Next" until your game appears (for example Jedi Knight II: Jedi Outcast). 

![Game selection]({filename}../../../de/jk/installation-1.4/gtk_step7.jpg)

Click on "Browse" ...

![Choosing GameData]({filename}../../../de/jk/installation-1.4/gtk_step8.jpg)

... and select the "GameData" folder of your game.

Important!

GtkRadiant only works properly if Editing-Tools I and II are already installed and you have chosen the "GameData" folder!

![Result]({filename}../../../de/jk/installation-1.4/gtk_step9.jpg)

After choosing your game's path correctly click on "Next".

## 6. GtkRadiant game relevant files

![Radiant Data Subfolder]({filename}../../../de/jk/installation-1.4/gtk_step10.jpg)

Here you can choose the name of the folder which will be installed in your game folder. As this isn't necessary to change you can go on ("Next").

## 7. installation extent

![Setup Type]({filename}../../../de/jk/installation-1.4/gtk_step11.jpg)

After choosing your game's path (and ignoring other game's paths) you are now given the choice between a custom and a full install. Darth-Arth recommends you to select "Full Install".

If you don't want to install the plugins for the other games you can choose "Custom". The setup will ask you what to install (default is everything, see "Full Install"). Uncheck only games you don't have. You should install program files, your game's plugin and documents (documents aren't necessary).

After selecting click "Next".

## 8. program group

![Start Menu Entry]({filename}../../../de/jk/installation-1.4/gtk_step12.jpg)

Here you can label the start menu's folder for GtkRadiant.

## 9. checking installation settings

![Summary]({filename}../../../de/jk/installation-1.4/gtk_step13.jpg)

The setup lists the settings you have chosen before. Check and change (click "Back") them if necessary. If the settings are ok click "Next" to install GtkRadiant.

Dart-Arth recommends to check the game's path again to make sure it's correct. If the path is wrong you will have to reinstall the program. And you're lazy, you don't want to repeat the installation, do you?




## 10. end of installation

![Setup Done]({filename}../../../de/jk/installation-1.4/gtk_step14.jpg)

If the setup succeeds click "Finish". 

## 11. first start

Start the GtkRadiant. A dialog will appear:

![Game Choice]({filename}../../../de/jk/installation-1.4/gtk_step15.jpg)

Choose your game and - if you want - check the auto load (the GtkRadiant won't ask you again. If you checked auto load and want to change game you can change it later. See below).

![Warning]({filename}../../../de/jk/installation-1.4/gtk_step17.jpg)

If you also check logging a warning will appear. It tells you that logging can slow down the programme. Choose whether you still want to log.

## 12. checking configurations

Okay, now you will see whether you did everything right. 

![GTK Radiant in Action]({filename}../../../de/jk/installation-1.4/gtk_step18.jpg)

Click on "Textures" and choose "cairn". If there is no cairn or any other option (below "shaderlist.txt only") the setup failed. If there are only tiny "shader image missing" images instead of textures the setup failed. You will have to check the installation path of your game again and reinstall the programme.



# Credits

original tutorial by: Darth Arth (Artur L.)

translated by: Garen (Jan M.)

typos fixed and his name added: mrwonko (Willi S.)