# Source: https://docs.manim.community/en/stable/reference/manim.animation.indication.Indicate.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Indicate[¶](#indicate "Link to this heading")
=============================================

Qualified name: `manim.animation.indication.Indicate`

*class* Indicate(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/indication.html#Indicate)[¶](#manim.animation.indication.Indicate "Link to this definition")
:   Bases: [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

    Indicate a Mobject by temporarily resizing and recoloring it.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to indicate.
        * **scale\_factor** (*float*) – The factor by which the mobject will be temporally scaled
        * **color** (*str*) – The color the mobject temporally takes.
        * **rate\_func** (*Callable**[**[**float**,* *float* *|* *None**]**,* *np.ndarray**]*) – The function defining the animation progress at every point in time.
        * **kwargs** – Additional arguments to be passed to the [`Succession`](manim.animation.composition.Succession.html#manim.animation.composition.Succession "manim.animation.composition.Succession") constructor

    Examples

    Example: UsingIndicate [¶](#usingindicate)

    [
    ](./UsingIndicate-1.mp4)

    ```
    from manim import *

    class UsingIndicate(Scene):
        def construct(self):
            tex = Tex("Indicate").scale(3)
            self.play(Indicate(tex))
            self.wait()

    ```

    ```

    class UsingIndicate(Scene):
        def construct(self):
            tex = Tex("Indicate").scale(3)
            self.play(Indicate(tex))
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

    \_original\_\_init\_\_(*mobject*, *scale\_factor=1.2*, *color=ManimColor('#FFFF00')*, *rate\_func=<function there\_and\_back>*, *\*\*kwargs*)[¶](#manim.animation.indication.Indicate._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **scale\_factor** (*float*)
            * **color** (*str*)
            * **rate\_func** (*Callable**[**[**float**,* *float* *|* *None**]**,* *ndarray**]*)

        Return type:
        :   None