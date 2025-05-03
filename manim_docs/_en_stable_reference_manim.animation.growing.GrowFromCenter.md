# Source: https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromCenter.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

GrowFromCenter[¶](#growfromcenter "Link to this heading")
=========================================================

Qualified name: `manim.animation.growing.GrowFromCenter`

*class* GrowFromCenter(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/growing.html#GrowFromCenter)[¶](#manim.animation.growing.GrowFromCenter "Link to this definition")
:   Bases: [`GrowFromPoint`](manim.animation.growing.GrowFromPoint.html#manim.animation.growing.GrowFromPoint "manim.animation.growing.GrowFromPoint")

    Introduce an [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") by growing it from its center.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to be introduced.
        * **point\_color** (*str*) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.

    Examples

    Example: GrowFromCenterExample [¶](#growfromcenterexample)

    [
    ](./GrowFromCenterExample-1.mp4)

    ```
    from manim import *

    class GrowFromCenterExample(Scene):
        def construct(self):
            squares = [Square() for _ in range(2)]
            VGroup(*squares).set_x(0).arrange(buff=2)
            self.play(GrowFromCenter(squares[0]))
            self.play(GrowFromCenter(squares[1], point_color=RED))

    ```

    ```

    class GrowFromCenterExample(Scene):
        def construct(self):
            squares = [Square() for _ in range(2)]
            VGroup(*squares).set_x(0).arrange(buff=2)
            self.play(GrowFromCenter(squares[0]))
            self.play(GrowFromCenter(squares[1], point_color=RED))


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *point\_color=None*, *\*\*kwargs*)[¶](#manim.animation.growing.GrowFromCenter._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **point\_color** (*str*)

        Return type:
        :   None