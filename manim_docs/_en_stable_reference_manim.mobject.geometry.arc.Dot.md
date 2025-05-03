# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Dot.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Dot[¶](#dot "Link to this heading")
===================================

Qualified name: `manim.mobject.geometry.arc.Dot`

*class* Dot(*point=array([0., 0., 0.])*, *radius=0.08*, *stroke\_width=0*, *fill\_opacity=1.0*, *color=ManimColor('#FFFFFF')*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/arc.html#Dot)[¶](#manim.mobject.geometry.arc.Dot "Link to this definition")
:   Bases: [`Circle`](manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle")

    A circle with a very small radius.

    Parameters:
    :   * **point** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – The location of the dot.
        * **radius** (*float*) – The radius of the dot.
        * **stroke\_width** (*float*) – The thickness of the outline of the dot.
        * **fill\_opacity** (*float*) – The opacity of the dot’s fill\_colour
        * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the dot.
        * **kwargs** (*Any*) – Additional arguments to be passed to [`Circle`](manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle")

    Examples

    Example: DotExample [¶](#dotexample)

    ![../_images/DotExample-1.png](../_images/DotExample-1.png)

    ```
    from manim import *

    class DotExample(Scene):
        def construct(self):
            dot1 = Dot(point=LEFT, radius=0.08)
            dot2 = Dot(point=ORIGIN)
            dot3 = Dot(point=RIGHT)
            self.add(dot1,dot2,dot3)

    ```

    ```

    class DotExample(Scene):
        def construct(self):
            dot1 = Dot(point=LEFT, radius=0.08)
            dot2 = Dot(point=ORIGIN)
            dot3 = Dot(point=RIGHT)
            self.add(dot1,dot2,dot3)


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

    \_original\_\_init\_\_(*point=array([0., 0., 0.])*, *radius=0.08*, *stroke\_width=0*, *fill\_opacity=1.0*, *color=ManimColor('#FFFFFF')*, *\*\*kwargs*)[¶](#manim.mobject.geometry.arc.Dot._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **point** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
            * **radius** (*float*)
            * **stroke\_width** (*float*)
            * **fill\_opacity** (*float*)
            * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
            * **kwargs** (*Any*)

        Return type:
        :   None