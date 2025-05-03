# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform.ShrinkToCenter.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ShrinkToCenter[¶](#shrinktocenter "Link to this heading")
=========================================================

Qualified name: `manim.animation.transform.ShrinkToCenter`

*class* ShrinkToCenter(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform.html#ShrinkToCenter)[¶](#manim.animation.transform.ShrinkToCenter "Link to this definition")
:   Bases: [`ScaleInPlace`](manim.animation.transform.ScaleInPlace.html#manim.animation.transform.ScaleInPlace "manim.animation.transform.ScaleInPlace")

    Animation that makes a mobject shrink to center.

    Examples

    Example: ShrinkToCenterExample [¶](#shrinktocenterexample)

    [
    ](./ShrinkToCenterExample-1.mp4)

    ```
    from manim import *

    class ShrinkToCenterExample(Scene):
        def construct(self):
            self.play(ShrinkToCenter(Text("Hello World!")))

    ```

    ```

    class ShrinkToCenterExample(Scene):
        def construct(self):
            self.play(ShrinkToCenter(Text("Hello World!")))


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    Parameters:
    :   **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

    \_original\_\_init\_\_(*mobject*, *\*\*kwargs*)[¶](#manim.animation.transform.ShrinkToCenter._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

        Return type:
        :   None