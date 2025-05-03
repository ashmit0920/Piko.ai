# Source: https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ChangingDecimal[¶](#changingdecimal "Link to this heading")
===========================================================

Qualified name: `manim.animation.numbers.ChangingDecimal`

*class* ChangingDecimal(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/numbers.html#ChangingDecimal)[¶](#manim.animation.numbers.ChangingDecimal "Link to this definition")
:   Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    Methods

    |  |  |
    | --- | --- |
    | `check_validity_of_input` |  |
    | [`interpolate_mobject`](#manim.animation.numbers.ChangingDecimal.interpolate_mobject "manim.animation.numbers.ChangingDecimal.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   * **decimal\_mob** ([*DecimalNumber*](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber"))
        * **number\_update\_func** (*Callable**[**[**float**]**,* *float**]*)
        * **suspend\_mobject\_updating** (*bool* *|* *None*)

    \_original\_\_init\_\_(*decimal\_mob*, *number\_update\_func*, *suspend\_mobject\_updating=False*, *\*\*kwargs*)[¶](#manim.animation.numbers.ChangingDecimal._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **decimal\_mob** ([*DecimalNumber*](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber"))
            * **number\_update\_func** (*Callable**[**[**float**]**,* *float**]*)
            * **suspend\_mobject\_updating** (*bool* *|* *None*)

        Return type:
        :   None

    interpolate\_mobject(*alpha*)[[source]](../_modules/manim/animation/numbers.html#ChangingDecimal.interpolate_mobject)[¶](#manim.animation.numbers.ChangingDecimal.interpolate_mobject "Link to this definition")
    :   Interpolates the mobject of the `Animation` based on alpha value.

        Parameters:
        :   **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
            is completed. For example, alpha-values of 0, 0.5, and 1 correspond
            to the animation being completed 0%, 50%, and 100%, respectively.

        Return type:
        :   None