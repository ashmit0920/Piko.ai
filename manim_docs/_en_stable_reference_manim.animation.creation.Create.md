# Source: https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Create[¶](#create "Link to this heading")
=========================================

Qualified name: `manim.animation.creation.Create`

*class* Create(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/creation.html#Create)[¶](#manim.animation.creation.Create "Link to this definition")
:   Bases: [`ShowPartial`](manim.animation.creation.ShowPartial.html#manim.animation.creation.ShowPartial "manim.animation.creation.ShowPartial")

    Incrementally show a VMobject.

    Parameters:
    :   * **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") *|* *OpenGLVMobject* *|* *OpenGLSurface*) – The VMobject to animate.
        * **lag\_ratio** (*float*)
        * **introducer** (*bool*)

    Raises:
    :   **TypeError** – If `mobject` is not an instance of [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").

    Examples

    Example: CreateScene [¶](#createscene)

    [
    ](./CreateScene-1.mp4)

    ```
    from manim import *

    class CreateScene(Scene):
        def construct(self):
            self.play(Create(Square()))

    ```

    ```

    class CreateScene(Scene):
        def construct(self):
            self.play(Create(Square()))


    ```

    See also

    [`ShowPassingFlash`](manim.animation.indication.ShowPassingFlash.html#manim.animation.indication.ShowPassingFlash "manim.animation.indication.ShowPassingFlash")

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *lag\_ratio=1.0*, *introducer=True*, *\*\*kwargs*)[¶](#manim.animation.creation.Create._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") *|* *OpenGLVMobject* *|* *OpenGLSurface*)
            * **lag\_ratio** (*float*)
            * **introducer** (*bool*)

        Return type:
        :   None