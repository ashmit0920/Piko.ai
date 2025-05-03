# Source: https://docs.manim.community/en/stable/reference/manim.utils.color.core.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

core[¶](#module-manim.utils.color.core "Link to this heading")
==============================================================

Manim’s (internal) color data structure and some utilities for color conversion.

This module contains the implementation of [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"), the data structure
internally used to represent colors.

The preferred way of using these colors is by importing their constants from Manim:

```
>>> from manim import RED, GREEN, BLUE
>>> print(RED)
#FC6255

```

Note that this way uses the name of the colors in UPPERCASE.

Note

The colors with a `_C` suffix have an alias equal to the colorname without a
letter. For example, `GREEN = GREEN_C`.

Custom Color Spaces[¶](#custom-color-spaces "Link to this heading")
-------------------------------------------------------------------

Hello, dear visitor. You seem to be interested in implementing a custom color class for
a color space we don’t currently support.

The current system is using a few indirections for ensuring a consistent behavior with
all other color types in Manim.

To implement a custom color space, you must subclass [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") and implement
three important methods:

> * [`_internal_value`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor._internal_value "manim.utils.color.core.ManimColor._internal_value"): a `@property` implemented on
>   [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") with the goal of keeping a consistent internal representation
>   which can be referenced by other functions in [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"). This property acts
>   as a proxy to whatever representation you need in your class.
>
>   > + The getter should always return a NumPy array in the format `[r,g,b,a]`, in
>   >   accordance with the type `ManimColorInternal`.
>   > + The setter should always accept a value in the format `[r,g,b,a]` which can be
>   >   converted to whatever attributes you need.
> * [`_internal_space`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor._internal_space "manim.utils.color.core.ManimColor._internal_space"): a read-only `@property` implemented on
>   [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") with the goal of providing a useful representation which can be
>   used by operators, interpolation and color transform functions.
>
>   The only constraints on this value are:
>
>   > + It must be a NumPy array.
>   > + The last value must be the opacity in a range `0.0` to `1.0`.
>
>   Additionally, your `__init__` must support this format as an initialization value
>   without additional parameters to ensure correct functionality of all other methods in
>   [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").
> * [`_from_internal()`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor._from_internal "manim.utils.color.core.ManimColor._from_internal"): a `@classmethod` which converts an
>   `[r,g,b,a]` value into suitable parameters for your `__init__` method and calls
>   the `cls` parameter.

Type Aliases

*class* ParsableManimColor[¶](#manim.utils.color.core.ParsableManimColor "Link to this definition")
:   ```
    ManimColor | int | str | RGB_Tuple_Int | RGB_Tuple_Float | RGBA_Tuple_Int | RGBA_Tuple_Float | RGB_Array_Int | RGB_Array_Float | RGBA_Array_Int | RGBA_Array_Float
    ```

    [`ParsableManimColor`](#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") represents all the types which can be parsed
    to a [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") in Manim.

TypeVar’s

*class* ManimColorT[¶](#manim.utils.color.core.ManimColorT "Link to this definition")
:   ```
    TypeVar('ManimColorT', bound=ManimColor)

    ```

Classes

|  |  |
| --- | --- |
| [`HSV`](manim.utils.color.core.HSV.html#manim.utils.color.core.HSV "manim.utils.color.core.HSV") | HSV Color Space |
| [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") | Internal representation of a color. |
| [`RGBA`](manim.utils.color.core.RGBA.html#manim.utils.color.core.RGBA "manim.utils.color.core.RGBA") | RGBA Color Space |

Functions

average\_color(*\*colors*)[[source]](../_modules/manim/utils/color/core.html#average_color)[¶](#manim.utils.color.core.average_color "Link to this definition")
:   Determine the average color between the given parameters.

    Note

    This operation does not consider the alphas (opacities) of the colors. The
    generated color has an alpha or opacity of 1.0.

    Returns:
    :   The average color of the input.

    Return type:
    :   [ManimColor](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

    Parameters:
    :   **colors** ([*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

color\_gradient(*reference\_colors*, *length\_of\_output*)[[source]](../_modules/manim/utils/color/core.html#color_gradient)[¶](#manim.utils.color.core.color_gradient "Link to this definition")
:   Create a list of colors interpolated between the input array of colors with a
    specific number of colors.

    Parameters:
    :   * **reference\_colors** (*Sequence**[*[*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")*]*) – The colors to be interpolated between or spread apart.
        * **length\_of\_output** (*int*) – The number of colors that the output should have, ideally more than the input.

    Returns:
    :   A [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") or a list of interpolated [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")’s.

    Return type:
    :   list[[ManimColor](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")] | [ManimColor](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

color\_to\_int\_rgb(*color*)[[source]](../_modules/manim/utils/color/core.html#color_to_int_rgb)[¶](#manim.utils.color.core.color_to_int_rgb "Link to this definition")
:   Helper function for use in functional style programming. Refer to
    [`ManimColor.to_int_rgb()`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_int_rgb "manim.utils.color.core.ManimColor.to_int_rgb").

    Parameters:
    :   **color** ([*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – A color to convert to an RGB integer array.

    Returns:
    :   The corresponding RGB integer array.

    Return type:
    :   [RGB\_Array\_Int](manim.typing.html#manim.typing.RGB_Array_Int "manim.typing.RGB_Array_Int")

color\_to\_int\_rgba(*color*, *alpha=1.0*)[[source]](../_modules/manim/utils/color/core.html#color_to_int_rgba)[¶](#manim.utils.color.core.color_to_int_rgba "Link to this definition")
:   Helper function for use in functional style programming. Refer to
    [`ManimColor.to_int_rgba_with_alpha()`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_int_rgba_with_alpha "manim.utils.color.core.ManimColor.to_int_rgba_with_alpha").

    Parameters:
    :   * **color** ([*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – A color to convert to an RGBA integer array.
        * **alpha** (*float*) – An alpha value between 0.0 and 1.0 to be used as opacity in the color. Default is
          1.0.

    Returns:
    :   The corresponding RGBA integer array.

    Return type:
    :   [RGBA\_Array\_Int](manim.typing.html#manim.typing.RGBA_Array_Int "manim.typing.RGBA_Array_Int")

color\_to\_rgb(*color*)[[source]](../_modules/manim/utils/color/core.html#color_to_rgb)[¶](#manim.utils.color.core.color_to_rgb "Link to this definition")
:   Helper function for use in functional style programming.
    Refer to [`ManimColor.to_rgb()`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_rgb "manim.utils.color.core.ManimColor.to_rgb").

    Parameters:
    :   **color** ([*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – A color to convert to an RGB float array.

    Returns:
    :   The corresponding RGB float array.

    Return type:
    :   [RGB\_Array\_Float](manim.typing.html#manim.typing.RGB_Array_Float "manim.typing.RGB_Array_Float")

color\_to\_rgba(*color*, *alpha=1.0*)[[source]](../_modules/manim/utils/color/core.html#color_to_rgba)[¶](#manim.utils.color.core.color_to_rgba "Link to this definition")
:   Helper function for use in functional style programming. Refer to
    [`ManimColor.to_rgba_with_alpha()`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_rgba_with_alpha "manim.utils.color.core.ManimColor.to_rgba_with_alpha").

    Parameters:
    :   * **color** ([*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – A color to convert to an RGBA float array.
        * **alpha** (*float*) – An alpha value between 0.0 and 1.0 to be used as opacity in the color. Default is
          1.0.

    Returns:
    :   The corresponding RGBA float array.

    Return type:
    :   [RGBA\_Array\_Float](manim.typing.html#manim.typing.RGBA_Array_Float "manim.typing.RGBA_Array_Float")

get\_shaded\_rgb(*rgb*, *point*, *unit\_normal\_vect*, *light\_source*)[[source]](../_modules/manim/utils/color/core.html#get_shaded_rgb)[¶](#manim.utils.color.core.get_shaded_rgb "Link to this definition")
:   Add light or shadow to the `rgb` color of some surface which is located at a
    given `point` in space and facing in the direction of `unit_normal_vect`,
    depending on whether the surface is facing a `light_source` or away from it.

    Parameters:
    :   * **rgb** ([*RGB\_Array\_Float*](manim.typing.html#manim.typing.RGB_Array_Float "manim.typing.RGB_Array_Float")) – An RGB array of floats.
        * **point** ([*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")) – The location of the colored surface.
        * **unit\_normal\_vect** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The direction in which the colored surface is facing.
        * **light\_source** ([*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")) – The location of a light source which might illuminate the surface.

    Returns:
    :   The color with added light or shadow, depending on the direction of the colored
        surface.

    Return type:
    :   [RGB\_Array\_Float](manim.typing.html#manim.typing.RGB_Array_Float "manim.typing.RGB_Array_Float")

hex\_to\_rgb(*hex\_code*)[[source]](../_modules/manim/utils/color/core.html#hex_to_rgb)[¶](#manim.utils.color.core.hex_to_rgb "Link to this definition")
:   Helper function for use in functional style programming. Refer to
    [`ManimColor.to_rgb()`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_rgb "manim.utils.color.core.ManimColor.to_rgb").

    Parameters:
    :   **hex\_code** (*str*) – A hex string representing a color.

    Returns:
    :   An RGB array representing the color.

    Return type:
    :   [RGB\_Array\_Float](manim.typing.html#manim.typing.RGB_Array_Float "manim.typing.RGB_Array_Float")

interpolate\_color(*color1*, *color2*, *alpha*)[[source]](../_modules/manim/utils/color/core.html#interpolate_color)[¶](#manim.utils.color.core.interpolate_color "Link to this definition")
:   Standalone function to interpolate two ManimColors and get the result. Refer to
    [`ManimColor.interpolate()`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.interpolate "manim.utils.color.core.ManimColor.interpolate").

    Parameters:
    :   * **color1** ([*ManimColorT*](#manim.utils.color.core.ManimColorT "manim.utils.color.core.ManimColorT")) – The first [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").
        * **color2** ([*ManimColorT*](#manim.utils.color.core.ManimColorT "manim.utils.color.core.ManimColorT")) – The second [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").
        * **alpha** (*float*) – The alpha value determining the point of interpolation between the colors.

    Returns:
    :   The interpolated ManimColor.

    Return type:
    :   [ManimColor](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

invert\_color(*color*)[[source]](../_modules/manim/utils/color/core.html#invert_color)[¶](#manim.utils.color.core.invert_color "Link to this definition")
:   Helper function for use in functional style programming. Refer to
    [`ManimColor.invert()`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.invert "manim.utils.color.core.ManimColor.invert")

    Parameters:
    :   **color** ([*ManimColorT*](#manim.utils.color.core.ManimColorT "manim.utils.color.core.ManimColorT")) – The [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") to invert.

    Returns:
    :   The linearly inverted [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

    Return type:
    :   [ManimColor](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

random\_bright\_color()[[source]](../_modules/manim/utils/color/core.html#random_bright_color)[¶](#manim.utils.color.core.random_bright_color "Link to this definition")
:   Return a random bright color: a random color averaged with `WHITE`.

    Warning

    This operation is very expensive. Please keep in mind the performance loss.

    Returns:
    :   A random bright [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

    Return type:
    :   [ManimColor](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

random\_color()[[source]](../_modules/manim/utils/color/core.html#random_color)[¶](#manim.utils.color.core.random_color "Link to this definition")
:   Return a random [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

    Warning

    This operation is very expensive. Please keep in mind the performance loss.

    Returns:
    :   A random [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

    Return type:
    :   [ManimColor](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

rgb\_to\_color(*rgb*)[[source]](../_modules/manim/utils/color/core.html#rgb_to_color)[¶](#manim.utils.color.core.rgb_to_color "Link to this definition")
:   Helper function for use in functional style programming. Refer to
    [`ManimColor.from_rgb()`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.from_rgb "manim.utils.color.core.ManimColor.from_rgb").

    Parameters:
    :   **rgb** ([*RGB\_Array\_Float*](manim.typing.html#manim.typing.RGB_Array_Float "manim.typing.RGB_Array_Float") *|* [*RGB\_Tuple\_Float*](manim.typing.html#manim.typing.RGB_Tuple_Float "manim.typing.RGB_Tuple_Float") *|* [*RGB\_Array\_Int*](manim.typing.html#manim.typing.RGB_Array_Int "manim.typing.RGB_Array_Int") *|* [*RGB\_Tuple\_Int*](manim.typing.html#manim.typing.RGB_Tuple_Int "manim.typing.RGB_Tuple_Int")) – A 3 element iterable.

    Returns:
    :   A ManimColor with the corresponding value.

    Return type:
    :   [ManimColor](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

rgb\_to\_hex(*rgb*)[[source]](../_modules/manim/utils/color/core.html#rgb_to_hex)[¶](#manim.utils.color.core.rgb_to_hex "Link to this definition")
:   Helper function for use in functional style programming. Refer to
    [`ManimColor.from_rgb()`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.from_rgb "manim.utils.color.core.ManimColor.from_rgb") and [`ManimColor.to_hex()`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_hex "manim.utils.color.core.ManimColor.to_hex").

    Parameters:
    :   **rgb** ([*RGB\_Array\_Float*](manim.typing.html#manim.typing.RGB_Array_Float "manim.typing.RGB_Array_Float") *|* [*RGB\_Tuple\_Float*](manim.typing.html#manim.typing.RGB_Tuple_Float "manim.typing.RGB_Tuple_Float") *|* [*RGB\_Array\_Int*](manim.typing.html#manim.typing.RGB_Array_Int "manim.typing.RGB_Array_Int") *|* [*RGB\_Tuple\_Int*](manim.typing.html#manim.typing.RGB_Tuple_Int "manim.typing.RGB_Tuple_Int")) – A 3 element iterable.

    Returns:
    :   A hex representation of the color.

    Return type:
    :   str

rgba\_to\_color(*rgba*)[[source]](../_modules/manim/utils/color/core.html#rgba_to_color)[¶](#manim.utils.color.core.rgba_to_color "Link to this definition")
:   Helper function for use in functional style programming. Refer to
    [`ManimColor.from_rgba()`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.from_rgba "manim.utils.color.core.ManimColor.from_rgba").

    Parameters:
    :   **rgba** ([*RGBA\_Array\_Float*](manim.typing.html#manim.typing.RGBA_Array_Float "manim.typing.RGBA_Array_Float") *|* [*RGBA\_Tuple\_Float*](manim.typing.html#manim.typing.RGBA_Tuple_Float "manim.typing.RGBA_Tuple_Float") *|* [*RGBA\_Array\_Int*](manim.typing.html#manim.typing.RGBA_Array_Int "manim.typing.RGBA_Array_Int") *|* [*RGBA\_Tuple\_Int*](manim.typing.html#manim.typing.RGBA_Tuple_Int "manim.typing.RGBA_Tuple_Int")) – A 4 element iterable.

    Returns:
    :   A ManimColor with the corresponding value

    Return type:
    :   [ManimColor](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")