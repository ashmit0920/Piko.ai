# Source: https://docs.manim.community/en/stable/reference/manim.animation.creation.Write.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Write[¶](#write "Link to this heading")
=======================================

Qualified name: `manim.animation.creation.Write`

*class* Write(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/creation.html#Write)[¶](#manim.animation.creation.Write "Link to this definition")
:   Bases: [`DrawBorderThenFill`](manim.animation.creation.DrawBorderThenFill.html#manim.animation.creation.DrawBorderThenFill "manim.animation.creation.DrawBorderThenFill")

    Simulate hand-writing a [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") or hand-drawing a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").

    Examples

    Example: ShowWrite [¶](#showwrite)

    [
    ](./ShowWrite-1.mp4)

    ```
    from manim import *

    class ShowWrite(Scene):
        def construct(self):
            self.play(Write(Text("Hello", font_size=144)))

    ```

    ```

    class ShowWrite(Scene):
        def construct(self):
            self.play(Write(Text("Hello", font_size=144)))


    ```

    Example: ShowWriteReversed [¶](#showwritereversed)

    [
    ](./ShowWriteReversed-1.mp4)

    ```
    from manim import *

    class ShowWriteReversed(Scene):
        def construct(self):
            self.play(Write(Text("Hello", font_size=144), reverse=True, remover=False))

    ```

    ```

    class ShowWriteReversed(Scene):
        def construct(self):
            self.play(Write(Text("Hello", font_size=144), reverse=True, remover=False))


    ```

    Tests

    Check that creating empty [`Write`](#manim.animation.creation.Write "manim.animation.creation.Write") animations works:

    ```
    >>> from manim import Write, Text
    >>> Write(Text(''))
    Write(Text(''))

    ```

    Methods

    |  |  |
    | --- | --- |
    | [`begin`](#manim.animation.creation.Write.begin "manim.animation.creation.Write.begin") | Begin the animation. |
    | [`finish`](#manim.animation.creation.Write.finish "manim.animation.creation.Write.finish") | Finish the animation. |
    | `reverse_submobjects` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") *|* *OpenGLVMobject*)
        * **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
        * **reverse** (*bool*)

    \_original\_\_init\_\_(*vmobject*, *rate\_func=<function linear>*, *reverse=False*, *\*\*kwargs*)[¶](#manim.animation.creation.Write._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") *|* *OpenGLVMobject*)
            * **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
            * **reverse** (*bool*)

        Return type:
        :   None

    begin()[[source]](../_modules/manim/animation/creation.html#Write.begin)[¶](#manim.animation.creation.Write.begin "Link to this definition")
    :   Begin the animation.

        This method is called right as an animation is being played. As much
        initialization as possible, especially any mobject copying, should live in this
        method.

        Return type:
        :   None

    finish()[[source]](../_modules/manim/animation/creation.html#Write.finish)[¶](#manim.animation.creation.Write.finish "Link to this definition")
    :   Finish the animation.

        This method gets called when the animation is over.

        Return type:
        :   None