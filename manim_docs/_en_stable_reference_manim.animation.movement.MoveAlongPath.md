# Source: https://docs.manim.community/en/stable/reference/manim.animation.movement.MoveAlongPath.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

MoveAlongPath[¶](#movealongpath "Link to this heading")
=======================================================

Qualified name: `manim.animation.movement.MoveAlongPath`

*class* MoveAlongPath(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/movement.html#MoveAlongPath)[¶](#manim.animation.movement.MoveAlongPath "Link to this definition")
:   Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    Make one mobject move along the path of another mobject.

    Example: MoveAlongPathExample [¶](#movealongpathexample)

    [
    ](./MoveAlongPathExample-1.mp4)

    ```
    from manim import *

    class MoveAlongPathExample(Scene):
        def construct(self):
            d1 = Dot().set_color(ORANGE)
            l1 = Line(LEFT, RIGHT)
            l2 = VMobject()
            self.add(d1, l1, l2)
            l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center()).set_color(ORANGE)))
            self.play(MoveAlongPath(d1, l1), rate_func=linear)

    ```

    ```

    class MoveAlongPathExample(Scene):
        def construct(self):
            d1 = Dot().set_color(ORANGE)
            l1 = Line(LEFT, RIGHT)
            l2 = VMobject()
            self.add(d1, l1, l2)
            l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center()).set_color(ORANGE)))
            self.play(MoveAlongPath(d1, l1), rate_func=linear)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`interpolate_mobject`](#manim.animation.movement.MoveAlongPath.interpolate_mobject "manim.animation.movement.MoveAlongPath.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **path** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))
        * **suspend\_mobject\_updating** (*bool* *|* *None*)

    \_original\_\_init\_\_(*mobject*, *path*, *suspend\_mobject\_updating=False*, *\*\*kwargs*)[¶](#manim.animation.movement.MoveAlongPath._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **path** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))
            * **suspend\_mobject\_updating** (*bool* *|* *None*)

        Return type:
        :   None

    interpolate\_mobject(*alpha*)[[source]](../_modules/manim/animation/movement.html#MoveAlongPath.interpolate_mobject)[¶](#manim.animation.movement.MoveAlongPath.interpolate_mobject "Link to this definition")
    :   Interpolates the mobject of the `Animation` based on alpha value.

        Parameters:
        :   **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
            is completed. For example, alpha-values of 0, 0.5, and 1 correspond
            to the animation being completed 0%, 50%, and 100%, respectively.

        Return type:
        :   None