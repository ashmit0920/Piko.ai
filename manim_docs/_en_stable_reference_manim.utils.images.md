# Source: https://docs.manim.community/en/stable/reference/manim.utils.images.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

images[¶](#module-manim.utils.images "Link to this heading")
============================================================

Image manipulation utilities.

Functions

change\_to\_rgba\_array(*image*, *dtype='uint8'*)[[source]](../_modules/manim/utils/images.html#change_to_rgba_array)[¶](#manim.utils.images.change_to_rgba_array "Link to this definition")
:   Converts an RGB array into RGBA with the alpha value opacity maxed.

    Parameters:
    :   * **image** ([*RGBPixelArray*](manim.typing.html#manim.typing.RGBPixelArray "manim.typing.RGBPixelArray"))
        * **dtype** (*str*)

    Return type:
    :   [*RGBPixelArray*](manim.typing.html#manim.typing.RGBPixelArray "manim.typing.RGBPixelArray")

drag\_pixels(*frames*)[[source]](../_modules/manim/utils/images.html#drag_pixels)[¶](#manim.utils.images.drag_pixels "Link to this definition")
:   Parameters:
    :   **frames** (*list**[**array**]*)

    Return type:
    :   list[*array*]

get\_full\_raster\_image\_path(*image\_file\_name*)[[source]](../_modules/manim/utils/images.html#get_full_raster_image_path)[¶](#manim.utils.images.get_full_raster_image_path "Link to this definition")
:   Parameters:
    :   **image\_file\_name** (*str* *|* *PurePath*)

    Return type:
    :   *Path*

get\_full\_vector\_image\_path(*image\_file\_name*)[[source]](../_modules/manim/utils/images.html#get_full_vector_image_path)[¶](#manim.utils.images.get_full_vector_image_path "Link to this definition")
:   Parameters:
    :   **image\_file\_name** (*str* *|* *PurePath*)

    Return type:
    :   *Path*

invert\_image(*image*)[[source]](../_modules/manim/utils/images.html#invert_image)[¶](#manim.utils.images.invert_image "Link to this definition")
:   Parameters:
    :   **image** (*array*)

    Return type:
    :   <module ‘PIL.Image’ from ‘/home/docs/checkouts/readthedocs.org/user\_builds/manimce/envs/stable/lib/python3.13/site-packages/PIL/Image.py’>