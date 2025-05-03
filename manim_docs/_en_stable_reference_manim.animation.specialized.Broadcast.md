# Source: https://docs.manim.community/en/stable/reference/manim.animation.specialized.Broadcast.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Broadcast[¶](#broadcast "Link to this heading")
===============================================

Qualified name: `manim.animation.specialized.Broadcast`

*class* Broadcast(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/specialized.html#Broadcast)[¶](#manim.animation.specialized.Broadcast "Link to this definition")
:   Bases: [`LaggedStart`](manim.animation.composition.LaggedStart.html#manim.animation.composition.LaggedStart "manim.animation.composition.LaggedStart")

    Broadcast a mobject starting from an `initial_width`, up to the actual size of the mobject.

    Parameters:
    :   * **mobject** – The mobject to be broadcast.
        * **focal\_point** (*Sequence**[**float**]*) – The center of the broadcast, by default ORIGIN.
        * **n\_mobs** (*int*) – The number of mobjects that emerge from the focal point, by default 5.
        * **initial\_opacity** (*float*) – The starting stroke opacity of the mobjects emitted from the broadcast, by default 1.
        * **final\_opacity** (*float*) – The final stroke opacity of the mobjects emitted from the broadcast, by default 0.
        * **initial\_width** (*float*) – The initial width of the mobjects, by default 0.0.
        * **remover** (*bool*) – Whether the mobjects should be removed from the scene after the animation, by default True.
        * **lag\_ratio** (*float*) – The time between each iteration of the mobject, by default 0.2.
        * **run\_time** (*float*) – The total duration of the animation, by default 3.
        * **kwargs** (*Any*) – Additional arguments to be passed to [`LaggedStart`](manim.animation.composition.LaggedStart.html#manim.animation.composition.LaggedStart "manim.animation.composition.LaggedStart").

    Examples

    Example: BroadcastExample [¶](#broadcastexample)

    [
    ](./BroadcastExample-1.mp4)

    ```
    from manim import *

    class BroadcastExample(Scene):
        def construct(self):
            mob = Circle(radius=4, color=TEAL_A)
            self.play(Broadcast(mob))

    ```

    ```

    class BroadcastExample(Scene):
        def construct(self):
            mob = Circle(radius=4, color=TEAL_A)
            self.play(Broadcast(mob))


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *focal\_point=array([0., 0., 0.])*, *n\_mobs=5*, *initial\_opacity=1*, *final\_opacity=0*, *initial\_width=0.0*, *remover=True*, *lag\_ratio=0.2*, *run\_time=3*, *\*\*kwargs*)[¶](#manim.animation.specialized.Broadcast._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **focal\_point** (*Sequence**[**float**]*)
            * **n\_mobs** (*int*)
            * **initial\_opacity** (*float*)
            * **final\_opacity** (*float*)
            * **initial\_width** (*float*)
            * **remover** (*bool*)
            * **lag\_ratio** (*float*)
            * **run\_time** (*float*)
            * **kwargs** (*Any*)