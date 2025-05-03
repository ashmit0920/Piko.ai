# Source: https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotating.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Rotating[¶](#rotating "Link to this heading")
=============================================

Qualified name: `manim.animation.rotation.Rotating`

*class* Rotating(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/rotation.html#Rotating)[¶](#manim.animation.rotation.Rotating "Link to this definition")
:   Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    Methods

    |  |  |
    | --- | --- |
    | [`interpolate_mobject`](#manim.animation.rotation.Rotating.interpolate_mobject "manim.animation.rotation.Rotating.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **axis** (*np.ndarray*)
        * **radians** (*np.ndarray*)
        * **about\_point** (*np.ndarray* *|* *None*)
        * **about\_edge** (*np.ndarray* *|* *None*)
        * **run\_time** (*float*)
        * **rate\_func** (*Callable**[**[**float**]**,* *float**]*)

    \_original\_\_init\_\_(*mobject*, *axis=array([0.*, *0.*, *1.])*, *radians=6.283185307179586*, *about\_point=None*, *about\_edge=None*, *run\_time=5*, *rate\_func=<function linear>*, *\*\*kwargs*)[¶](#manim.animation.rotation.Rotating._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **axis** (*np.ndarray*)
            * **radians** (*np.ndarray*)
            * **about\_point** (*np.ndarray* *|* *None*)
            * **about\_edge** (*np.ndarray* *|* *None*)
            * **run\_time** (*float*)
            * **rate\_func** (*Callable**[**[**float**]**,* *float**]*)

        Return type:
        :   None

    interpolate\_mobject(*alpha*)[[source]](../_modules/manim/animation/rotation.html#Rotating.interpolate_mobject)[¶](#manim.animation.rotation.Rotating.interpolate_mobject "Link to this definition")
    :   Interpolates the mobject of the `Animation` based on alpha value.

        Parameters:
        :   **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
            is completed. For example, alpha-values of 0, 0.5, and 1 correspond
            to the animation being completed 0%, 50%, and 100%, respectively.

        Return type:
        :   None