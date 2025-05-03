# Source: https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Circumscribe[¶](#circumscribe "Link to this heading")
=====================================================

Qualified name: `manim.animation.indication.Circumscribe`

*class* Circumscribe(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/indication.html#Circumscribe)[¶](#manim.animation.indication.Circumscribe "Link to this definition")
:   Bases: [`Succession`](manim.animation.composition.Succession.html#manim.animation.composition.Succession "manim.animation.composition.Succession")

    Draw a temporary line surrounding the mobject.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to be circumscribed.
        * **shape** (*type*) – The shape with which to surround the given mobject. Should be either
          [`Rectangle`](manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle") or [`Circle`](manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle")
        * **fade\_in** – Whether to make the surrounding shape to fade in. It will be drawn otherwise.
        * **fade\_out** – Whether to make the surrounding shape to fade out. It will be undrawn otherwise.
        * **time\_width** – The time\_width of the drawing and undrawing. Gets ignored if either fade\_in or fade\_out is True.
        * **buff** (*float*) – The distance between the surrounding shape and the given mobject.
        * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the surrounding shape.
        * **run\_time** – The duration of the entire animation.
        * **kwargs** – Additional arguments to be passed to the [`Succession`](manim.animation.composition.Succession.html#manim.animation.composition.Succession "manim.animation.composition.Succession") constructor

    Examples

    Example: UsingCircumscribe [¶](#usingcircumscribe)

    [
    ](./UsingCircumscribe-1.mp4)

    ```
    from manim import *

    class UsingCircumscribe(Scene):
        def construct(self):
            lbl = Tex(r"Circum-\\scribe").scale(2)
            self.add(lbl)
            self.play(Circumscribe(lbl))
            self.play(Circumscribe(lbl, Circle))
            self.play(Circumscribe(lbl, fade_out=True))
            self.play(Circumscribe(lbl, time_width=2))
            self.play(Circumscribe(lbl, Circle, True))

    ```

    ```

    class UsingCircumscribe(Scene):
        def construct(self):
            lbl = Tex(r"Circum-\\scribe").scale(2)
            self.add(lbl)
            self.play(Circumscribe(lbl))
            self.play(Circumscribe(lbl, Circle))
            self.play(Circumscribe(lbl, fade_out=True))
            self.play(Circumscribe(lbl, time_width=2))
            self.play(Circumscribe(lbl, Circle, True))


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *shape=<class 'manim.mobject.geometry.polygram.Rectangle'>*, *fade\_in=False*, *fade\_out=False*, *time\_width=0.3*, *buff=0.1*, *color=ManimColor('#FFFF00')*, *run\_time=1*, *stroke\_width=4*, *\*\*kwargs*)[¶](#manim.animation.indication.Circumscribe._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **shape** (*type*)
            * **buff** (*float*)
            * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))