# Source: https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

HSV[¶](#hsv "Link to this heading")
===================================

Qualified name: `manim.utils.color.core.HSV`

*class* HSV(*hsv*, *alpha=1.0*)[[source]](../_modules/manim/utils/color/core.html#HSV)[¶](#manim.utils.color.core.HSV "Link to this definition")
:   Bases: [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

    HSV Color Space

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `h` |  |
    | `hue` |  |
    | `s` |  |
    | `saturation` |  |
    | `v` |  |
    | `value` |  |

    Parameters:
    :   * **hsv** ([*HSV\_Array\_Float*](manim.typing.html#manim.typing.HSV_Array_Float "manim.typing.HSV_Array_Float") *|* [*HSV\_Tuple\_Float*](manim.typing.html#manim.typing.HSV_Tuple_Float "manim.typing.HSV_Tuple_Float") *|* [*HSVA\_Array\_Float*](manim.typing.html#manim.typing.HSVA_Array_Float "manim.typing.HSVA_Array_Float") *|* [*HSVA\_Tuple\_Float*](manim.typing.html#manim.typing.HSVA_Tuple_Float "manim.typing.HSVA_Tuple_Float"))
        * **alpha** (*float*)

    *classmethod* \_from\_internal(*value*)[[source]](../_modules/manim/utils/color/core.html#HSV._from_internal)[¶](#manim.utils.color.core.HSV._from_internal "Link to this definition")
    :   This method is intended to be overwritten by custom color space classes
        which are subtypes of [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

        The method constructs a new object of the given class by transforming the value
        in the internal format `[r,g,b,a]` into a format which the constructor of the
        custom class can understand. Look at [`HSV`](#manim.utils.color.core.HSV "manim.utils.color.core.HSV") for an example.

        Parameters:
        :   **value** ([*ManimColorInternal*](manim.typing.html#manim.typing.ManimColorInternal "manim.typing.ManimColorInternal"))

        Return type:
        :   *Self*

    *property* \_internal\_space*: ndarray[tuple[int, ...], dtype[\_ScalarType\_co]]*[¶](#manim.utils.color.core.HSV._internal_space "Link to this definition")
    :   This is a readonly property which is a custom representation for color space
        operations. It is used for operators and can be used when implementing a custom
        color space.

    *property* \_internal\_value*: [ManimColorInternal](manim.typing.html#manim.typing.ManimColorInternal "manim.typing.ManimColorInternal")*[¶](#manim.utils.color.core.HSV._internal_value "Link to this definition")
    :   Return the internal value of the current [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") as an
        `[r,g,b,a]` float array.

        Returns:
        :   Internal color representation.

        Return type:
        :   [ManimColorInternal](manim.typing.html#manim.typing.ManimColorInternal "manim.typing.ManimColorInternal")