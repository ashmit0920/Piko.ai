# Source: https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

scene\_file\_writer[¶](#module-manim.scene.scene_file_writer "Link to this heading")
====================================================================================

The interface between scenes and ffmpeg.

Classes

|  |  |
| --- | --- |
| [`SceneFileWriter`](manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter "manim.scene.scene_file_writer.SceneFileWriter") | SceneFileWriter is the object that actually writes the animations played, into video files, using FFMPEG. |

Functions

convert\_audio(*input\_path*, *output\_path*, *codec\_name*)[[source]](../_modules/manim/scene/scene_file_writer.html#convert_audio)[¶](#manim.scene.scene_file_writer.convert_audio "Link to this definition")
:   Parameters:
    :   * **input\_path** (*Path*)
        * **output\_path** (*Path*)
        * **codec\_name** (*str*)

to\_av\_frame\_rate(*fps*)[[source]](../_modules/manim/scene/scene_file_writer.html#to_av_frame_rate)[¶](#manim.scene.scene_file_writer.to_av_frame_rate "Link to this definition")