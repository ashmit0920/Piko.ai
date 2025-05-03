# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RoundedRectangle.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

RoundedRectangle[¶](#roundedrectangle "Link to this heading")
=============================================================

Qualified name: `manim.mobject.geometry.polygram.RoundedRectangle`

*class* RoundedRectangle(*corner\_radius=0.5*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/polygram.html#RoundedRectangle)[¶](#manim.mobject.geometry.polygram.RoundedRectangle "Link to this definition")
:   Bases: [`Rectangle`](manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle")

    A rectangle with rounded corners.

    Parameters:
    :   * **corner\_radius** (*float* *|* *list**[**float**]*) – The curvature of the corners of the rectangle.
        * **kwargs** (*Any*) – Additional arguments to be passed to [`Rectangle`](manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle")

    Examples

    Example: RoundedRectangleExample [¶](#roundedrectangleexample)

    ![../_images/RoundedRectangleExample-1.png](../_images/RoundedRectangleExample-1.png)

    ```
    from manim import *

    class RoundedRectangleExample(Scene):
        def construct(self):
            rect_1 = RoundedRectangle(corner_radius=0.5)
            rect_2 = RoundedRectangle(corner_radius=1.5, height=4.0, width=4.0)

            rect_group = Group(rect_1, rect_2).arrange(buff=1)
            self.add(rect_group)

    ```

    ```

    class RoundedRectangleExample(Scene):
        def construct(self):
            rect_1 = RoundedRectangle(corner_radius=0.5)
            rect_2 = RoundedRectangle(corner_radius=1.5, height=4.0, width=4.0)

            rect_group = Group(rect_1, rect_2).arrange(buff=1)
            self.add(rect_group)


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

    \_original\_\_init\_\_(*corner\_radius=0.5*, *\*\*kwargs*)[¶](#manim.mobject.geometry.polygram.RoundedRectangle._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **corner\_radius** (*float* *|* *list**[**float**]*)
            * **kwargs** (*Any*)