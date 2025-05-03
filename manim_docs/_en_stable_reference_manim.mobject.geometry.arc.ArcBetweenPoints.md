# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcBetweenPoints.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ArcBetweenPoints[¶](#arcbetweenpoints "Link to this heading")
=============================================================

Qualified name: `manim.mobject.geometry.arc.ArcBetweenPoints`

*class* ArcBetweenPoints(*start*, *end*, *angle=1.5707963267948966*, *radius=None*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/arc.html#ArcBetweenPoints)[¶](#manim.mobject.geometry.arc.ArcBetweenPoints "Link to this definition")
:   Bases: [`Arc`](manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc")

    Inherits from Arc and additionally takes 2 points between which the arc is spanned.

    Example

    Example: ArcBetweenPointsExample [¶](#arcbetweenpointsexample)

    [
    ](./ArcBetweenPointsExample-1.mp4)

    ```
    from manim import *

    class ArcBetweenPointsExample(Scene):
        def construct(self):
            circle = Circle(radius=2, stroke_color=GREY)
            dot_1 = Dot(color=GREEN).move_to([2, 0, 0]).scale(0.5)
            dot_1_text = Tex("(2,0)").scale(0.5).next_to(dot_1, RIGHT).set_color(BLUE)
            dot_2 = Dot(color=GREEN).move_to([0, 2, 0]).scale(0.5)
            dot_2_text = Tex("(0,2)").scale(0.5).next_to(dot_2, UP).set_color(BLUE)
            arc= ArcBetweenPoints(start=2 * RIGHT, end=2 * UP, stroke_color=YELLOW)
            self.add(circle, dot_1, dot_2, dot_1_text, dot_2_text)
            self.play(Create(arc))

    ```

    ```

    class ArcBetweenPointsExample(Scene):
        def construct(self):
            circle = Circle(radius=2, stroke_color=GREY)
            dot_1 = Dot(color=GREEN).move_to([2, 0, 0]).scale(0.5)
            dot_1_text = Tex("(2,0)").scale(0.5).next_to(dot_1, RIGHT).set_color(BLUE)
            dot_2 = Dot(color=GREEN).move_to([0, 2, 0]).scale(0.5)
            dot_2_text = Tex("(0,2)").scale(0.5).next_to(dot_2, UP).set_color(BLUE)
            arc= ArcBetweenPoints(start=2 * RIGHT, end=2 * UP, stroke_color=YELLOW)
            self.add(circle, dot_1, dot_2, dot_1_text, dot_2_text)
            self.play(Create(arc))


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    Parameters:
    :   * **start** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
        * **end** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
        * **angle** (*float*)
        * **radius** (*float* *|* *None*)
        * **kwargs** (*Any*)

    \_original\_\_init\_\_(*start*, *end*, *angle=1.5707963267948966*, *radius=None*, *\*\*kwargs*)[¶](#manim.mobject.geometry.arc.ArcBetweenPoints._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **start** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
            * **end** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
            * **angle** (*float*)
            * **radius** (*float* *|* *None*)
            * **kwargs** (*Any*)

        Return type:
        :   None