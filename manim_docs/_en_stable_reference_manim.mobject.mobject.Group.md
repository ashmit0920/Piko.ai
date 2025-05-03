# Source: https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Group.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Group[¶](#group "Link to this heading")
=======================================

Qualified name: `manim.mobject.mobject.Group`

*class* Group(*\*mobjects*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/mobject.html#Group)[¶](#manim.mobject.mobject.Group "Link to this definition")
:   Bases: [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

    Groups together multiple [`Mobjects`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

    Notes

    When adding the same mobject more than once, repetitions are ignored.
    Use [`Mobject.copy()`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.copy "manim.mobject.mobject.Mobject.copy") to create a separate copy which can then
    be added to the group.

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `depth` | The depth of the mobject. |
    | `height` | The height of the mobject. |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*\*mobjects*, *\*\*kwargs*)[¶](#manim.mobject.mobject.Group._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Return type:
        :   None