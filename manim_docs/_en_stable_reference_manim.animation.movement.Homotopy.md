# Source: https://docs.manim.community/en/stable/reference/manim.animation.movement.Homotopy.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Homotopy[¶](#homotopy "Link to this heading")
=============================================

Qualified name: `manim.animation.movement.Homotopy`

*class* Homotopy(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/movement.html#Homotopy)[¶](#manim.animation.movement.Homotopy "Link to this definition")
:   Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    A Homotopy.

    This is an animation transforming the points of a mobject according
    to the specified transformation function. With the parameter \(t\)
    moving from 0 to 1 throughout the animation and \((x, y, z)\)
    describing the coordinates of the point of a mobject,
    the function passed to the `homotopy` keyword argument should
    transform the tuple \((x, y, z, t)\) to \((x', y', z')\),
    the coordinates the original point is transformed to at time \(t\).

    Parameters:
    :   * **homotopy** (*Callable**[**[**float**,* *float**,* *float**,* *float**]**,* *tuple**[**float**,* *float**,* *float**]**]*) – A function mapping \((x, y, z, t)\) to \((x', y', z')\).
        * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject transformed under the given homotopy.
        * **run\_time** (*float*) – The run time of the animation.
        * **apply\_function\_kwargs** (*dict**[**str**,* *Any**]* *|* *None*) – Keyword arguments propagated to `Mobject.apply_function()`.
        * **kwargs** – Further keyword arguments passed to the parent class.

    Examples

    Example: HomotopyExample [¶](#homotopyexample)

    [
    ](./HomotopyExample-1.mp4)

    ```
    from manim import *

    class HomotopyExample(Scene):
        def construct(self):
            square = Square()

            def homotopy(x, y, z, t):
                if t <= 0.25:
                    progress = t / 0.25
                    return (x, y + progress * 0.2 * np.sin(x), z)
                else:
                    wave_progress = (t - 0.25) / 0.75
                    return (x, y + 0.2 * np.sin(x + 10 * wave_progress), z)

            self.play(Homotopy(homotopy, square, rate_func= linear, run_time=2))

    ```

    ```

    class HomotopyExample(Scene):
        def construct(self):
            square = Square()

            def homotopy(x, y, z, t):
                if t <= 0.25:
                    progress = t / 0.25
                    return (x, y + progress * 0.2 * np.sin(x), z)
                else:
                    wave_progress = (t - 0.25) / 0.75
                    return (x, y + 0.2 * np.sin(x + 10 * wave_progress), z)

            self.play(Homotopy(homotopy, square, rate_func= linear, run_time=2))


    ```

    Methods

    |  |  |
    | --- | --- |
    | `function_at_time_t` |  |
    | `interpolate_submobject` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*homotopy*, *mobject*, *run\_time=3*, *apply\_function\_kwargs=None*, *\*\*kwargs*)[¶](#manim.animation.movement.Homotopy._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **homotopy** (*Callable**[**[**float**,* *float**,* *float**,* *float**]**,* *tuple**[**float**,* *float**,* *float**]**]*)
            * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **run\_time** (*float*)
            * **apply\_function\_kwargs** (*dict**[**str**,* *Any**]* *|* *None*)

        Return type:
        :   None