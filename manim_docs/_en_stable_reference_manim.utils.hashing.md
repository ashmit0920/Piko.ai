# Source: https://docs.manim.community/en/stable/reference/manim.utils.hashing.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

hashing[¶](#module-manim.utils.hashing "Link to this heading")
==============================================================

Utilities for scene caching.

Functions

get\_hash\_from\_play\_call(*scene\_object*, *camera\_object*, *animations\_list*, *current\_mobjects\_list*)[[source]](../_modules/manim/utils/hashing.html#get_hash_from_play_call)[¶](#manim.utils.hashing.get_hash_from_play_call "Link to this definition")
:   Take the list of animations and a list of mobjects and output their hashes. This is meant to be used for scene.play function.

    Parameters:
    :   * **scene\_object** ([*Scene*](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene object.
        * **camera\_object** ([*Camera*](manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera") *|* *OpenGLCamera*) – The camera object used in the scene.
        * **animations\_list** (*Iterable**[*[*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")*]*) – The list of animations.
        * **current\_mobjects\_list** (*Iterable**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The list of mobjects.

    Returns:
    :   A string concatenation of the respective hashes of camera\_object, animations\_list and current\_mobjects\_list, separated by \_.

    Return type:
    :   `str`

get\_json(*obj*)[[source]](../_modules/manim/utils/hashing.html#get_json)[¶](#manim.utils.hashing.get_json "Link to this definition")
:   Recursively serialize object to JSON using the `CustomEncoder` class.

    Parameters:
    :   **obj** (*dict*) – The dict to flatten

    Returns:
    :   The flattened object

    Return type:
    :   `str`