# Source: https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.MaintainPositionRelativeTo.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

MaintainPositionRelativeTo[¶](#maintainpositionrelativeto "Link to this heading")
=================================================================================

Qualified name: `manim.animation.updaters.update.MaintainPositionRelativeTo`

*class* MaintainPositionRelativeTo(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/updaters/update.html#MaintainPositionRelativeTo)[¶](#manim.animation.updaters.update.MaintainPositionRelativeTo "Link to this definition")
:   Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    Methods

    |  |  |
    | --- | --- |
    | [`interpolate_mobject`](#manim.animation.updaters.update.MaintainPositionRelativeTo.interpolate_mobject "manim.animation.updaters.update.MaintainPositionRelativeTo.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **tracked\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

    \_original\_\_init\_\_(*mobject*, *tracked\_mobject*, *\*\*kwargs*)[¶](#manim.animation.updaters.update.MaintainPositionRelativeTo._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **tracked\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

        Return type:
        :   None

    interpolate\_mobject(*alpha*)[[source]](../_modules/manim/animation/updaters/update.html#MaintainPositionRelativeTo.interpolate_mobject)[¶](#manim.animation.updaters.update.MaintainPositionRelativeTo.interpolate_mobject "Link to this definition")
    :   Interpolates the mobject of the `Animation` based on alpha value.

        Parameters:
        :   **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
            is completed. For example, alpha-values of 0, 0.5, and 1 correspond
            to the animation being completed 0%, 50%, and 100%, respectively.

        Return type:
        :   None