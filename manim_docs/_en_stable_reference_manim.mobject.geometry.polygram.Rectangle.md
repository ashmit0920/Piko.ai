# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Rectangle.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Rectangle[¶](#rectangle "Link to this heading")
===============================================

Qualified name: `manim.mobject.geometry.polygram.Rectangle`

*class* Rectangle(*color=ManimColor('#FFFFFF')*, *height=2.0*, *width=4.0*, *grid\_xstep=None*, *grid\_ystep=None*, *mark\_paths\_closed=True*, *close\_new\_points=True*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/polygram.html#Rectangle)[¶](#manim.mobject.geometry.polygram.Rectangle "Link to this definition")
:   Bases: [`Polygon`](manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon")

    A quadrilateral with two sets of parallel sides.

    Parameters:
    :   * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the rectangle.
        * **height** (*float*) – The vertical height of the rectangle.
        * **width** (*float*) – The horizontal width of the rectangle.
        * **grid\_xstep** (*float* *|* *None*) – Space between vertical grid lines.
        * **grid\_ystep** (*float* *|* *None*) – Space between horizontal grid lines.
        * **mark\_paths\_closed** (*bool*) – No purpose.
        * **close\_new\_points** (*bool*) – No purpose.
        * **kwargs** (*Any*) – Additional arguments to be passed to [`Polygon`](manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon")

    Examples

    Example: RectangleExample [¶](#rectangleexample)

    ![../_images/RectangleExample-1.png](../_images/RectangleExample-1.png)

    ```
    from manim import *

    class RectangleExample(Scene):
        def construct(self):
            rect1 = Rectangle(width=4.0, height=2.0, grid_xstep=1.0, grid_ystep=0.5)
            rect2 = Rectangle(width=1.0, height=4.0)
            rect3 = Rectangle(width=2.0, height=2.0, grid_xstep=1.0, grid_ystep=1.0)
            rect3.grid_lines.set_stroke(width=1)

            rects = Group(rect1, rect2, rect3).arrange(buff=1)
            self.add(rects)

    ```

    ```

    class RectangleExample(Scene):
        def construct(self):
            rect1 = Rectangle(width=4.0, height=2.0, grid_xstep=1.0, grid_ystep=0.5)
            rect2 = Rectangle(width=1.0, height=4.0)
            rect3 = Rectangle(width=2.0, height=2.0, grid_xstep=1.0, grid_ystep=1.0)
            rect3.grid_lines.set_stroke(width=1)

            rects = Group(rect1, rect2, rect3).arrange(buff=1)
            self.add(rects)


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

    \_original\_\_init\_\_(*color=ManimColor('#FFFFFF')*, *height=2.0*, *width=4.0*, *grid\_xstep=None*, *grid\_ystep=None*, *mark\_paths\_closed=True*, *close\_new\_points=True*, *\*\*kwargs*)[¶](#manim.mobject.geometry.polygram.Rectangle._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
            * **height** (*float*)
            * **width** (*float*)
            * **grid\_xstep** (*float* *|* *None*)
            * **grid\_ystep** (*float* *|* *None*)
            * **mark\_paths\_closed** (*bool*)
            * **close\_new\_points** (*bool*)
            * **kwargs** (*Any*)