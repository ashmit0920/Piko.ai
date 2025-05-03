# Source: https://docs.manim.community/en/stable/reference/manim.animation.creation.Uncreate.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Uncreate[¶](#uncreate "Link to this heading")
=============================================

Qualified name: `manim.animation.creation.Uncreate`

*class* Uncreate(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/creation.html#Uncreate)[¶](#manim.animation.creation.Uncreate "Link to this definition")
:   Bases: [`Create`](manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create")

    Like [`Create`](manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create") but in reverse.

    Examples

    Example: ShowUncreate [¶](#showuncreate)

    [
    ](./ShowUncreate-1.mp4)

    ```
    from manim import *

    class ShowUncreate(Scene):
        def construct(self):
            self.play(Uncreate(Square()))

    ```

    ```

    class ShowUncreate(Scene):
        def construct(self):
            self.play(Uncreate(Square()))


    ```

    See also

    [`Create`](manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create")

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   * **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") *|* *OpenGLVMobject*)
        * **reverse\_rate\_function** (*bool*)
        * **remover** (*bool*)

    \_original\_\_init\_\_(*mobject*, *reverse\_rate\_function=True*, *remover=True*, *\*\*kwargs*)[¶](#manim.animation.creation.Uncreate._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") *|* *OpenGLVMobject*)
            * **reverse\_rate\_function** (*bool*)
            * **remover** (*bool*)

        Return type:
        :   None