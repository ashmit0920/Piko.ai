# Source: https://docs.manim.community/en/stable/reference/manim.animation.creation.Unwrite.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Unwrite[¶](#unwrite "Link to this heading")
===========================================

Qualified name: `manim.animation.creation.Unwrite`

*class* Unwrite(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/creation.html#Unwrite)[¶](#manim.animation.creation.Unwrite "Link to this definition")
:   Bases: [`Write`](manim.animation.creation.Write.html#manim.animation.creation.Write "manim.animation.creation.Write")

    Simulate erasing by hand a [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") or a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").

    Parameters:
    :   * **reverse** (*bool*) – Set True to have the animation start erasing from the last submobject first.
        * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))
        * **rate\_func** (*Callable**[**[**float**]**,* *float**]*)

    Examples

    Example: UnwriteReverseTrue [¶](#unwritereversetrue)

    [
    ](./UnwriteReverseTrue-1.mp4)

    ```
    from manim import *

    class UnwriteReverseTrue(Scene):
        def construct(self):
            text = Tex("Alice and Bob").scale(3)
            self.add(text)
            self.play(Unwrite(text))

    ```

    ```

    class UnwriteReverseTrue(Scene):
        def construct(self):
            text = Tex("Alice and Bob").scale(3)
            self.add(text)
            self.play(Unwrite(text))


    ```

    Example: UnwriteReverseFalse [¶](#unwritereversefalse)

    [
    ](./UnwriteReverseFalse-1.mp4)

    ```
    from manim import *

    class UnwriteReverseFalse(Scene):
        def construct(self):
            text = Tex("Alice and Bob").scale(3)
            self.add(text)
            self.play(Unwrite(text, reverse=False))

    ```

    ```

    class UnwriteReverseFalse(Scene):
        def construct(self):
            text = Tex("Alice and Bob").scale(3)
            self.add(text)
            self.play(Unwrite(text, reverse=False))


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*vmobject*, *rate\_func=<function linear>*, *reverse=True*, *\*\*kwargs*)[¶](#manim.animation.creation.Unwrite._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))
            * **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
            * **reverse** (*bool*)

        Return type:
        :   None