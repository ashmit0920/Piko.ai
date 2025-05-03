# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Ellipse.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Ellipse[¶](#ellipse "Link to this heading")
===========================================

Qualified name: `manim.mobject.geometry.arc.Ellipse`

*class* Ellipse(*width=2*, *height=1*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/arc.html#Ellipse)[¶](#manim.mobject.geometry.arc.Ellipse "Link to this definition")
:   Bases: [`Circle`](manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle")

    A circular shape; oval, circle.

    Parameters:
    :   * **width** (*float*) – The horizontal width of the ellipse.
        * **height** (*float*) – The vertical height of the ellipse.
        * **kwargs** (*Any*) – Additional arguments to be passed to [`Circle`](manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle").

    Examples

    Example: EllipseExample [¶](#ellipseexample)

    ![../_images/EllipseExample-1.png](../_images/EllipseExample-1.png)

    ```
    from manim import *

    class EllipseExample(Scene):
        def construct(self):
            ellipse_1 = Ellipse(width=2.0, height=4.0, color=BLUE_B)
            ellipse_2 = Ellipse(width=4.0, height=1.0, color=BLUE_D)
            ellipse_group = Group(ellipse_1,ellipse_2).arrange(buff=1)
            self.add(ellipse_group)

    ```

    ```

    class EllipseExample(Scene):
        def construct(self):
            ellipse_1 = Ellipse(width=2.0, height=4.0, color=BLUE_B)
            ellipse_2 = Ellipse(width=4.0, height=1.0, color=BLUE_D)
            ellipse_group = Group(ellipse_1,ellipse_2).arrange(buff=1)
            self.add(ellipse_group)


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

    \_original\_\_init\_\_(*width=2*, *height=1*, *\*\*kwargs*)[¶](#manim.mobject.geometry.arc.Ellipse._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **width** (*float*)
            * **height** (*float*)
            * **kwargs** (*Any*)

        Return type:
        :   None