# Source: https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromPoint.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

GrowFromPoint[¶](#growfrompoint "Link to this heading")
=======================================================

Qualified name: `manim.animation.growing.GrowFromPoint`

*class* GrowFromPoint(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/growing.html#GrowFromPoint)[¶](#manim.animation.growing.GrowFromPoint "Link to this definition")
:   Bases: [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

    Introduce an [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") by growing it from a point.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to be introduced.
        * **point** (*np.ndarray*) – The point from which the mobject grows.
        * **point\_color** (*str*) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.

    Examples

    Example: GrowFromPointExample [¶](#growfrompointexample)

    [
    ](./GrowFromPointExample-1.mp4)

    ```
    from manim import *

    class GrowFromPointExample(Scene):
        def construct(self):
            dot = Dot(3 * UR, color=GREEN)
            squares = [Square() for _ in range(4)]
            VGroup(*squares).set_x(0).arrange(buff=1)
            self.add(dot)
            self.play(GrowFromPoint(squares[0], ORIGIN))
            self.play(GrowFromPoint(squares[1], [-2, 2, 0]))
            self.play(GrowFromPoint(squares[2], [3, -2, 0], RED))
            self.play(GrowFromPoint(squares[3], dot, dot.get_color()))

    ```

    ```

    class GrowFromPointExample(Scene):
        def construct(self):
            dot = Dot(3 * UR, color=GREEN)
            squares = [Square() for _ in range(4)]
            VGroup(*squares).set_x(0).arrange(buff=1)
            self.add(dot)
            self.play(GrowFromPoint(squares[0], ORIGIN))
            self.play(GrowFromPoint(squares[1], [-2, 2, 0]))
            self.play(GrowFromPoint(squares[2], [3, -2, 0], RED))
            self.play(GrowFromPoint(squares[3], dot, dot.get_color()))


    ```

    Methods

    |  |  |
    | --- | --- |
    | `create_starting_mobject` |  |
    | `create_target` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *point*, *point\_color=None*, *\*\*kwargs*)[¶](#manim.animation.growing.GrowFromPoint._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **point** (*np.ndarray*)
            * **point\_color** (*str*)

        Return type:
        :   None