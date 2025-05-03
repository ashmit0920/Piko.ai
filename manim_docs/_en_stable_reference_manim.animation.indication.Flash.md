# Source: https://docs.manim.community/en/stable/reference/manim.animation.indication.Flash.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Flash[¶](#flash "Link to this heading")
=======================================

Qualified name: `manim.animation.indication.Flash`

*class* Flash(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/indication.html#Flash)[¶](#manim.animation.indication.Flash "Link to this definition")
:   Bases: [`AnimationGroup`](manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")

    Send out lines in all directions.

    Parameters:
    :   * **point** (*np.ndarray* *|* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The center of the flash lines. If it is a `Mobject` its center will be used.
        * **line\_length** (*float*) – The length of the flash lines.
        * **num\_lines** (*int*) – The number of flash lines.
        * **flash\_radius** (*float*) – The distance from point at which the flash lines start.
        * **line\_stroke\_width** (*int*) – The stroke width of the flash lines.
        * **color** (*str*) – The color of the flash lines.
        * **time\_width** (*float*) – The time width used for the flash lines. See `ShowPassingFlash` for more details.
        * **run\_time** (*float*) – The duration of the animation.
        * **kwargs** – Additional arguments to be passed to the [`Succession`](manim.animation.composition.Succession.html#manim.animation.composition.Succession "manim.animation.composition.Succession") constructor

    Examples

    Example: UsingFlash [¶](#usingflash)

    [
    ](./UsingFlash-1.mp4)

    ```
    from manim import *

    class UsingFlash(Scene):
        def construct(self):
            dot = Dot(color=YELLOW).shift(DOWN)
            self.add(Tex("Flash the dot below:"), dot)
            self.play(Flash(dot))
            self.wait()

    ```

    ```

    class UsingFlash(Scene):
        def construct(self):
            dot = Dot(color=YELLOW).shift(DOWN)
            self.add(Tex("Flash the dot below:"), dot)
            self.play(Flash(dot))
            self.wait()


    ```

    Example: FlashOnCircle [¶](#flashoncircle)

    [
    ](./FlashOnCircle-1.mp4)

    ```
    from manim import *

    class FlashOnCircle(Scene):
        def construct(self):
            radius = 2
            circle = Circle(radius)
            self.add(circle)
            self.play(Flash(
                circle, line_length=1,
                num_lines=30, color=RED,
                flash_radius=radius+SMALL_BUFF,
                time_width=0.3, run_time=2,
                rate_func = rush_from
            ))

    ```

    ```

    class FlashOnCircle(Scene):
        def construct(self):
            radius = 2
            circle = Circle(radius)
            self.add(circle)
            self.play(Flash(
                circle, line_length=1,
                num_lines=30, color=RED,
                flash_radius=radius+SMALL_BUFF,
                time_width=0.3, run_time=2,
                rate_func = rush_from
            ))


    ```

    Methods

    |  |  |
    | --- | --- |
    | `create_line_anims` |  |
    | `create_lines` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*point*, *line\_length=0.2*, *num\_lines=12*, *flash\_radius=0.1*, *line\_stroke\_width=3*, *color=ManimColor('#FFFF00')*, *time\_width=1*, *run\_time=1.0*, *\*\*kwargs*)[¶](#manim.animation.indication.Flash._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **point** (*ndarray* *|* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **line\_length** (*float*)
            * **num\_lines** (*int*)
            * **flash\_radius** (*float*)
            * **line\_stroke\_width** (*int*)
            * **color** (*str*)
            * **time\_width** (*float*)
            * **run\_time** (*float*)

        Return type:
        :   None