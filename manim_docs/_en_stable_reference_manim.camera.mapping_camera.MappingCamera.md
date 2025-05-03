# Source: https://docs.manim.community/en/stable/reference/manim.camera.mapping_camera.MappingCamera.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

MappingCamera[¶](#mappingcamera "Link to this heading")
=======================================================

Qualified name: `manim.camera.mapping\_camera.MappingCamera`

*class* MappingCamera(*mapping\_func=<function MappingCamera.<lambda>>*, *min\_num\_curves=50*, *allow\_object\_intrusion=False*, *\*\*kwargs*)[[source]](../_modules/manim/camera/mapping_camera.html#MappingCamera)[¶](#manim.camera.mapping_camera.MappingCamera "Link to this definition")
:   Bases: [`Camera`](manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera")

    Camera object that allows mapping
    between objects.

    Methods

    |  |  |
    | --- | --- |
    | [`capture_mobjects`](#manim.camera.mapping_camera.MappingCamera.capture_mobjects "manim.camera.mapping_camera.MappingCamera.capture_mobjects") | Capture mobjects by printing them on `pixel_array`. |
    | `points_to_pixel_coords` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `background_color` |  |
    | `background_opacity` |  |

    capture\_mobjects(*mobjects*, *\*\*kwargs*)[[source]](../_modules/manim/camera/mapping_camera.html#MappingCamera.capture_mobjects)[¶](#manim.camera.mapping_camera.MappingCamera.capture_mobjects "Link to this definition")
    :   Capture mobjects by printing them on `pixel_array`.

        This is the essential function that converts the contents of a Scene
        into an array, which is then converted to an image or video.

        Parameters:
        :   * **mobjects** – Mobjects to capture.
            * **kwargs** – Keyword arguments to be passed to `get_mobjects_to_display()`.

        Notes

        For a list of classes that can currently be rendered, see `display_funcs()`.