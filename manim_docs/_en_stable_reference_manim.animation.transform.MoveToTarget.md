# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform.MoveToTarget.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

MoveToTarget[¶](#movetotarget "Link to this heading")
=====================================================

Qualified name: `manim.animation.transform.MoveToTarget`

*class* MoveToTarget(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform.html#MoveToTarget)[¶](#manim.animation.transform.MoveToTarget "Link to this definition")
:   Bases: [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

    Transforms a mobject to the mobject stored in its `target` attribute.

    After calling the `generate_target()` method, the `target`
    attribute of the mobject is populated with a copy of it. After modifying the attribute,
    playing the [`MoveToTarget`](#manim.animation.transform.MoveToTarget "manim.animation.transform.MoveToTarget") animation transforms the original mobject
    into the modified one stored in the `target` attribute.

    Examples

    Example: MoveToTargetExample [¶](#movetotargetexample)

    [
    ](./MoveToTargetExample-1.mp4)

    ```
    from manim import *

    class MoveToTargetExample(Scene):
        def construct(self):
            c = Circle()

            c.generate_target()
            c.target.set_fill(color=GREEN, opacity=0.5)
            c.target.shift(2*RIGHT + UP).scale(0.5)

            self.add(c)
            self.play(MoveToTarget(c))

    ```

    ```

    class MoveToTargetExample(Scene):
        def construct(self):
            c = Circle()

            c.generate_target()
            c.target.set_fill(color=GREEN, opacity=0.5)
            c.target.shift(2*RIGHT + UP).scale(0.5)

            self.add(c)
            self.play(MoveToTarget(c))


    ```

    Methods

    |  |  |
    | --- | --- |
    | `check_validity_of_input` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    Parameters:
    :   **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

    \_original\_\_init\_\_(*mobject*, *\*\*kwargs*)[¶](#manim.animation.transform.MoveToTarget._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

        Return type:
        :   None