# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform.CyclicReplace.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

CyclicReplace[¶](#cyclicreplace "Link to this heading")
=======================================================

Qualified name: `manim.animation.transform.CyclicReplace`

*class* CyclicReplace(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform.html#CyclicReplace)[¶](#manim.animation.transform.CyclicReplace "Link to this definition")
:   Bases: [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

    An animation moving mobjects cyclically.

    In particular, this means: the first mobject takes the place
    of the second mobject, the second one takes the place of
    the third mobject, and so on. The last mobject takes the
    place of the first one.

    Parameters:
    :   * **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – List of mobjects to be transformed.
        * **path\_arc** (*float*) – The angle of the arc (in radians) that the mobjects will follow to reach
          their target.
        * **kwargs** – Further keyword arguments that are passed to [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform").

    Examples

    Example: CyclicReplaceExample [¶](#cyclicreplaceexample)

    [
    ](./CyclicReplaceExample-1.mp4)

    ```
    from manim import *

    class CyclicReplaceExample(Scene):
        def construct(self):
            group = VGroup(Square(), Circle(), Triangle(), Star())
            group.arrange(RIGHT)
            self.add(group)

            for _ in range(4):
                self.play(CyclicReplace(*group))

    ```

    ```

    class CyclicReplaceExample(Scene):
        def construct(self):
            group = VGroup(Square(), Circle(), Triangle(), Star())
            group.arrange(RIGHT)
            self.add(group)

            for _ in range(4):
                self.play(CyclicReplace(*group))


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

    \_original\_\_init\_\_(*\*mobjects*, *path\_arc=1.5707963267948966*, *\*\*kwargs*)[¶](#manim.animation.transform.CyclicReplace._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **path\_arc** (*float*)

        Return type:
        :   None