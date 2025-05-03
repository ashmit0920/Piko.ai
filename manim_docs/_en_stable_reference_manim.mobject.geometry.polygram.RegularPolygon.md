# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygon.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

RegularPolygon[¶](#regularpolygon "Link to this heading")
=========================================================

Qualified name: `manim.mobject.geometry.polygram.RegularPolygon`

*class* RegularPolygon(*n=6*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/polygram.html#RegularPolygon)[¶](#manim.mobject.geometry.polygram.RegularPolygon "Link to this definition")
:   Bases: [`RegularPolygram`](manim.mobject.geometry.polygram.RegularPolygram.html#manim.mobject.geometry.polygram.RegularPolygram "manim.mobject.geometry.polygram.RegularPolygram")

    An n-sided regular [`Polygon`](manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon").

    Parameters:
    :   * **n** (*int*) – The number of sides of the [`RegularPolygon`](#manim.mobject.geometry.polygram.RegularPolygon "manim.mobject.geometry.polygram.RegularPolygon").
        * **kwargs** (*Any*) – Forwarded to the parent constructor.

    Examples

    Example: RegularPolygonExample [¶](#regularpolygonexample)

    ![../_images/RegularPolygonExample-1.png](../_images/RegularPolygonExample-1.png)

    ```
    from manim import *

    class RegularPolygonExample(Scene):
        def construct(self):
            poly_1 = RegularPolygon(n=6)
            poly_2 = RegularPolygon(n=6, start_angle=30*DEGREES, color=GREEN)
            poly_3 = RegularPolygon(n=10, color=RED)

            poly_group = Group(poly_1, poly_2, poly_3).scale(1.5).arrange(buff=1)
            self.add(poly_group)

    ```

    ```

    class RegularPolygonExample(Scene):
        def construct(self):
            poly_1 = RegularPolygon(n=6)
            poly_2 = RegularPolygon(n=6, start_angle=30*DEGREES, color=GREEN)
            poly_3 = RegularPolygon(n=10, color=RED)

            poly_group = Group(poly_1, poly_2, poly_3).scale(1.5).arrange(buff=1)
            self.add(poly_group)


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

    \_original\_\_init\_\_(*n=6*, *\*\*kwargs*)[¶](#manim.mobject.geometry.polygram.RegularPolygon._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **n** (*int*)
            * **kwargs** (*Any*)

        Return type:
        :   None