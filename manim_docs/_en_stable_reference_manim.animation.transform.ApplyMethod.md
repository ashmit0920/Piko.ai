# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ApplyMethod[¶](#applymethod "Link to this heading")
===================================================

Qualified name: `manim.animation.transform.ApplyMethod`

*class* ApplyMethod(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform.html#ApplyMethod)[¶](#manim.animation.transform.ApplyMethod "Link to this definition")
:   Bases: [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

    Animates a mobject by applying a method.

    Note that only the method needs to be passed to this animation,
    it is not required to pass the corresponding mobject. Furthermore,
    this animation class only works if the method returns the modified
    mobject.

    Parameters:
    :   * **method** (*Callable*) – The method that will be applied in the animation.
        * **args** – Any positional arguments to be passed when applying the method.
        * **kwargs** – Any keyword arguments passed to [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform").

    Methods

    |  |  |
    | --- | --- |
    | `check_validity_of_input` |  |
    | `create_target` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*method*, *\*args*, *\*\*kwargs*)[¶](#manim.animation.transform.ApplyMethod._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   **method** (*Callable*)

        Return type:
        :   None