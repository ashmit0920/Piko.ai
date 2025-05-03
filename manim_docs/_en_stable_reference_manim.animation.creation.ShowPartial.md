# Source: https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowPartial.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ShowPartial[¶](#showpartial "Link to this heading")
===================================================

Qualified name: `manim.animation.creation.ShowPartial`

*class* ShowPartial(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/creation.html#ShowPartial)[¶](#manim.animation.creation.ShowPartial "Link to this definition")
:   Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    Abstract class for Animations that show the VMobject partially.

    Raises:
    :   **TypeError** – If `mobject` is not an instance of [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").

    Parameters:
    :   **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") *|* *OpenGLVMobject* *|* *OpenGLSurface* *|* *None*)

    See also

    [`Create`](manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create"), [`ShowPassingFlash`](manim.animation.indication.ShowPassingFlash.html#manim.animation.indication.ShowPassingFlash "manim.animation.indication.ShowPassingFlash")

    Methods

    |  |  |
    | --- | --- |
    | `interpolate_submobject` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *\*\*kwargs*)[¶](#manim.animation.creation.ShowPartial._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") *|* *OpenGLVMobject* *|* *OpenGLSurface* *|* *None*)