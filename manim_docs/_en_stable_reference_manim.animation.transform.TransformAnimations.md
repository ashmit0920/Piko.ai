# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformAnimations.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

TransformAnimations[¶](#transformanimations "Link to this heading")
===================================================================

Qualified name: `manim.animation.transform.TransformAnimations`

*class* TransformAnimations(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform.html#TransformAnimations)[¶](#manim.animation.transform.TransformAnimations "Link to this definition")
:   Bases: [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

    Methods

    |  |  |
    | --- | --- |
    | [`interpolate`](#manim.animation.transform.TransformAnimations.interpolate "manim.animation.transform.TransformAnimations.interpolate") | Set the animation progress. |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    Parameters:
    :   * **start\_anim** ([*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"))
        * **end\_anim** ([*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"))
        * **rate\_func** (*Callable*)

    \_original\_\_init\_\_(*start\_anim*, *end\_anim*, *rate\_func=<function squish\_rate\_func.<locals>.result>*, *\*\*kwargs*)[¶](#manim.animation.transform.TransformAnimations._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **start\_anim** ([*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"))
            * **end\_anim** ([*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"))
            * **rate\_func** (*Callable*)

        Return type:
        :   None

    interpolate(*alpha*)[[source]](../_modules/manim/animation/transform.html#TransformAnimations.interpolate)[¶](#manim.animation.transform.TransformAnimations.interpolate "Link to this definition")
    :   Set the animation progress.

        This method gets called for every frame during an animation.

        Parameters:
        :   **alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
            the end.

        Return type:
        :   None