# Source: https://docs.manim.community/en/stable/reference/manim.animation.indication.FocusOn.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

FocusOn[¶](#focuson "Link to this heading")
===========================================

Qualified name: `manim.animation.indication.FocusOn`

*class* FocusOn(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/indication.html#FocusOn)[¶](#manim.animation.indication.FocusOn "Link to this definition")
:   Bases: [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

    Shrink a spotlight to a position.

    Parameters:
    :   * **focus\_point** (*np.ndarray* *|* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The point at which to shrink the spotlight. If it is a `Mobject` its center will be used.
        * **opacity** (*float*) – The opacity of the spotlight.
        * **color** (*str*) – The color of the spotlight.
        * **run\_time** (*float*) – The duration of the animation.

    Examples

    Example: UsingFocusOn [¶](#usingfocuson)

    [
    ](./UsingFocusOn-1.mp4)

    ```
    from manim import *

    class UsingFocusOn(Scene):
        def construct(self):
            dot = Dot(color=YELLOW).shift(DOWN)
            self.add(Tex("Focusing on the dot below:"), dot)
            self.play(FocusOn(dot))
            self.wait()

    ```

    ```

    class UsingFocusOn(Scene):
        def construct(self):
            dot = Dot(color=YELLOW).shift(DOWN)
            self.add(Tex("Focusing on the dot below:"), dot)
            self.play(FocusOn(dot))
            self.wait()


    ```

    Methods

    |  |  |
    | --- | --- |
    | `create_target` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*focus\_point*, *opacity=0.2*, *color=ManimColor('#888888')*, *run\_time=2*, *\*\*kwargs*)[¶](#manim.animation.indication.FocusOn._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **focus\_point** (*ndarray* *|* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **opacity** (*float*)
            * **color** (*str*)
            * **run\_time** (*float*)

        Return type:
        :   None