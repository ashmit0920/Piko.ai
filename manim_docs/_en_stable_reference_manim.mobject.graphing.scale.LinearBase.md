# Source: https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LinearBase.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

LinearBase[¶](#linearbase "Link to this heading")
=================================================

Qualified name: `manim.mobject.graphing.scale.LinearBase`

*class* LinearBase(*scale\_factor=1.0*)[[source]](../_modules/manim/mobject/graphing/scale.html#LinearBase)[¶](#manim.mobject.graphing.scale.LinearBase "Link to this definition")
:   Bases: `_ScaleBase`

    The default scaling class.

    Parameters:
    :   **scale\_factor** (*float*) – The slope of the linear function, by default 1.0

    Methods

    |  |  |
    | --- | --- |
    | [`function`](#manim.mobject.graphing.scale.LinearBase.function "manim.mobject.graphing.scale.LinearBase.function") | Multiplies the value by the scale factor. |
    | [`inverse_function`](#manim.mobject.graphing.scale.LinearBase.inverse_function "manim.mobject.graphing.scale.LinearBase.inverse_function") | Inverse of function. |

    function(*value*)[[source]](../_modules/manim/mobject/graphing/scale.html#LinearBase.function)[¶](#manim.mobject.graphing.scale.LinearBase.function "Link to this definition")
    :   Multiplies the value by the scale factor.

        Parameters:
        :   **value** (*float*) – Value to be multiplied by the scale factor.

        Return type:
        :   float

    inverse\_function(*value*)[[source]](../_modules/manim/mobject/graphing/scale.html#LinearBase.inverse_function)[¶](#manim.mobject.graphing.scale.LinearBase.inverse_function "Link to this definition")
    :   Inverse of function. Divides the value by the scale factor.

        Parameters:
        :   **value** (*float*) – value to be divided by the scale factor.

        Return type:
        :   float