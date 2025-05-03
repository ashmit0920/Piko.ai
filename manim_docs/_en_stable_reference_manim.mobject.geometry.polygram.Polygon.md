# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Polygon[¶](#polygon "Link to this heading")
===========================================

Qualified name: `manim.mobject.geometry.polygram.Polygon`

*class* Polygon(*\*vertices*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/polygram.html#Polygon)[¶](#manim.mobject.geometry.polygram.Polygon "Link to this definition")
:   Bases: [`Polygram`](manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram")

    A shape consisting of one closed loop of vertices.

    Parameters:
    :   * **vertices** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – The vertices of the [`Polygon`](#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon").
        * **kwargs** (*Any*) – Forwarded to the parent constructor.

    Examples

    Example: PolygonExample [¶](#polygonexample)

    ![../_images/PolygonExample-1.png](../_images/PolygonExample-1.png)

    ```
    from manim import *

    class PolygonExample(Scene):
        def construct(self):
            isosceles = Polygon([-5, 1.5, 0], [-2, 1.5, 0], [-3.5, -2, 0])
            position_list = [
                [4, 1, 0],  # middle right
                [4, -2.5, 0],  # bottom right
                [0, -2.5, 0],  # bottom left
                [0, 3, 0],  # top left
                [2, 1, 0],  # middle
                [4, 3, 0],  # top right
            ]
            square_and_triangles = Polygon(*position_list, color=PURPLE_B)
            self.add(isosceles, square_and_triangles)

    ```

    ```

    class PolygonExample(Scene):
        def construct(self):
            isosceles = Polygon([-5, 1.5, 0], [-2, 1.5, 0], [-3.5, -2, 0])
            position_list = [
                [4, 1, 0],  # middle right
                [4, -2.5, 0],  # bottom right
                [0, -2.5, 0],  # bottom left
                [0, 3, 0],  # top left
                [2, 1, 0],  # middle
                [4, 3, 0],  # top right
            ]
            square_and_triangles = Polygon(*position_list, color=PURPLE_B)
            self.add(isosceles, square_and_triangles)


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

    \_original\_\_init\_\_(*\*vertices*, *\*\*kwargs*)[¶](#manim.mobject.geometry.polygram.Polygon._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **vertices** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
            * **kwargs** (*Any*)

        Return type:
        :   None