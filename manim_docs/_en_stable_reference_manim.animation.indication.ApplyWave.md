# Source: https://docs.manim.community/en/stable/reference/manim.animation.indication.ApplyWave.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ApplyWave[¶](#applywave "Link to this heading")
===============================================

Qualified name: `manim.animation.indication.ApplyWave`

*class* ApplyWave(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/indication.html#ApplyWave)[¶](#manim.animation.indication.ApplyWave "Link to this definition")
:   Bases: [`Homotopy`](manim.animation.movement.Homotopy.html#manim.animation.movement.Homotopy "manim.animation.movement.Homotopy")

    Send a wave through the Mobject distorting it temporarily.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to be distorted.
        * **direction** (*np.ndarray*) – The direction in which the wave nudges points of the shape
        * **amplitude** (*float*) – The distance points of the shape get shifted
        * **wave\_func** (*Callable**[**[**float**]**,* *float**]*) – The function defining the shape of one wave flank.
        * **time\_width** (*float*) – The length of the wave relative to the width of the mobject.
        * **ripples** (*int*) – The number of ripples of the wave
        * **run\_time** (*float*) – The duration of the animation.

    Examples

    Example: ApplyingWaves [¶](#applyingwaves)

    [
    ](./ApplyingWaves-1.mp4)

    ```
    from manim import *

    class ApplyingWaves(Scene):
        def construct(self):
            tex = Tex("WaveWaveWaveWaveWave").scale(2)
            self.play(ApplyWave(tex))
            self.play(ApplyWave(
                tex,
                direction=RIGHT,
                time_width=0.5,
                amplitude=0.3
            ))
            self.play(ApplyWave(
                tex,
                rate_func=linear,
                ripples=4
            ))

    ```

    ```

    class ApplyingWaves(Scene):
        def construct(self):
            tex = Tex("WaveWaveWaveWaveWave").scale(2)
            self.play(ApplyWave(tex))
            self.play(ApplyWave(
                tex,
                direction=RIGHT,
                time_width=0.5,
                amplitude=0.3
            ))
            self.play(ApplyWave(
                tex,
                rate_func=linear,
                ripples=4
            ))


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *direction=array([0.*, *1.*, *0.])*, *amplitude=0.2*, *wave\_func=<function smooth>*, *time\_width=1*, *ripples=1*, *run\_time=2*, *\*\*kwargs*)[¶](#manim.animation.indication.ApplyWave._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **direction** (*ndarray*)
            * **amplitude** (*float*)
            * **wave\_func** (*Callable**[**[**float**]**,* *float**]*)
            * **time\_width** (*float*)
            * **ripples** (*int*)
            * **run\_time** (*float*)

        Return type:
        :   None