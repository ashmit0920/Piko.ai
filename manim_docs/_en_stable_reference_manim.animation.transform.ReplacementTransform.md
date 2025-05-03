# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform.ReplacementTransform.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ReplacementTransform[¶](#replacementtransform "Link to this heading")
=====================================================================

Qualified name: `manim.animation.transform.ReplacementTransform`

*class* ReplacementTransform(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform.html#ReplacementTransform)[¶](#manim.animation.transform.ReplacementTransform "Link to this definition")
:   Bases: [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

    Replaces and morphs a mobject into a target mobject.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The starting [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
        * **target\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The target [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
        * **kwargs** – Further keyword arguments that are passed to [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform").

    Examples

    Example: ReplacementTransformOrTransform [¶](#replacementtransformortransform)

    [
    ](./ReplacementTransformOrTransform-1.mp4)

    ```
    from manim import *

    class ReplacementTransformOrTransform(Scene):
        def construct(self):
            # set up the numbers
            r_transform = VGroup(*[Integer(i) for i in range(1,4)])
            text_1 = Text("ReplacementTransform", color=RED)
            r_transform.add(text_1)

            transform = VGroup(*[Integer(i) for i in range(4,7)])
            text_2 = Text("Transform", color=BLUE)
            transform.add(text_2)

            ints = VGroup(r_transform, transform)
            texts = VGroup(text_1, text_2).scale(0.75)
            r_transform.arrange(direction=UP, buff=1)
            transform.arrange(direction=UP, buff=1)

            ints.arrange(buff=2)
            self.add(ints, texts)

            # The mobs replace each other and none are left behind
            self.play(ReplacementTransform(r_transform[0], r_transform[1]))
            self.play(ReplacementTransform(r_transform[1], r_transform[2]))

            # The mobs linger after the Transform()
            self.play(Transform(transform[0], transform[1]))
            self.play(Transform(transform[1], transform[2]))
            self.wait()

    ```

    ```

    class ReplacementTransformOrTransform(Scene):
        def construct(self):
            # set up the numbers
            r_transform = VGroup(*[Integer(i) for i in range(1,4)])
            text_1 = Text("ReplacementTransform", color=RED)
            r_transform.add(text_1)

            transform = VGroup(*[Integer(i) for i in range(4,7)])
            text_2 = Text("Transform", color=BLUE)
            transform.add(text_2)

            ints = VGroup(r_transform, transform)
            texts = VGroup(text_1, text_2).scale(0.75)
            r_transform.arrange(direction=UP, buff=1)
            transform.arrange(direction=UP, buff=1)

            ints.arrange(buff=2)
            self.add(ints, texts)

            # The mobs replace each other and none are left behind
            self.play(ReplacementTransform(r_transform[0], r_transform[1]))
            self.play(ReplacementTransform(r_transform[1], r_transform[2]))

            # The mobs linger after the Transform()
            self.play(Transform(transform[0], transform[1]))
            self.play(Transform(transform[1], transform[2]))
            self.wait()


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *target\_mobject*, *\*\*kwargs*)[¶](#manim.animation.transform.ReplacementTransform._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **target\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

        Return type:
        :   None