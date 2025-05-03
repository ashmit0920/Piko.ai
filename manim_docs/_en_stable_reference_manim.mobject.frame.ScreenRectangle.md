# Source: https://docs.manim.community/en/stable/reference/manim.mobject.frame.ScreenRectangle.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ScreenRectangle[¶](#screenrectangle "Link to this heading")
===========================================================

Qualified name: `manim.mobject.frame.ScreenRectangle`

*class* ScreenRectangle(*aspect\_ratio=1.7777777777777777*, *height=4*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/frame.html#ScreenRectangle)[¶](#manim.mobject.frame.ScreenRectangle "Link to this definition")
:   Bases: [`Rectangle`](manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle")

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | [`aspect_ratio`](#manim.mobject.frame.ScreenRectangle.aspect_ratio "manim.mobject.frame.ScreenRectangle.aspect_ratio") | The aspect ratio. |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*aspect\_ratio=1.7777777777777777*, *height=4*, *\*\*kwargs*)[¶](#manim.mobject.frame.ScreenRectangle._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

    *property* aspect\_ratio[¶](#manim.mobject.frame.ScreenRectangle.aspect_ratio "Link to this definition")
    :   The aspect ratio.

        When set, the width is stretched to accommodate
        the new aspect ratio.