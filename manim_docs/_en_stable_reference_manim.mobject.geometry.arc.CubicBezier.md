# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CubicBezier.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

CubicBezier[¶](#cubicbezier "Link to this heading")
===================================================

Qualified name: `manim.mobject.geometry.arc.CubicBezier`

*class* CubicBezier(*start\_anchor*, *start\_handle*, *end\_handle*, *end\_anchor*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/arc.html#CubicBezier)[¶](#manim.mobject.geometry.arc.CubicBezier "Link to this definition")
:   Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    A cubic Bézier curve.

    Example

    Example: BezierSplineExample [¶](#beziersplineexample)

    ![../_images/BezierSplineExample-1.png](../_images/BezierSplineExample-1.png)

    ```
    from manim import *

    class BezierSplineExample(Scene):
        def construct(self):
            p1 = np.array([-3, 1, 0])
            p1b = p1 + [1, 0, 0]
            d1 = Dot(point=p1).set_color(BLUE)
            l1 = Line(p1, p1b)
            p2 = np.array([3, -1, 0])
            p2b = p2 - [1, 0, 0]
            d2 = Dot(point=p2).set_color(RED)
            l2 = Line(p2, p2b)
            bezier = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)
            self.add(l1, d1, l2, d2, bezier)

    ```

    ```

    class BezierSplineExample(Scene):
        def construct(self):
            p1 = np.array([-3, 1, 0])
            p1b = p1 + [1, 0, 0]
            d1 = Dot(point=p1).set_color(BLUE)
            l1 = Line(p1, p1b)
            p2 = np.array([3, -1, 0])
            p2b = p2 - [1, 0, 0]
            d2 = Dot(point=p2).set_color(RED)
            l2 = Line(p2, p2b)
            bezier = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)
            self.add(l1, d1, l2, d2, bezier)


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
    :   * **start\_anchor** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
        * **start\_handle** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
        * **end\_handle** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
        * **end\_anchor** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
        * **kwargs** (*Any*)

    \_original\_\_init\_\_(*start\_anchor*, *start\_handle*, *end\_handle*, *end\_anchor*, *\*\*kwargs*)[¶](#manim.mobject.geometry.arc.CubicBezier._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **start\_anchor** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
            * **start\_handle** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
            * **end\_handle** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
            * **end\_anchor** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
            * **kwargs** (*Any*)

        Return type:
        :   None