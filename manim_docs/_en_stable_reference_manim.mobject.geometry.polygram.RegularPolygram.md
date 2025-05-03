# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygram.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

RegularPolygram[¶](#regularpolygram "Link to this heading")
===========================================================

Qualified name: `manim.mobject.geometry.polygram.RegularPolygram`

*class* RegularPolygram(*num\_vertices*, *\**, *density=2*, *radius=1*, *start\_angle=None*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/polygram.html#RegularPolygram)[¶](#manim.mobject.geometry.polygram.RegularPolygram "Link to this definition")
:   Bases: [`Polygram`](manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram")

    A [`Polygram`](manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram") with regularly spaced vertices.

    Parameters:
    :   * **num\_vertices** (*int*) – The number of vertices.
        * **density** (*int*) –

          The density of the [`RegularPolygram`](#manim.mobject.geometry.polygram.RegularPolygram "manim.mobject.geometry.polygram.RegularPolygram").

          Can be thought of as how many vertices to hop
          to draw a line between them. Every `density`-th
          vertex is connected.
        * **radius** (*float*) – The radius of the circle that the vertices are placed on.
        * **start\_angle** (*float* *|* *None*) – The angle the vertices start at; the rotation of
          the [`RegularPolygram`](#manim.mobject.geometry.polygram.RegularPolygram "manim.mobject.geometry.polygram.RegularPolygram").
        * **kwargs** (*Any*) – Forwarded to the parent constructor.

    Examples

    Example: RegularPolygramExample [¶](#regularpolygramexample)

    ![../_images/RegularPolygramExample-1.png](../_images/RegularPolygramExample-1.png)

    ```
    from manim import *

    class RegularPolygramExample(Scene):
        def construct(self):
            pentagram = RegularPolygram(5, radius=2)
            self.add(pentagram)

    ```

    ```

    class RegularPolygramExample(Scene):
        def construct(self):
            pentagram = RegularPolygram(5, radius=2)
            self.add(pentagram)


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

    \_original\_\_init\_\_(*num\_vertices*, *\**, *density=2*, *radius=1*, *start\_angle=None*, *\*\*kwargs*)[¶](#manim.mobject.geometry.polygram.RegularPolygram._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **num\_vertices** (*int*)
            * **density** (*int*)
            * **radius** (*float*)
            * **start\_angle** (*float* *|* *None*)
            * **kwargs** (*Any*)

        Return type:
        :   None