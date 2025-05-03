# Source: https://docs.manim.community/en/stable/reference/manim.animation.movement.SmoothedVectorizedHomotopy.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

SmoothedVectorizedHomotopy[¶](#smoothedvectorizedhomotopy "Link to this heading")
=================================================================================

Qualified name: `manim.animation.movement.SmoothedVectorizedHomotopy`

*class* SmoothedVectorizedHomotopy(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/movement.html#SmoothedVectorizedHomotopy)[¶](#manim.animation.movement.SmoothedVectorizedHomotopy "Link to this definition")
:   Bases: [`Homotopy`](manim.animation.movement.Homotopy.html#manim.animation.movement.Homotopy "manim.animation.movement.Homotopy")

    Methods

    |  |  |
    | --- | --- |
    | `interpolate_submobject` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   * **homotopy** (*Callable**[**[**float**,* *float**,* *float**,* *float**]**,* *tuple**[**float**,* *float**,* *float**]**]*)
        * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **run\_time** (*float*)
        * **apply\_function\_kwargs** (*dict**[**str**,* *Any**]* *|* *None*)

    \_original\_\_init\_\_(*homotopy*, *mobject*, *run\_time=3*, *apply\_function\_kwargs=None*, *\*\*kwargs*)[¶](#manim.animation.movement.SmoothedVectorizedHomotopy._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **homotopy** (*Callable**[**[**float**,* *float**,* *float**,* *float**]**,* *tuple**[**float**,* *float**,* *float**]**]*)
            * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **run\_time** (*float*)
            * **apply\_function\_kwargs** (*dict**[**str**,* *Any**]* *|* *None*)

        Return type:
        :   None