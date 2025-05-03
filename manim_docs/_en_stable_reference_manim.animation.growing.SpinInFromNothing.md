# Source: https://docs.manim.community/en/stable/reference/manim.animation.growing.SpinInFromNothing.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

SpinInFromNothing[¶](#spininfromnothing "Link to this heading")
===============================================================

Qualified name: `manim.animation.growing.SpinInFromNothing`

*class* SpinInFromNothing(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/growing.html#SpinInFromNothing)[¶](#manim.animation.growing.SpinInFromNothing "Link to this definition")
:   Bases: [`GrowFromCenter`](manim.animation.growing.GrowFromCenter.html#manim.animation.growing.GrowFromCenter "manim.animation.growing.GrowFromCenter")

    Introduce an [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") spinning and growing it from its center.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to be introduced.
        * **angle** (*float*) – The amount of spinning before mobject reaches its full size. E.g. 2\*PI means
          that the object will do one full spin before being fully introduced.
        * **point\_color** (*str*) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.

    Examples

    Example: SpinInFromNothingExample [¶](#spininfromnothingexample)

    [
    ](./SpinInFromNothingExample-1.mp4)

    ```
    from manim import *

    class SpinInFromNothingExample(Scene):
        def construct(self):
            squares = [Square() for _ in range(3)]
            VGroup(*squares).set_x(0).arrange(buff=2)
            self.play(SpinInFromNothing(squares[0]))
            self.play(SpinInFromNothing(squares[1], angle=2 * PI))
            self.play(SpinInFromNothing(squares[2], point_color=RED))

    ```

    ```

    class SpinInFromNothingExample(Scene):
        def construct(self):
            squares = [Square() for _ in range(3)]
            VGroup(*squares).set_x(0).arrange(buff=2)
            self.play(SpinInFromNothing(squares[0]))
            self.play(SpinInFromNothing(squares[1], angle=2 * PI))
            self.play(SpinInFromNothing(squares[2], point_color=RED))


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *angle=1.5707963267948966*, *point\_color=None*, *\*\*kwargs*)[¶](#manim.animation.growing.SpinInFromNothing._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **angle** (*float*)
            * **point\_color** (*str*)

        Return type:
        :   None