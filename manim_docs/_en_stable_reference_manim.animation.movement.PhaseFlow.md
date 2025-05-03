# Source: https://docs.manim.community/en/stable/reference/manim.animation.movement.PhaseFlow.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

PhaseFlow[¶](#phaseflow "Link to this heading")
===============================================

Qualified name: `manim.animation.movement.PhaseFlow`

*class* PhaseFlow(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/movement.html#PhaseFlow)[¶](#manim.animation.movement.PhaseFlow "Link to this definition")
:   Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    Methods

    |  |  |
    | --- | --- |
    | [`interpolate_mobject`](#manim.animation.movement.PhaseFlow.interpolate_mobject "manim.animation.movement.PhaseFlow.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   * **function** (*Callable**[**[**np.ndarray**]**,* *np.ndarray**]*)
        * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **virtual\_time** (*float*)
        * **suspend\_mobject\_updating** (*bool*)
        * **rate\_func** (*Callable**[**[**float**]**,* *float**]*)

    \_original\_\_init\_\_(*function*, *mobject*, *virtual\_time=1*, *suspend\_mobject\_updating=False*, *rate\_func=<function linear>*, *\*\*kwargs*)[¶](#manim.animation.movement.PhaseFlow._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **function** (*Callable**[**[**np.ndarray**]**,* *np.ndarray**]*)
            * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **virtual\_time** (*float*)
            * **suspend\_mobject\_updating** (*bool*)
            * **rate\_func** (*Callable**[**[**float**]**,* *float**]*)

        Return type:
        :   None

    interpolate\_mobject(*alpha*)[[source]](../_modules/manim/animation/movement.html#PhaseFlow.interpolate_mobject)[¶](#manim.animation.movement.PhaseFlow.interpolate_mobject "Link to this definition")
    :   Interpolates the mobject of the `Animation` based on alpha value.

        Parameters:
        :   **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
            is completed. For example, alpha-values of 0, 0.5, and 1 correspond
            to the animation being completed 0%, 50%, and 100%, respectively.

        Return type:
        :   None