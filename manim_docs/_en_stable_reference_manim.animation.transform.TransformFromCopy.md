# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformFromCopy.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

TransformFromCopy[¶](#transformfromcopy "Link to this heading")
===============================================================

Qualified name: `manim.animation.transform.TransformFromCopy`

*class* TransformFromCopy(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform.html#TransformFromCopy)[¶](#manim.animation.transform.TransformFromCopy "Link to this definition")
:   Bases: [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

    Performs a reversed Transform

    Methods

    |  |  |
    | --- | --- |
    | [`interpolate`](#manim.animation.transform.TransformFromCopy.interpolate "manim.animation.transform.TransformFromCopy.interpolate") | Set the animation progress. |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **target\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

    \_original\_\_init\_\_(*mobject*, *target\_mobject*, *\*\*kwargs*)[¶](#manim.animation.transform.TransformFromCopy._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **target\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

        Return type:
        :   None

    interpolate(*alpha*)[[source]](../_modules/manim/animation/transform.html#TransformFromCopy.interpolate)[¶](#manim.animation.transform.TransformFromCopy.interpolate "Link to this definition")
    :   Set the animation progress.

        This method gets called for every frame during an animation.

        Parameters:
        :   **alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
            the end.

        Return type:
        :   None