# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform.Restore.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Restore[¶](#restore "Link to this heading")
===========================================

Qualified name: `manim.animation.transform.Restore`

*class* Restore(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform.html#Restore)[¶](#manim.animation.transform.Restore "Link to this definition")
:   Bases: [`ApplyMethod`](manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

    Transforms a mobject to its last saved state.

    To save the state of a mobject, use the [`save_state()`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.save_state "manim.mobject.mobject.Mobject.save_state") method.

    Examples

    Example: RestoreExample [¶](#restoreexample)

    [
    ](./RestoreExample-1.mp4)

    ```
    from manim import *

    class RestoreExample(Scene):
        def construct(self):
            s = Square()
            s.save_state()
            self.play(FadeIn(s))
            self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2*LEFT).scale(3))
            self.play(s.animate.shift(5*DOWN).rotate(PI/4))
            self.wait()
            self.play(Restore(s), run_time=2)

    ```

    ```

    class RestoreExample(Scene):
        def construct(self):
            s = Square()
            s.save_state()
            self.play(FadeIn(s))
            self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2*LEFT).scale(3))
            self.play(s.animate.shift(5*DOWN).rotate(PI/4))
            self.wait()
            self.play(Restore(s), run_time=2)


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    Parameters:
    :   **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

    \_original\_\_init\_\_(*mobject*, *\*\*kwargs*)[¶](#manim.animation.transform.Restore._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

        Return type:
        :   None