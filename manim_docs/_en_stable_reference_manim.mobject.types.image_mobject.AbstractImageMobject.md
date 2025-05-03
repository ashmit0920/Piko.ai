# Source: https://docs.manim.community/en/stable/reference/manim.mobject.types.image_mobject.AbstractImageMobject.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

AbstractImageMobject[¶](#abstractimagemobject "Link to this heading")
=====================================================================

Qualified name: `manim.mobject.types.image\_mobject.AbstractImageMobject`

*class* AbstractImageMobject(*scale\_to\_resolution*, *pixel\_array\_dtype='uint8'*, *resampling\_algorithm=Resampling.BICUBIC*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/types/image_mobject.html#AbstractImageMobject)[¶](#manim.mobject.types.image_mobject.AbstractImageMobject "Link to this definition")
:   Bases: [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

    Automatically filters out black pixels

    Parameters:
    :   * **scale\_to\_resolution** (*int*) – At this resolution the image is placed pixel by pixel onto the screen, so it
          will look the sharpest and best.
          This is a custom parameter of ImageMobject so that rendering a scene with
          e.g. the `--quality low` or `--quality medium` flag for faster rendering
          won’t effect the position of the image on the screen.
        * **pixel\_array\_dtype** (*str*)
        * **resampling\_algorithm** (*Resampling*)
        * **kwargs** (*Any*)

    Methods

    |  |  |
    | --- | --- |
    | `get_pixel_array` |  |
    | [`reset_points`](#manim.mobject.types.image_mobject.AbstractImageMobject.reset_points "manim.mobject.types.image_mobject.AbstractImageMobject.reset_points") | Sets `points` to be the four image corners. |
    | [`set_color`](#manim.mobject.types.image_mobject.AbstractImageMobject.set_color "manim.mobject.types.image_mobject.AbstractImageMobject.set_color") | Condition is function which takes in one arguments, (x, y, z). |
    | [`set_resampling_algorithm`](#manim.mobject.types.image_mobject.AbstractImageMobject.set_resampling_algorithm "manim.mobject.types.image_mobject.AbstractImageMobject.set_resampling_algorithm") | Sets the interpolation method for upscaling the image. |

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `depth` | The depth of the mobject. |
    | `height` | The height of the mobject. |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*scale\_to\_resolution*, *pixel\_array\_dtype='uint8'*, *resampling\_algorithm=Resampling.BICUBIC*, *\*\*kwargs*)[¶](#manim.mobject.types.image_mobject.AbstractImageMobject._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **scale\_to\_resolution** (*int*)
            * **pixel\_array\_dtype** (*str*)
            * **resampling\_algorithm** (*Resampling*)
            * **kwargs** (*Any*)

        Return type:
        :   None

    reset\_points()[[source]](../_modules/manim/mobject/types/image_mobject.html#AbstractImageMobject.reset_points)[¶](#manim.mobject.types.image_mobject.AbstractImageMobject.reset_points "Link to this definition")
    :   Sets `points` to be the four image corners.

        Return type:
        :   None

    set\_color(*color*, *alpha=None*, *family=True*)[[source]](../_modules/manim/mobject/types/image_mobject.html#AbstractImageMobject.set_color)[¶](#manim.mobject.types.image_mobject.AbstractImageMobject.set_color "Link to this definition")
    :   Condition is function which takes in one arguments, (x, y, z).
        Here it just recurses to submobjects, but in subclasses this
        should be further implemented based on the the inner workings
        of color

    set\_resampling\_algorithm(*resampling\_algorithm*)[[source]](../_modules/manim/mobject/types/image_mobject.html#AbstractImageMobject.set_resampling_algorithm)[¶](#manim.mobject.types.image_mobject.AbstractImageMobject.set_resampling_algorithm "Link to this definition")
    :   Sets the interpolation method for upscaling the image. By default the image is
        interpolated using bicubic algorithm. This method lets you change it.
        Interpolation is done internally using Pillow, and the function besides the
        string constants describing the algorithm accepts the Pillow integer constants.

        Parameters:
        :   **resampling\_algorithm** (*int*) –

            An integer constant described in the Pillow library,
            or one from the RESAMPLING\_ALGORITHMS global dictionary,
            under the following keys:

            * ’bicubic’ or ‘cubic’
            * ’nearest’ or ‘none’
            * ’box’
            * ’bilinear’ or ‘linear’
            * ’hamming’
            * ’lanczos’ or ‘antialias’

        Return type:
        :   Self