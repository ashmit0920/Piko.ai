# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeToColor.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

FadeToColor[¶](#fadetocolor "Link to this heading")
===================================================

Qualified name: `manim.animation.transform.FadeToColor`

*class* FadeToColor(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform.html#FadeToColor)[¶](#manim.animation.transform.FadeToColor "Link to this definition")
:   Bases: [`ApplyMethod`](manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

    Animation that changes color of a mobject.

    Examples

    Example: FadeToColorExample [¶](#fadetocolorexample)

    [
    ](./FadeToColorExample-1.mp4)

    ```
    from manim import *

    class FadeToColorExample(Scene):
        def construct(self):
            self.play(FadeToColor(Text("Hello World!"), color=RED))

    ```

    ```

    class FadeToColorExample(Scene):
        def construct(self):
            self.play(FadeToColor(Text("Hello World!"), color=RED))


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
        * **color** (*str*)

    \_original\_\_init\_\_(*mobject*, *color*, *\*\*kwargs*)[¶](#manim.animation.transform.FadeToColor._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **color** (*str*)

        Return type:
        :   None