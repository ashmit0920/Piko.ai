# Source: https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromAlphaFunc.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

UpdateFromAlphaFunc[¶](#updatefromalphafunc "Link to this heading")
===================================================================

Qualified name: `manim.animation.updaters.update.UpdateFromAlphaFunc`

*class* UpdateFromAlphaFunc(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/updaters/update.html#UpdateFromAlphaFunc)[¶](#manim.animation.updaters.update.UpdateFromAlphaFunc "Link to this definition")
:   Bases: [`UpdateFromFunc`](manim.animation.updaters.update.UpdateFromFunc.html#manim.animation.updaters.update.UpdateFromFunc "manim.animation.updaters.update.UpdateFromFunc")

    Methods

    |  |  |
    | --- | --- |
    | [`interpolate_mobject`](#manim.animation.updaters.update.UpdateFromAlphaFunc.interpolate_mobject "manim.animation.updaters.update.UpdateFromAlphaFunc.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **update\_function** (*Callable**[**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]**,* *Any**]*)
        * **suspend\_mobject\_updating** (*bool*)

    \_original\_\_init\_\_(*mobject*, *update\_function*, *suspend\_mobject\_updating=False*, *\*\*kwargs*)[¶](#manim.animation.updaters.update.UpdateFromAlphaFunc._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **update\_function** (*Callable**[**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]**,* *Any**]*)
            * **suspend\_mobject\_updating** (*bool*)

        Return type:
        :   None

    interpolate\_mobject(*alpha*)[[source]](../_modules/manim/animation/updaters/update.html#UpdateFromAlphaFunc.interpolate_mobject)[¶](#manim.animation.updaters.update.UpdateFromAlphaFunc.interpolate_mobject "Link to this definition")
    :   Interpolates the mobject of the `Animation` based on alpha value.

        Parameters:
        :   **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
            is completed. For example, alpha-values of 0, 0.5, and 1 correspond
            to the animation being completed 0%, 50%, and 100%, respectively.

        Return type:
        :   None