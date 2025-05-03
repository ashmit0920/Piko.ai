# Source: https://docs.manim.community/en/stable/reference/manim.camera.camera.BackgroundColoredVMobjectDisplayer.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

BackgroundColoredVMobjectDisplayer[¶](#backgroundcoloredvmobjectdisplayer "Link to this heading")
=================================================================================================

Qualified name: `manim.camera.camera.BackgroundColoredVMobjectDisplayer`

*class* BackgroundColoredVMobjectDisplayer(*camera*)[[source]](../_modules/manim/camera/camera.html#BackgroundColoredVMobjectDisplayer)[¶](#manim.camera.camera.BackgroundColoredVMobjectDisplayer "Link to this definition")
:   Bases: `object`

    Auxiliary class that handles displaying vectorized mobjects with
    a set background image.

    Parameters:
    :   **camera** ([*Camera*](manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera")) – Camera object to use.

    Methods

    |  |  |
    | --- | --- |
    | [`display`](#manim.camera.camera.BackgroundColoredVMobjectDisplayer.display "manim.camera.camera.BackgroundColoredVMobjectDisplayer.display") | Displays the colored VMobjects. |
    | [`get_background_array`](#manim.camera.camera.BackgroundColoredVMobjectDisplayer.get_background_array "manim.camera.camera.BackgroundColoredVMobjectDisplayer.get_background_array") | Gets the background array that has the passed file\_name. |
    | `reset_pixel_array` |  |
    | [`resize_background_array`](#manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array "manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array") | Resizes the pixel array representing the background. |
    | [`resize_background_array_to_match`](#manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array_to_match "manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array_to_match") | Resizes the background array to match the passed pixel array. |

    display(*\*cvmobjects*)[[source]](../_modules/manim/camera/camera.html#BackgroundColoredVMobjectDisplayer.display)[¶](#manim.camera.camera.BackgroundColoredVMobjectDisplayer.display "Link to this definition")
    :   Displays the colored VMobjects.

        Parameters:
        :   **\*cvmobjects** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The VMobjects

        Returns:
        :   The pixel array with the cvmobjects displayed.

        Return type:
        :   np.array

    get\_background\_array(*image*)[[source]](../_modules/manim/camera/camera.html#BackgroundColoredVMobjectDisplayer.get_background_array)[¶](#manim.camera.camera.BackgroundColoredVMobjectDisplayer.get_background_array "Link to this definition")
    :   Gets the background array that has the passed file\_name.

        Parameters:
        :   **image** (*Image* *|* *Path* *|* *str*) – The background image or its file name.

        Returns:
        :   The pixel array of the image.

        Return type:
        :   np.ndarray

    resize\_background\_array(*background\_array*, *new\_width*, *new\_height*, *mode='RGBA'*)[[source]](../_modules/manim/camera/camera.html#BackgroundColoredVMobjectDisplayer.resize_background_array)[¶](#manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array "Link to this definition")
    :   Resizes the pixel array representing the background.

        Parameters:
        :   * **background\_array** (*ndarray*) – The pixel
            * **new\_width** (*float*) – The new width of the background
            * **new\_height** (*float*) – The new height of the background
            * **mode** (*str*) – The PIL image mode, by default “RGBA”

        Returns:
        :   The numpy pixel array of the resized background.

        Return type:
        :   np.array

    resize\_background\_array\_to\_match(*background\_array*, *pixel\_array*)[[source]](../_modules/manim/camera/camera.html#BackgroundColoredVMobjectDisplayer.resize_background_array_to_match)[¶](#manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array_to_match "Link to this definition")
    :   Resizes the background array to match the passed pixel array.

        Parameters:
        :   * **background\_array** (*ndarray*) – The prospective pixel array.
            * **pixel\_array** (*ndarray*) – The pixel array whose width and height should be matched.

        Returns:
        :   The resized background array.

        Return type:
        :   np.array