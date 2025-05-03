# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform.ScaleInPlace.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ScaleInPlace[¶](#scaleinplace "Link to this heading")
=====================================================

Qualified name: `manim.animation.transform.ScaleInPlace`

*class* ScaleInPlace(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform.html#ScaleInPlace)[¶](#manim.animation.transform.ScaleInPlace "Link to this definition")
:   Bases: [`ApplyMethod`](manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

    Animation that scales a mobject by a certain factor.

    Examples

    Example: ScaleInPlaceExample [¶](#scaleinplaceexample)

    [
    ](./ScaleInPlaceExample-1.mp4)

    ```
    from manim import *

    class ScaleInPlaceExample(Scene):
        def construct(self):
            self.play(ScaleInPlace(Text("Hello World!"), 2))

    ```

    ```

    class ScaleInPlaceExample(Scene):
        def construct(self):
            self.play(ScaleInPlace(Text("Hello World!"), 2))


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **scale\_factor** (*float*)

    \_original\_\_init\_\_(*mobject*, *scale\_factor*, *\*\*kwargs*)[¶](#manim.animation.transform.ScaleInPlace._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **scale\_factor** (*float*)

        Return type:
        :   None