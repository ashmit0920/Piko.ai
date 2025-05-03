# Source: https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotate.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Rotate[¶](#rotate "Link to this heading")
=========================================

Qualified name: `manim.animation.rotation.Rotate`

*class* Rotate(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/rotation.html#Rotate)[¶](#manim.animation.rotation.Rotate "Link to this definition")
:   Bases: [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

    Animation that rotates a Mobject.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to be rotated.
        * **angle** (*float*) – The rotation angle.
        * **axis** (*np.ndarray*) – The rotation axis as a numpy vector.
        * **about\_point** (*Sequence**[**float**]* *|* *None*) – The rotation center.
        * **about\_edge** (*Sequence**[**float**]* *|* *None*) – If `about_point` is `None`, this argument specifies
          the direction of the bounding box point to be taken as
          the rotation center.

    Examples

    Example: UsingRotate [¶](#usingrotate)

    [
    ](./UsingRotate-1.mp4)

    ```
    from manim import *

    class UsingRotate(Scene):
        def construct(self):
            self.play(
                Rotate(
                    Square(side_length=0.5).shift(UP * 2),
                    angle=2*PI,
                    about_point=ORIGIN,
                    rate_func=linear,
                ),
                Rotate(Square(side_length=0.5), angle=2*PI, rate_func=linear),
                )

    ```

    ```

    class UsingRotate(Scene):
        def construct(self):
            self.play(
                Rotate(
                    Square(side_length=0.5).shift(UP * 2),
                    angle=2*PI,
                    about_point=ORIGIN,
                    rate_func=linear,
                ),
                Rotate(Square(side_length=0.5), angle=2*PI, rate_func=linear),
                )


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

    \_original\_\_init\_\_(*mobject*, *angle=3.141592653589793*, *axis=array([0., 0., 1.])*, *about\_point=None*, *about\_edge=None*, *\*\*kwargs*)[¶](#manim.animation.rotation.Rotate._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **angle** (*float*)
            * **axis** (*np.ndarray*)
            * **about\_point** (*Sequence**[**float**]* *|* *None*)
            * **about\_edge** (*Sequence**[**float**]* *|* *None*)

        Return type:
        :   None