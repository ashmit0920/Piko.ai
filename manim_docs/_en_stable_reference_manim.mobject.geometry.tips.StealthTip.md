# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

StealthTip[¶](#stealthtip "Link to this heading")
=================================================

Qualified name: `manim.mobject.geometry.tips.StealthTip`

*class* StealthTip(*fill\_opacity=1*, *stroke\_width=3*, *length=0.175*, *start\_angle=3.141592653589793*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/tips.html#StealthTip)[¶](#manim.mobject.geometry.tips.StealthTip "Link to this definition")
:   Bases: [`ArrowTip`](manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip "manim.mobject.geometry.tips.ArrowTip")

    ‘Stealth’ fighter / kite arrow shape.

    Naming is inspired by the corresponding
    [TikZ arrow shape](https://tikz.dev/tikz-arrows#sec-16.3).

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `base` | The base point of the arrow tip. |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | [`length`](#manim.mobject.geometry.tips.StealthTip.length "manim.mobject.geometry.tips.StealthTip.length") | The length of the arrow tip. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `tip_angle` | The angle of the arrow tip. |
    | `tip_point` | The tip point of the arrow tip. |
    | `vector` | The vector pointing from the base point to the tip point. |
    | `width` | The width of the mobject. |

    Parameters:
    :   * **fill\_opacity** (*float*)
        * **stroke\_width** (*float*)
        * **length** (*float*)
        * **start\_angle** (*float*)
        * **kwargs** (*Any*)

    \_original\_\_init\_\_(*fill\_opacity=1*, *stroke\_width=3*, *length=0.175*, *start\_angle=3.141592653589793*, *\*\*kwargs*)[¶](#manim.mobject.geometry.tips.StealthTip._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **fill\_opacity** (*float*)
            * **stroke\_width** (*float*)
            * **length** (*float*)
            * **start\_angle** (*float*)
            * **kwargs** (*Any*)

    *property* length*: float*[¶](#manim.mobject.geometry.tips.StealthTip.length "Link to this definition")
    :   The length of the arrow tip.

        In this case, the length is computed as the height of
        the triangle encompassing the stealth tip (otherwise,
        the tip is scaled too large).