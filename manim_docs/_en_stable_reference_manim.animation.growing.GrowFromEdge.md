# Source: https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromEdge.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

GrowFromEdge[¶](#growfromedge "Link to this heading")
=====================================================

Qualified name: `manim.animation.growing.GrowFromEdge`

*class* GrowFromEdge(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/growing.html#GrowFromEdge)[¶](#manim.animation.growing.GrowFromEdge "Link to this definition")
:   Bases: [`GrowFromPoint`](manim.animation.growing.GrowFromPoint.html#manim.animation.growing.GrowFromPoint "manim.animation.growing.GrowFromPoint")

    Introduce an [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") by growing it from one of its bounding box edges.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to be introduced.
        * **edge** (*np.ndarray*) – The direction to seek bounding box edge of mobject.
        * **point\_color** (*str*) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.

    Examples

    Example: GrowFromEdgeExample [¶](#growfromedgeexample)

    [
    ](./GrowFromEdgeExample-1.mp4)

    ```
    from manim import *

    class GrowFromEdgeExample(Scene):
        def construct(self):
            squares = [Square() for _ in range(4)]
            VGroup(*squares).set_x(0).arrange(buff=1)
            self.play(GrowFromEdge(squares[0], DOWN))
            self.play(GrowFromEdge(squares[1], RIGHT))
            self.play(GrowFromEdge(squares[2], UR))
            self.play(GrowFromEdge(squares[3], UP, point_color=RED))

    ```

    ```

    class GrowFromEdgeExample(Scene):
        def construct(self):
            squares = [Square() for _ in range(4)]
            VGroup(*squares).set_x(0).arrange(buff=1)
            self.play(GrowFromEdge(squares[0], DOWN))
            self.play(GrowFromEdge(squares[1], RIGHT))
            self.play(GrowFromEdge(squares[2], UR))
            self.play(GrowFromEdge(squares[3], UP, point_color=RED))


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *edge*, *point\_color=None*, *\*\*kwargs*)[¶](#manim.animation.growing.GrowFromEdge._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **edge** (*np.ndarray*)
            * **point\_color** (*str*)

        Return type:
        :   None