# Source: https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowArrow.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

GrowArrow[¶](#growarrow "Link to this heading")
===============================================

Qualified name: `manim.animation.growing.GrowArrow`

*class* GrowArrow(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/growing.html#GrowArrow)[¶](#manim.animation.growing.GrowArrow "Link to this definition")
:   Bases: [`GrowFromPoint`](manim.animation.growing.GrowFromPoint.html#manim.animation.growing.GrowFromPoint "manim.animation.growing.GrowFromPoint")

    Introduce an [`Arrow`](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow") by growing it from its start toward its tip.

    Parameters:
    :   * **arrow** ([*Arrow*](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")) – The arrow to be introduced.
        * **point\_color** (*str*) – Initial color of the arrow before growing to its full size. Leave empty to match arrow’s color.

    Examples

    Example: GrowArrowExample [¶](#growarrowexample)

    [
    ](./GrowArrowExample-1.mp4)

    ```
    from manim import *

    class GrowArrowExample(Scene):
        def construct(self):
            arrows = [Arrow(2 * LEFT, 2 * RIGHT), Arrow(2 * DR, 2 * UL)]
            VGroup(*arrows).set_x(0).arrange(buff=2)
            self.play(GrowArrow(arrows[0]))
            self.play(GrowArrow(arrows[1], point_color=RED))

    ```

    ```

    class GrowArrowExample(Scene):
        def construct(self):
            arrows = [Arrow(2 * LEFT, 2 * RIGHT), Arrow(2 * DR, 2 * UL)]
            VGroup(*arrows).set_x(0).arrange(buff=2)
            self.play(GrowArrow(arrows[0]))
            self.play(GrowArrow(arrows[1], point_color=RED))


    ```

    Methods

    |  |  |
    | --- | --- |
    | `create_starting_mobject` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*arrow*, *point\_color=None*, *\*\*kwargs*)[¶](#manim.animation.growing.GrowArrow._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **arrow** ([*Arrow*](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow"))
            * **point\_color** (*str*)

        Return type:
        :   None