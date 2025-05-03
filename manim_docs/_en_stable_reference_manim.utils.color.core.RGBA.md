# Source: https://docs.manim.community/en/stable/reference/manim.utils.color.core.RGBA.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

RGBA[¶](#rgba "Link to this heading")
=====================================

Qualified name: `manim.utils.color.core.RGBA`

RGBA[¶](#manim.utils.color.core.RGBA "Link to this definition")
:   RGBA Color Space

    Methods

    |  |  |
    | --- | --- |
    | `contrasting` | Return one of two colors, light or dark (by default white or black), that contrasts with the current color (depending on its luminance). |
    | `darker` | Return a new color that is darker than the current color, i.e. interpolated with `BLACK`. |
    | `from_hex` | Create a [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") from a hex string. |
    | `from_hsl` | Create a [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") from an HSL array. |
    | `from_hsv` | Create a [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") from an HSV array. |
    | `from_rgb` | Create a ManimColor from an RGB array. |
    | `from_rgba` | Create a ManimColor from an RGBA Array. |
    | `gradient` | This method is currently not implemented. |
    | `interpolate` | Interpolate between the current and the given [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"), and return the result. |
    | `into` | Convert the current color into a different colorspace given by `class_type`, without changing the `_internal_value`. |
    | `invert` | Return a new, linearly inverted version of this [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") (no inplace changes). |
    | `lighter` | Return a new color that is lighter than the current color, i.e. interpolated with `WHITE`. |
    | `opacity` | Create a new [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") with the given opacity and the same color values as before. |
    | `parse` | Parse one color as a [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") or a sequence of colors as a list of [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")'s. |
    | `to_hex` | Convert the [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") to a hexadecimal representation of the color. |
    | `to_hsl` | Convert the [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") to an HSL array. |
    | `to_hsv` | Convert the [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") to an HSV array. |
    | `to_int_rgb` | Convert the current [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGB array of integers. |
    | `to_int_rgba` | Convert the current ManimColor into an RGBA array of integers. |
    | `to_int_rgba_with_alpha` | Convert the current [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGBA array of integers. |
    | `to_integer` | Convert the current [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an integer. |
    | `to_rgb` | Convert the current [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGB array of floats. |
    | `to_rgba` | Convert the current [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGBA array of floats. |
    | `to_rgba_with_alpha` | Convert the current [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGBA array of floats. |