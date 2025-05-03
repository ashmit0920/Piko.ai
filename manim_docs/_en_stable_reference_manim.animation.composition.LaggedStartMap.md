# Source: https://docs.manim.community/en/stable/reference/manim.animation.composition.LaggedStartMap.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

LaggedStartMap[¶](#laggedstartmap "Link to this heading")
=========================================================

Qualified name: `manim.animation.composition.LaggedStartMap`

*class* LaggedStartMap(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/composition.html#LaggedStartMap)[¶](#manim.animation.composition.LaggedStartMap "Link to this definition")
:   Bases: [`LaggedStart`](manim.animation.composition.LaggedStart.html#manim.animation.composition.LaggedStart "manim.animation.composition.LaggedStart")

    Plays a series of [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") while mapping a function to submobjects.

    Parameters:
    :   * **AnimationClass** (*Callable**[**...**,* [*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")*]*) – [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") to apply to mobject.
        * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") whose submobjects the animation, and optionally the function,
          are to be applied.
        * **arg\_creator** (*Callable**[**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]**,* *str**]*) – Function which will be applied to [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
        * **run\_time** (*float*) – The duration of the animation in seconds.

    Examples

    Example: LaggedStartMapExample [¶](#laggedstartmapexample)

    [
    ](./LaggedStartMapExample-1.mp4)

    ```
    from manim import *

    class LaggedStartMapExample(Scene):
        def construct(self):
            title = Tex("LaggedStartMap").to_edge(UP, buff=LARGE_BUFF)
            dots = VGroup(
                *[Dot(radius=0.16) for _ in range(35)]
                ).arrange_in_grid(rows=5, cols=7, buff=MED_LARGE_BUFF)
            self.add(dots, title)

            # Animate yellow ripple effect
            for mob in dots, title:
                self.play(LaggedStartMap(
                    ApplyMethod, mob,
                    lambda m : (m.set_color, YELLOW),
                    lag_ratio = 0.1,
                    rate_func = there_and_back,
                    run_time = 2
                ))

    ```

    ```

    class LaggedStartMapExample(Scene):
        def construct(self):
            title = Tex("LaggedStartMap").to_edge(UP, buff=LARGE_BUFF)
            dots = VGroup(
                *[Dot(radius=0.16) for _ in range(35)]
                ).arrange_in_grid(rows=5, cols=7, buff=MED_LARGE_BUFF)
            self.add(dots, title)

            # Animate yellow ripple effect
            for mob in dots, title:
                self.play(LaggedStartMap(
                    ApplyMethod, mob,
                    lambda m : (m.set_color, YELLOW),
                    lag_ratio = 0.1,
                    rate_func = there_and_back,
                    run_time = 2
                ))


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*AnimationClass*, *mobject*, *arg\_creator=None*, *run\_time=2*, *\*\*kwargs*)[¶](#manim.animation.composition.LaggedStartMap._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **AnimationClass** (*Callable**[**[**...**]**,* [*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")*]*)
            * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **arg\_creator** (*Callable**[**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]**,* *str**]*)
            * **run\_time** (*float*)

        Return type:
        :   None