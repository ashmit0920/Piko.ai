# Source: https://docs.manim.community/en/stable/reference/manim.scene.scene.RerunSceneHandler.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

RerunSceneHandler[¶](#rerunscenehandler "Link to this heading")
===============================================================

Qualified name: `manim.scene.scene.RerunSceneHandler`

*class* RerunSceneHandler(*queue*)[[source]](../_modules/manim/scene/scene.html#RerunSceneHandler)[¶](#manim.scene.scene.RerunSceneHandler "Link to this definition")
:   Bases: `FileSystemEventHandler`

    A class to handle rerunning a Scene after the input file is modified.

    Methods

    |  |  |
    | --- | --- |
    | [`on_modified`](#manim.scene.scene.RerunSceneHandler.on_modified "manim.scene.scene.RerunSceneHandler.on_modified") | Called when a file or directory is modified. |

    on\_modified(*event*)[[source]](../_modules/manim/scene/scene.html#RerunSceneHandler.on_modified)[¶](#manim.scene.scene.RerunSceneHandler.on_modified "Link to this definition")
    :   Called when a file or directory is modified.

        Parameters:
        :   **event** (`DirModifiedEvent` or `FileModifiedEvent`) – Event representing file/directory modification.