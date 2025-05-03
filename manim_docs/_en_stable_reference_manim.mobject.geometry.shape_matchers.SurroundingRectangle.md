# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

SurroundingRectangle[¶](#surroundingrectangle "Link to this heading")
=====================================================================

Qualified name: `manim.mobject.geometry.shape\_matchers.SurroundingRectangle`

*class* SurroundingRectangle(*\*mobjects*, *color=ManimColor('#FFFF00')*, *buff=0.1*, *corner\_radius=0.0*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/shape_matchers.html#SurroundingRectangle)[¶](#manim.mobject.geometry.shape_matchers.SurroundingRectangle "Link to this definition")
:   Bases: [`RoundedRectangle`](manim.mobject.geometry.polygram.RoundedRectangle.html#manim.mobject.geometry.polygram.RoundedRectangle "manim.mobject.geometry.polygram.RoundedRectangle")

    A rectangle surrounding a [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

    Examples

    Example: SurroundingRectExample [¶](#surroundingrectexample)

    ![../_images/SurroundingRectExample-1.png](../_images/SurroundingRectExample-1.png)

    ```
    from manim import *

    class SurroundingRectExample(Scene):
        def construct(self):
            title = Title("A Quote from Newton")
            quote = Text(
                "If I have seen further than others, \n"
                "it is by standing upon the shoulders of giants.",
                color=BLUE,
            ).scale(0.75)
            box = SurroundingRectangle(quote, color=YELLOW, buff=MED_LARGE_BUFF)

            t2 = Tex(r"Hello World").scale(1.5)
            box2 = SurroundingRectangle(t2, corner_radius=0.2)
            mobjects = VGroup(VGroup(box, quote), VGroup(t2, box2)).arrange(DOWN)
            self.add(title, mobjects)

    ```

    ```

    class SurroundingRectExample(Scene):
        def construct(self):
            title = Title("A Quote from Newton")
            quote = Text(
                "If I have seen further than others, \n"
                "it is by standing upon the shoulders of giants.",
                color=BLUE,
            ).scale(0.75)
            box = SurroundingRectangle(quote, color=YELLOW, buff=MED_LARGE_BUFF)

            t2 = Tex(r"Hello World").scale(1.5)
            box2 = SurroundingRectangle(t2, corner_radius=0.2)
            mobjects = VGroup(VGroup(box, quote), VGroup(t2, box2)).arrange(DOWN)
            self.add(title, mobjects)


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
    :   * **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
        * **buff** (*float*)
        * **corner\_radius** (*float*)
        * **kwargs** (*Any*)

    \_original\_\_init\_\_(*\*mobjects*, *color=ManimColor('#FFFF00')*, *buff=0.1*, *corner\_radius=0.0*, *\*\*kwargs*)[¶](#manim.mobject.geometry.shape_matchers.SurroundingRectangle._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
            * **buff** (*float*)
            * **corner\_radius** (*float*)
            * **kwargs** (*Any*)

        Return type:
        :   None