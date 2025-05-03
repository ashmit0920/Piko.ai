# Source: https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ShowPassingFlash[¶](#showpassingflash "Link to this heading")
=============================================================

Qualified name: `manim.animation.indication.ShowPassingFlash`

*class* ShowPassingFlash(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/indication.html#ShowPassingFlash)[¶](#manim.animation.indication.ShowPassingFlash "Link to this definition")
:   Bases: [`ShowPartial`](manim.animation.creation.ShowPartial.html#manim.animation.creation.ShowPartial "manim.animation.creation.ShowPartial")

    Show only a sliver of the VMobject each frame.

    Parameters:
    :   * **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The mobject whose stroke is animated.
        * **time\_width** (*float*) – The length of the sliver relative to the length of the stroke.

    Examples

    Example: TimeWidthValues [¶](#timewidthvalues)

    [
    ](./TimeWidthValues-1.mp4)

    ```
    from manim import *

    class TimeWidthValues(Scene):
        def construct(self):
            p = RegularPolygon(5, color=DARK_GRAY, stroke_width=6).scale(3)
            lbl = VMobject()
            self.add(p, lbl)
            p = p.copy().set_color(BLUE)
            for time_width in [0.2, 0.5, 1, 2]:
                lbl.become(Tex(r"\texttt{time\_width={{%.1f}}}"%time_width))
                self.play(ShowPassingFlash(
                    p.copy().set_color(BLUE),
                    run_time=2,
                    time_width=time_width
                ))

    ```

    ```

    class TimeWidthValues(Scene):
        def construct(self):
            p = RegularPolygon(5, color=DARK_GRAY, stroke_width=6).scale(3)
            lbl = VMobject()
            self.add(p, lbl)
            p = p.copy().set_color(BLUE)
            for time_width in [0.2, 0.5, 1, 2]:
                lbl.become(Tex(r"\texttt{time\_width={{%.1f}}}"%time_width))
                self.play(ShowPassingFlash(
                    p.copy().set_color(BLUE),
                    run_time=2,
                    time_width=time_width
                ))


    ```

    See also

    [`Create`](manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create")

    Methods

    |  |  |
    | --- | --- |
    | [`clean_up_from_scene`](#manim.animation.indication.ShowPassingFlash.clean_up_from_scene "manim.animation.indication.ShowPassingFlash.clean_up_from_scene") | Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *time\_width=0.1*, *\*\*kwargs*)[¶](#manim.animation.indication.ShowPassingFlash._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))
            * **time\_width** (*float*)

        Return type:
        :   None

    clean\_up\_from\_scene(*scene*)[[source]](../_modules/manim/animation/indication.html#ShowPassingFlash.clean_up_from_scene)[¶](#manim.animation.indication.ShowPassingFlash.clean_up_from_scene "Link to this definition")
    :   Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.

        This includes to [`remove()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
        [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.

        Parameters:
        :   **scene** ([*Scene*](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.

        Return type:
        :   None