# Source: https://docs.manim.community/en/stable/reference/manim.camera.mapping_camera.OldMultiCamera.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

OldMultiCamera[¶](#oldmulticamera "Link to this heading")
=========================================================

Qualified name: `manim.camera.mapping\_camera.OldMultiCamera`

*class* OldMultiCamera(*\*cameras\_with\_start\_positions*, *\*\*kwargs*)[[source]](../_modules/manim/camera/mapping_camera.html#OldMultiCamera)[¶](#manim.camera.mapping_camera.OldMultiCamera "Link to this definition")
:   Bases: [`Camera`](manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera")

    Methods

    |  |  |
    | --- | --- |
    | [`capture_mobjects`](#manim.camera.mapping_camera.OldMultiCamera.capture_mobjects "manim.camera.mapping_camera.OldMultiCamera.capture_mobjects") | Capture mobjects by printing them on `pixel_array`. |
    | [`init_background`](#manim.camera.mapping_camera.OldMultiCamera.init_background "manim.camera.mapping_camera.OldMultiCamera.init_background") | Initialize the background. |
    | [`set_background`](#manim.camera.mapping_camera.OldMultiCamera.set_background "manim.camera.mapping_camera.OldMultiCamera.set_background") | Sets the background to the passed pixel\_array after converting to valid RGB values. |
    | [`set_pixel_array`](#manim.camera.mapping_camera.OldMultiCamera.set_pixel_array "manim.camera.mapping_camera.OldMultiCamera.set_pixel_array") | Sets the pixel array of the camera to the passed pixel array. |

    Attributes

    |  |  |
    | --- | --- |
    | `background_color` |  |
    | `background_opacity` |  |

    capture\_mobjects(*mobjects*, *\*\*kwargs*)[[source]](../_modules/manim/camera/mapping_camera.html#OldMultiCamera.capture_mobjects)[¶](#manim.camera.mapping_camera.OldMultiCamera.capture_mobjects "Link to this definition")
    :   Capture mobjects by printing them on `pixel_array`.

        This is the essential function that converts the contents of a Scene
        into an array, which is then converted to an image or video.

        Parameters:
        :   * **mobjects** – Mobjects to capture.
            * **kwargs** – Keyword arguments to be passed to `get_mobjects_to_display()`.

        Notes

        For a list of classes that can currently be rendered, see `display_funcs()`.

    init\_background()[[source]](../_modules/manim/camera/mapping_camera.html#OldMultiCamera.init_background)[¶](#manim.camera.mapping_camera.OldMultiCamera.init_background "Link to this definition")
    :   Initialize the background.
        If self.background\_image is the path of an image
        the image is set as background; else, the default
        background color fills the background.

    set\_background(*pixel\_array*, *\*\*kwargs*)[[source]](../_modules/manim/camera/mapping_camera.html#OldMultiCamera.set_background)[¶](#manim.camera.mapping_camera.OldMultiCamera.set_background "Link to this definition")
    :   Sets the background to the passed pixel\_array after converting
        to valid RGB values.

        Parameters:
        :   * **pixel\_array** – The pixel array to set the background to.
            * **convert\_from\_floats** – Whether or not to convert floats values to proper RGB valid ones, by default False

    set\_pixel\_array(*pixel\_array*, *\*\*kwargs*)[[source]](../_modules/manim/camera/mapping_camera.html#OldMultiCamera.set_pixel_array)[¶](#manim.camera.mapping_camera.OldMultiCamera.set_pixel_array "Link to this definition")
    :   Sets the pixel array of the camera to the passed pixel array.

        Parameters:
        :   * **pixel\_array** – The pixel array to convert and then set as the camera’s pixel array.
            * **convert\_from\_floats** – Whether or not to convert float values to proper RGB values, by default False