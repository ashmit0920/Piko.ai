# Source: https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Blink[¶](#blink "Link to this heading")
=======================================

Qualified name: `manim.animation.indication.Blink`

*class* Blink(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/indication.html#Blink)[¶](#manim.animation.indication.Blink "Link to this definition")
:   Bases: [`Succession`](manim.animation.composition.Succession.html#manim.animation.composition.Succession "manim.animation.composition.Succession")

    Blink the mobject.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to be blinked.
        * **time\_on** (*float*) – The duration that the mobject is shown for one blink.
        * **time\_off** (*float*) – The duration that the mobject is hidden for one blink.
        * **blinks** (*int*) – The number of blinks
        * **hide\_at\_end** (*bool*) – Whether to hide the mobject at the end of the animation.
        * **kwargs** – Additional arguments to be passed to the [`Succession`](manim.animation.composition.Succession.html#manim.animation.composition.Succession "manim.animation.composition.Succession") constructor.

    Examples

    Example: BlinkingExample [¶](#blinkingexample)

    [
    ](./BlinkingExample-1.mp4)

    ```
    from manim import *

    class BlinkingExample(Scene):
        def construct(self):
            text = Text("Blinking").scale(1.5)
            self.add(text)
            self.play(Blink(text, blinks=3))

    ```

    ```

    class BlinkingExample(Scene):
        def construct(self):
            text = Text("Blinking").scale(1.5)
            self.add(text)
            self.play(Blink(text, blinks=3))


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *time\_on=0.5*, *time\_off=0.5*, *blinks=1*, *hide\_at\_end=False*, *\*\*kwargs*)[¶](#manim.animation.indication.Blink._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **time\_on** (*float*)
            * **time\_off** (*float*)
            * **blinks** (*int*)
            * **hide\_at\_end** (*bool*)