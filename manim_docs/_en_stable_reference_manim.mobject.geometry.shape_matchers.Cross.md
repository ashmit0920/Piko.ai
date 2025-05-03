# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.Cross.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Cross[¶](#cross "Link to this heading")
=======================================

Qualified name: `manim.mobject.geometry.shape\_matchers.Cross`

*class* Cross(*mobject=None*, *stroke\_color=ManimColor('#FC6255')*, *stroke\_width=6.0*, *scale\_factor=1.0*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/shape_matchers.html#Cross)[¶](#manim.mobject.geometry.shape_matchers.Cross "Link to this definition")
:   Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

    Creates a cross.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *|* *None*) – The mobject linked to this instance. It fits the mobject when specified. Defaults to None.
        * **stroke\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – Specifies the color of the cross lines. Defaults to RED.
        * **stroke\_width** (*float*) – Specifies the width of the cross lines. Defaults to 6.
        * **scale\_factor** (*float*) – Scales the cross to the provided units. Defaults to 1.
        * **kwargs** (*Any*)

    Examples

    Example: ExampleCross [¶](#examplecross)

    ![../_images/ExampleCross-1.png](../_images/ExampleCross-1.png)

    ```
    from manim import *

    class ExampleCross(Scene):
        def construct(self):
            cross = Cross()
            self.add(cross)

    ```

    ```

    class ExampleCross(Scene):
        def construct(self):
            cross = Cross()
            self.add(cross)


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

    \_original\_\_init\_\_(*mobject=None*, *stroke\_color=ManimColor('#FC6255')*, *stroke\_width=6.0*, *scale\_factor=1.0*, *\*\*kwargs*)[¶](#manim.mobject.geometry.shape_matchers.Cross._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *|* *None*)
            * **stroke\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
            * **stroke\_width** (*float*)
            * **scale\_factor** (*float*)
            * **kwargs** (*Any*)

        Return type:
        :   None