# Source: https://docs.manim.community/en/stable/reference/manim.animation.changing.AnimatedBoundary.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

AnimatedBoundary[¶](#animatedboundary "Link to this heading")
=============================================================

Qualified name: `manim.animation.changing.AnimatedBoundary`

*class* AnimatedBoundary(*vmobject, colors=[ManimColor('#29ABCA'), ManimColor('#9CDCEB'), ManimColor('#236B8E'), ManimColor('#736357')], max\_stroke\_width=3, cycle\_rate=0.5, back\_and\_forth=True, draw\_rate\_func=<function smooth>, fade\_rate\_func=<function smooth>, \*\*kwargs*)[[source]](../_modules/manim/animation/changing.html#AnimatedBoundary)[¶](#manim.animation.changing.AnimatedBoundary "Link to this definition")
:   Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

    Boundary of a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") with animated color change.

    Examples

    Example: AnimatedBoundaryExample [¶](#animatedboundaryexample)

    [
    ](./AnimatedBoundaryExample-1.mp4)

    ```
    from manim import *

    class AnimatedBoundaryExample(Scene):
        def construct(self):
            text = Text("So shiny!")
            boundary = AnimatedBoundary(text, colors=[RED, GREEN, BLUE],
                                        cycle_rate=3)
            self.add(text, boundary)
            self.wait(2)

    ```

    ```

    class AnimatedBoundaryExample(Scene):
        def construct(self):
            text = Text("So shiny!")
            boundary = AnimatedBoundary(text, colors=[RED, GREEN, BLUE],
                                        cycle_rate=3)
            self.add(text, boundary)
            self.wait(2)


    ```

    Methods

    |  |  |
    | --- | --- |
    | `full_family_become_partial` |  |
    | `update_boundary_copies` |  |

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

    \_original\_\_init\_\_(*vmobject, colors=[ManimColor('#29ABCA'), ManimColor('#9CDCEB'), ManimColor('#236B8E'), ManimColor('#736357')], max\_stroke\_width=3, cycle\_rate=0.5, back\_and\_forth=True, draw\_rate\_func=<function smooth>, fade\_rate\_func=<function smooth>, \*\*kwargs*)[¶](#manim.animation.changing.AnimatedBoundary._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.