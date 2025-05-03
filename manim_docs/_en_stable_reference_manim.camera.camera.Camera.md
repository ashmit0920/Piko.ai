# Source: https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Camera[¶](#camera "Link to this heading")
=========================================

Qualified name: `manim.camera.camera.Camera`

*class* Camera(*background\_image=None*, *frame\_center=array([0., 0., 0.])*, *image\_mode='RGBA'*, *n\_channels=4*, *pixel\_array\_dtype='uint8'*, *cairo\_line\_width\_multiple=0.01*, *use\_z\_index=True*, *background=None*, *pixel\_height=None*, *pixel\_width=None*, *frame\_height=None*, *frame\_width=None*, *frame\_rate=None*, *background\_color=None*, *background\_opacity=None*, *\*\*kwargs*)[[source]](../_modules/manim/camera/camera.html#Camera)[¶](#manim.camera.camera.Camera "Link to this definition")
:   Bases: `object`

    Base camera class.

    This is the object which takes care of what exactly is displayed
    on screen at any given moment.

    Parameters:
    :   * **background\_image** (*str* *|* *None*) – The path to an image that should be the background image.
          If not set, the background is filled with `self.background_color`
        * **background** (*np.ndarray* *|* *None*) – What `background` is set to. By default, `None`.
        * **pixel\_height** (*int* *|* *None*) – The height of the scene in pixels.
        * **pixel\_width** (*int* *|* *None*) – The width of the scene in pixels.
        * **kwargs** – Additional arguments (`background_color`, `background_opacity`)
          to be set.
        * **frame\_center** (*np.ndarray*)
        * **image\_mode** (*str*)
        * **n\_channels** (*int*)
        * **pixel\_array\_dtype** (*str*)
        * **cairo\_line\_width\_multiple** (*float*)
        * **use\_z\_index** (*bool*)
        * **frame\_height** (*float* *|* *None*)
        * **frame\_width** (*float* *|* *None*)
        * **frame\_rate** (*float* *|* *None*)
        * **background\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *|* *None*)
        * **background\_opacity** (*float* *|* *None*)

    Methods

    |  |  |
    | --- | --- |
    | [`adjust_out_of_range_points`](#manim.camera.camera.Camera.adjust_out_of_range_points "manim.camera.camera.Camera.adjust_out_of_range_points") | If any of the points in the passed array are out of the viable range, they are adjusted suitably. |
    | [`adjusted_thickness`](#manim.camera.camera.Camera.adjusted_thickness "manim.camera.camera.Camera.adjusted_thickness") | Computes the adjusted stroke width for a zoomed camera. |
    | [`apply_fill`](#manim.camera.camera.Camera.apply_fill "manim.camera.camera.Camera.apply_fill") | Fills the cairo context |
    | [`apply_stroke`](#manim.camera.camera.Camera.apply_stroke "manim.camera.camera.Camera.apply_stroke") | Applies a stroke to the VMobject in the cairo context. |
    | [`cache_cairo_context`](#manim.camera.camera.Camera.cache_cairo_context "manim.camera.camera.Camera.cache_cairo_context") | Caches the passed Pixel array into a Cairo Context |
    | [`capture_mobject`](#manim.camera.camera.Camera.capture_mobject "manim.camera.camera.Camera.capture_mobject") | Capture mobjects by storing it in `pixel_array`. |
    | [`capture_mobjects`](#manim.camera.camera.Camera.capture_mobjects "manim.camera.camera.Camera.capture_mobjects") | Capture mobjects by printing them on `pixel_array`. |
    | [`convert_pixel_array`](#manim.camera.camera.Camera.convert_pixel_array "manim.camera.camera.Camera.convert_pixel_array") | Converts a pixel array from values that have floats in then to proper RGB values. |
    | [`display_image_mobject`](#manim.camera.camera.Camera.display_image_mobject "manim.camera.camera.Camera.display_image_mobject") | Displays an ImageMobject by changing the pixel\_array suitably. |
    | [`display_multiple_background_colored_vmobjects`](#manim.camera.camera.Camera.display_multiple_background_colored_vmobjects "manim.camera.camera.Camera.display_multiple_background_colored_vmobjects") | Displays multiple vmobjects that have the same color as the background. |
    | [`display_multiple_image_mobjects`](#manim.camera.camera.Camera.display_multiple_image_mobjects "manim.camera.camera.Camera.display_multiple_image_mobjects") | Displays multiple image mobjects by modifying the passed pixel\_array. |
    | [`display_multiple_non_background_colored_vmobjects`](#manim.camera.camera.Camera.display_multiple_non_background_colored_vmobjects "manim.camera.camera.Camera.display_multiple_non_background_colored_vmobjects") | Displays multiple VMobjects in the cairo context, as long as they don't have background colors. |
    | [`display_multiple_point_cloud_mobjects`](#manim.camera.camera.Camera.display_multiple_point_cloud_mobjects "manim.camera.camera.Camera.display_multiple_point_cloud_mobjects") | Displays multiple PMobjects by modifying the passed pixel array. |
    | [`display_multiple_vectorized_mobjects`](#manim.camera.camera.Camera.display_multiple_vectorized_mobjects "manim.camera.camera.Camera.display_multiple_vectorized_mobjects") | Displays multiple VMobjects in the pixel\_array |
    | [`display_point_cloud`](#manim.camera.camera.Camera.display_point_cloud "manim.camera.camera.Camera.display_point_cloud") | Displays a PMobject by modifying the pixel array suitably. |
    | [`display_vectorized`](#manim.camera.camera.Camera.display_vectorized "manim.camera.camera.Camera.display_vectorized") | Displays a VMobject in the cairo context |
    | [`get_background_colored_vmobject_displayer`](#manim.camera.camera.Camera.get_background_colored_vmobject_displayer "manim.camera.camera.Camera.get_background_colored_vmobject_displayer") | Returns the background\_colored\_vmobject\_displayer if it exists or makes one and returns it if not. |
    | [`get_cached_cairo_context`](#manim.camera.camera.Camera.get_cached_cairo_context "manim.camera.camera.Camera.get_cached_cairo_context") | Returns the cached cairo context of the passed pixel array if it exists, and None if it doesn't. |
    | [`get_cairo_context`](#manim.camera.camera.Camera.get_cairo_context "manim.camera.camera.Camera.get_cairo_context") | Returns the cairo context for a pixel array after caching it to self.pixel\_array\_to\_cairo\_context If that array has already been cached, it returns the cached version instead. |
    | [`get_coords_of_all_pixels`](#manim.camera.camera.Camera.get_coords_of_all_pixels "manim.camera.camera.Camera.get_coords_of_all_pixels") | Returns the cartesian coordinates of each pixel. |
    | [`get_fill_rgbas`](#manim.camera.camera.Camera.get_fill_rgbas "manim.camera.camera.Camera.get_fill_rgbas") | Returns the RGBA array of the fill of the passed VMobject |
    | [`get_image`](#manim.camera.camera.Camera.get_image "manim.camera.camera.Camera.get_image") | Returns an image from the passed pixel array, or from the current frame if the passed pixel array is none. |
    | [`get_mobjects_to_display`](#manim.camera.camera.Camera.get_mobjects_to_display "manim.camera.camera.Camera.get_mobjects_to_display") | Used to get the list of mobjects to display with the camera. |
    | [`get_stroke_rgbas`](#manim.camera.camera.Camera.get_stroke_rgbas "manim.camera.camera.Camera.get_stroke_rgbas") | Gets the RGBA array for the stroke of the passed VMobject. |
    | [`get_thickening_nudges`](#manim.camera.camera.Camera.get_thickening_nudges "manim.camera.camera.Camera.get_thickening_nudges") | Determine a list of vectors used to nudge two-dimensional pixel coordinates. |
    | [`init_background`](#manim.camera.camera.Camera.init_background "manim.camera.camera.Camera.init_background") | Initialize the background. |
    | [`is_in_frame`](#manim.camera.camera.Camera.is_in_frame "manim.camera.camera.Camera.is_in_frame") | Checks whether the passed mobject is in frame or not. |
    | [`make_background_from_func`](#manim.camera.camera.Camera.make_background_from_func "manim.camera.camera.Camera.make_background_from_func") | Makes a pixel array for the background by using coords\_to\_colors\_func to determine each pixel's color. |
    | [`on_screen_pixels`](#manim.camera.camera.Camera.on_screen_pixels "manim.camera.camera.Camera.on_screen_pixels") | Returns array of pixels that are on the screen from a given array of pixel\_coordinates |
    | [`overlay_PIL_image`](#manim.camera.camera.Camera.overlay_PIL_image "manim.camera.camera.Camera.overlay_PIL_image") | Overlays a PIL image on the passed pixel array. |
    | [`overlay_rgba_array`](#manim.camera.camera.Camera.overlay_rgba_array "manim.camera.camera.Camera.overlay_rgba_array") | Overlays an RGBA array on top of the given Pixel array. |
    | `points_to_pixel_coords` |  |
    | [`reset`](#manim.camera.camera.Camera.reset "manim.camera.camera.Camera.reset") | Resets the camera's pixel array to that of the background |
    | [`reset_pixel_shape`](#manim.camera.camera.Camera.reset_pixel_shape "manim.camera.camera.Camera.reset_pixel_shape") | This method resets the height and width of a single pixel to the passed new\_height and new\_width. |
    | [`resize_frame_shape`](#manim.camera.camera.Camera.resize_frame_shape "manim.camera.camera.Camera.resize_frame_shape") | Changes frame\_shape to match the aspect ratio of the pixels, where fixed\_dimension determines whether frame\_height or frame\_width remains fixed while the other changes accordingly. |
    | [`set_background`](#manim.camera.camera.Camera.set_background "manim.camera.camera.Camera.set_background") | Sets the background to the passed pixel\_array after converting to valid RGB values. |
    | [`set_background_from_func`](#manim.camera.camera.Camera.set_background_from_func "manim.camera.camera.Camera.set_background_from_func") | Sets the background to a pixel array using coords\_to\_colors\_func to determine each pixel's color. |
    | [`set_cairo_context_color`](#manim.camera.camera.Camera.set_cairo_context_color "manim.camera.camera.Camera.set_cairo_context_color") | Sets the color of the cairo context |
    | [`set_cairo_context_path`](#manim.camera.camera.Camera.set_cairo_context_path "manim.camera.camera.Camera.set_cairo_context_path") | Sets a path for the cairo context with the vmobject passed |
    | `set_frame_to_background` |  |
    | [`set_pixel_array`](#manim.camera.camera.Camera.set_pixel_array "manim.camera.camera.Camera.set_pixel_array") | Sets the pixel array of the camera to the passed pixel array. |
    | [`thickened_coordinates`](#manim.camera.camera.Camera.thickened_coordinates "manim.camera.camera.Camera.thickened_coordinates") | Returns thickened coordinates for a passed array of pixel coords and a thickness to thicken by. |
    | `transform_points_pre_display` |  |
    | [`type_or_raise`](#manim.camera.camera.Camera.type_or_raise "manim.camera.camera.Camera.type_or_raise") | Return the type of mobject, if it is a type that can be rendered. |

    Attributes

    |  |  |
    | --- | --- |
    | `background_color` |  |
    | `background_opacity` |  |

    adjust\_out\_of\_range\_points(*points*)[[source]](../_modules/manim/camera/camera.html#Camera.adjust_out_of_range_points)[¶](#manim.camera.camera.Camera.adjust_out_of_range_points "Link to this definition")
    :   If any of the points in the passed array are out of
        the viable range, they are adjusted suitably.

        Parameters:
        :   **points** (*ndarray*) – The points to adjust

        Returns:
        :   The adjusted points.

        Return type:
        :   np.array

    adjusted\_thickness(*thickness*)[[source]](../_modules/manim/camera/camera.html#Camera.adjusted_thickness)[¶](#manim.camera.camera.Camera.adjusted_thickness "Link to this definition")
    :   Computes the adjusted stroke width for a zoomed camera.

        Parameters:
        :   **thickness** (*float*) – The stroke width of a mobject.

        Returns:
        :   The adjusted stroke width that reflects zooming in with
            the camera.

        Return type:
        :   float

    apply\_fill(*ctx*, *vmobject*)[[source]](../_modules/manim/camera/camera.html#Camera.apply_fill)[¶](#manim.camera.camera.Camera.apply_fill "Link to this definition")
    :   Fills the cairo context

        Parameters:
        :   * **ctx** (*Context*) – The cairo context
            * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The VMobject

        Returns:
        :   The camera object.

        Return type:
        :   [Camera](#manim.camera.camera.Camera "manim.camera.camera.Camera")

    apply\_stroke(*ctx*, *vmobject*, *background=False*)[[source]](../_modules/manim/camera/camera.html#Camera.apply_stroke)[¶](#manim.camera.camera.Camera.apply_stroke "Link to this definition")
    :   Applies a stroke to the VMobject in the cairo context.

        Parameters:
        :   * **ctx** (*Context*) – The cairo context
            * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The VMobject
            * **background** (*bool*) – Whether or not to consider the background when applying this
              stroke width, by default False

        Returns:
        :   The camera object with the stroke applied.

        Return type:
        :   [Camera](#manim.camera.camera.Camera "manim.camera.camera.Camera")

    cache\_cairo\_context(*pixel\_array*, *ctx*)[[source]](../_modules/manim/camera/camera.html#Camera.cache_cairo_context)[¶](#manim.camera.camera.Camera.cache_cairo_context "Link to this definition")
    :   Caches the passed Pixel array into a Cairo Context

        Parameters:
        :   * **pixel\_array** (*ndarray*) – The pixel array to cache
            * **ctx** (*Context*) – The context to cache it into.

    capture\_mobject(*mobject*, *\*\*kwargs*)[[source]](../_modules/manim/camera/camera.html#Camera.capture_mobject)[¶](#manim.camera.camera.Camera.capture_mobject "Link to this definition")
    :   Capture mobjects by storing it in `pixel_array`.

        This is a single-mobject version of [`capture_mobjects()`](#manim.camera.camera.Camera.capture_mobjects "manim.camera.camera.Camera.capture_mobjects").

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – Mobject to capture.
            * **kwargs** (*Any*) – Keyword arguments to be passed to [`get_mobjects_to_display()`](#manim.camera.camera.Camera.get_mobjects_to_display "manim.camera.camera.Camera.get_mobjects_to_display").

    capture\_mobjects(*mobjects*, *\*\*kwargs*)[[source]](../_modules/manim/camera/camera.html#Camera.capture_mobjects)[¶](#manim.camera.camera.Camera.capture_mobjects "Link to this definition")
    :   Capture mobjects by printing them on `pixel_array`.

        This is the essential function that converts the contents of a Scene
        into an array, which is then converted to an image or video.

        Parameters:
        :   * **mobjects** (*Iterable**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – Mobjects to capture.
            * **kwargs** – Keyword arguments to be passed to [`get_mobjects_to_display()`](#manim.camera.camera.Camera.get_mobjects_to_display "manim.camera.camera.Camera.get_mobjects_to_display").

        Notes

        For a list of classes that can currently be rendered, see `display_funcs()`.

    convert\_pixel\_array(*pixel\_array*, *convert\_from\_floats=False*)[[source]](../_modules/manim/camera/camera.html#Camera.convert_pixel_array)[¶](#manim.camera.camera.Camera.convert_pixel_array "Link to this definition")
    :   Converts a pixel array from values that have floats in then
        to proper RGB values.

        Parameters:
        :   * **pixel\_array** (*ndarray* *|* *list* *|* *tuple*) – Pixel array to convert.
            * **convert\_from\_floats** (*bool*) – Whether or not to convert float values to ints, by default False

        Returns:
        :   The new, converted pixel array.

        Return type:
        :   np.array

    display\_image\_mobject(*image\_mobject*, *pixel\_array*)[[source]](../_modules/manim/camera/camera.html#Camera.display_image_mobject)[¶](#manim.camera.camera.Camera.display_image_mobject "Link to this definition")
    :   Displays an ImageMobject by changing the pixel\_array suitably.

        Parameters:
        :   * **image\_mobject** ([*AbstractImageMobject*](manim.mobject.types.image_mobject.AbstractImageMobject.html#manim.mobject.types.image_mobject.AbstractImageMobject "manim.mobject.types.image_mobject.AbstractImageMobject")) – The imageMobject to display
            * **pixel\_array** (*ndarray*) – The Pixel array to put the imagemobject in.

    display\_multiple\_background\_colored\_vmobjects(*cvmobjects*, *pixel\_array*)[[source]](../_modules/manim/camera/camera.html#Camera.display_multiple_background_colored_vmobjects)[¶](#manim.camera.camera.Camera.display_multiple_background_colored_vmobjects "Link to this definition")
    :   Displays multiple vmobjects that have the same color as the background.

        Parameters:
        :   * **cvmobjects** (*list*) – List of Colored VMobjects
            * **pixel\_array** (*ndarray*) – The pixel array.

        Returns:
        :   The camera object.

        Return type:
        :   [Camera](#manim.camera.camera.Camera "manim.camera.camera.Camera")

    display\_multiple\_image\_mobjects(*image\_mobjects*, *pixel\_array*)[[source]](../_modules/manim/camera/camera.html#Camera.display_multiple_image_mobjects)[¶](#manim.camera.camera.Camera.display_multiple_image_mobjects "Link to this definition")
    :   Displays multiple image mobjects by modifying the passed pixel\_array.

        Parameters:
        :   * **image\_mobjects** (*list*) – list of ImageMobjects
            * **pixel\_array** (*ndarray*) – The pixel array to modify.

    display\_multiple\_non\_background\_colored\_vmobjects(*vmobjects*, *pixel\_array*)[[source]](../_modules/manim/camera/camera.html#Camera.display_multiple_non_background_colored_vmobjects)[¶](#manim.camera.camera.Camera.display_multiple_non_background_colored_vmobjects "Link to this definition")
    :   Displays multiple VMobjects in the cairo context, as long as they don’t have
        background colors.

        Parameters:
        :   * **vmobjects** (*list*) – list of the VMobjects
            * **pixel\_array** (*ndarray*) – The Pixel array to add the VMobjects to.

    display\_multiple\_point\_cloud\_mobjects(*pmobjects*, *pixel\_array*)[[source]](../_modules/manim/camera/camera.html#Camera.display_multiple_point_cloud_mobjects)[¶](#manim.camera.camera.Camera.display_multiple_point_cloud_mobjects "Link to this definition")
    :   Displays multiple PMobjects by modifying the passed pixel array.

        Parameters:
        :   * **pmobjects** (*list*) – List of PMobjects
            * **pixel\_array** (*ndarray*) – The pixel array to modify.

    display\_multiple\_vectorized\_mobjects(*vmobjects*, *pixel\_array*)[[source]](../_modules/manim/camera/camera.html#Camera.display_multiple_vectorized_mobjects)[¶](#manim.camera.camera.Camera.display_multiple_vectorized_mobjects "Link to this definition")
    :   Displays multiple VMobjects in the pixel\_array

        Parameters:
        :   * **vmobjects** (*list*) – list of VMobjects to display
            * **pixel\_array** (*ndarray*) – The pixel array

    display\_point\_cloud(*pmobject*, *points*, *rgbas*, *thickness*, *pixel\_array*)[[source]](../_modules/manim/camera/camera.html#Camera.display_point_cloud)[¶](#manim.camera.camera.Camera.display_point_cloud "Link to this definition")
    :   Displays a PMobject by modifying the pixel array suitably.

        TODO: Write a description for the rgbas argument.

        Parameters:
        :   * **pmobject** ([*PMobject*](manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject "manim.mobject.types.point_cloud_mobject.PMobject")) – Point Cloud Mobject
            * **points** (*list*) – The points to display in the point cloud mobject
            * **rgbas** (*ndarray*)
            * **thickness** (*float*) – The thickness of each point of the PMobject
            * **pixel\_array** (*ndarray*) – The pixel array to modify.

    display\_vectorized(*vmobject*, *ctx*)[[source]](../_modules/manim/camera/camera.html#Camera.display_vectorized)[¶](#manim.camera.camera.Camera.display_vectorized "Link to this definition")
    :   Displays a VMobject in the cairo context

        Parameters:
        :   * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The Vectorized Mobject to display
            * **ctx** (*Context*) – The cairo context to use.

        Returns:
        :   The camera object

        Return type:
        :   [Camera](#manim.camera.camera.Camera "manim.camera.camera.Camera")

    get\_background\_colored\_vmobject\_displayer()[[source]](../_modules/manim/camera/camera.html#Camera.get_background_colored_vmobject_displayer)[¶](#manim.camera.camera.Camera.get_background_colored_vmobject_displayer "Link to this definition")
    :   Returns the background\_colored\_vmobject\_displayer
        if it exists or makes one and returns it if not.

        Returns:
        :   Object that displays VMobjects that have the same color
            as the background.

        Return type:
        :   BackGroundColoredVMobjectDisplayer

    get\_cached\_cairo\_context(*pixel\_array*)[[source]](../_modules/manim/camera/camera.html#Camera.get_cached_cairo_context)[¶](#manim.camera.camera.Camera.get_cached_cairo_context "Link to this definition")
    :   Returns the cached cairo context of the passed
        pixel array if it exists, and None if it doesn’t.

        Parameters:
        :   **pixel\_array** (*ndarray*) – The pixel array to check.

        Returns:
        :   The cached cairo context.

        Return type:
        :   cairo.Context

    get\_cairo\_context(*pixel\_array*)[[source]](../_modules/manim/camera/camera.html#Camera.get_cairo_context)[¶](#manim.camera.camera.Camera.get_cairo_context "Link to this definition")
    :   Returns the cairo context for a pixel array after
        caching it to self.pixel\_array\_to\_cairo\_context
        If that array has already been cached, it returns the
        cached version instead.

        Parameters:
        :   **pixel\_array** (*ndarray*) – The Pixel array to get the cairo context of.

        Returns:
        :   The cairo context of the pixel array.

        Return type:
        :   cairo.Context

    get\_coords\_of\_all\_pixels()[[source]](../_modules/manim/camera/camera.html#Camera.get_coords_of_all_pixels)[¶](#manim.camera.camera.Camera.get_coords_of_all_pixels "Link to this definition")
    :   Returns the cartesian coordinates of each pixel.

        Returns:
        :   The array of cartesian coordinates.

        Return type:
        :   np.ndarray

    get\_fill\_rgbas(*vmobject*)[[source]](../_modules/manim/camera/camera.html#Camera.get_fill_rgbas)[¶](#manim.camera.camera.Camera.get_fill_rgbas "Link to this definition")
    :   Returns the RGBA array of the fill of the passed VMobject

        Parameters:
        :   **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The VMobject

        Returns:
        :   The RGBA Array of the fill of the VMobject

        Return type:
        :   np.array

    get\_image(*pixel\_array=None*)[[source]](../_modules/manim/camera/camera.html#Camera.get_image)[¶](#manim.camera.camera.Camera.get_image "Link to this definition")
    :   Returns an image from the passed
        pixel array, or from the current frame
        if the passed pixel array is none.

        Parameters:
        :   **pixel\_array** (*ndarray* *|* *list* *|* *tuple* *|* *None*) – The pixel array from which to get an image, by default None

        Returns:
        :   The PIL image of the array.

        Return type:
        :   PIL.Image

    get\_mobjects\_to\_display(*mobjects*, *include\_submobjects=True*, *excluded\_mobjects=None*)[[source]](../_modules/manim/camera/camera.html#Camera.get_mobjects_to_display)[¶](#manim.camera.camera.Camera.get_mobjects_to_display "Link to this definition")
    :   Used to get the list of mobjects to display
        with the camera.

        Parameters:
        :   * **mobjects** (*Iterable**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The Mobjects
            * **include\_submobjects** (*bool*) – Whether or not to include the submobjects of mobjects, by default True
            * **excluded\_mobjects** (*list* *|* *None*) – Any mobjects to exclude, by default None

        Returns:
        :   list of mobjects

        Return type:
        :   list

    get\_stroke\_rgbas(*vmobject*, *background=False*)[[source]](../_modules/manim/camera/camera.html#Camera.get_stroke_rgbas)[¶](#manim.camera.camera.Camera.get_stroke_rgbas "Link to this definition")
    :   Gets the RGBA array for the stroke of the passed
        VMobject.

        Parameters:
        :   * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The VMobject
            * **background** (*bool*) – Whether or not to consider the background when getting the stroke
              RGBAs, by default False

        Returns:
        :   The RGBA array of the stroke.

        Return type:
        :   np.ndarray

    get\_thickening\_nudges(*thickness*)[[source]](../_modules/manim/camera/camera.html#Camera.get_thickening_nudges)[¶](#manim.camera.camera.Camera.get_thickening_nudges "Link to this definition")
    :   Determine a list of vectors used to nudge
        two-dimensional pixel coordinates.

        Parameters:
        :   **thickness** (*float*)

        Return type:
        :   np.array

    init\_background()[[source]](../_modules/manim/camera/camera.html#Camera.init_background)[¶](#manim.camera.camera.Camera.init_background "Link to this definition")
    :   Initialize the background.
        If self.background\_image is the path of an image
        the image is set as background; else, the default
        background color fills the background.

    is\_in\_frame(*mobject*)[[source]](../_modules/manim/camera/camera.html#Camera.is_in_frame)[¶](#manim.camera.camera.Camera.is_in_frame "Link to this definition")
    :   Checks whether the passed mobject is in
        frame or not.

        Parameters:
        :   **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject for which the checking needs to be done.

        Returns:
        :   True if in frame, False otherwise.

        Return type:
        :   bool

    make\_background\_from\_func(*coords\_to\_colors\_func*)[[source]](../_modules/manim/camera/camera.html#Camera.make_background_from_func)[¶](#manim.camera.camera.Camera.make_background_from_func "Link to this definition")
    :   Makes a pixel array for the background by using coords\_to\_colors\_func to determine each pixel’s color. Each input
        pixel’s color. Each input to coords\_to\_colors\_func is an (x, y) pair in space (in ordinary space coordinates; not
        pixel coordinates), and each output is expected to be an RGBA array of 4 floats.

        Parameters:
        :   **coords\_to\_colors\_func** (*Callable**[**[**ndarray**]**,* *ndarray**]*) – The function whose input is an (x,y) pair of coordinates and
            whose return values must be the colors for that point

        Returns:
        :   The pixel array which can then be passed to set\_background.

        Return type:
        :   np.array

    on\_screen\_pixels(*pixel\_coords*)[[source]](../_modules/manim/camera/camera.html#Camera.on_screen_pixels)[¶](#manim.camera.camera.Camera.on_screen_pixels "Link to this definition")
    :   Returns array of pixels that are on the screen from a given
        array of pixel\_coordinates

        Parameters:
        :   **pixel\_coords** (*ndarray*) – The pixel coords to check.

        Returns:
        :   The pixel coords on screen.

        Return type:
        :   np.array

    overlay\_PIL\_image(*pixel\_array*, *image*)[[source]](../_modules/manim/camera/camera.html#Camera.overlay_PIL_image)[¶](#manim.camera.camera.Camera.overlay_PIL_image "Link to this definition")
    :   Overlays a PIL image on the passed pixel array.

        Parameters:
        :   * **pixel\_array** (*ndarray*) – The Pixel array
            * **image** (*<module 'PIL.Image' from '/home/docs/checkouts/readthedocs.org/user\_builds/manimce/envs/stable/lib/python3.13/site-packages/PIL/Image.py'>*) – The Image to overlay.

    overlay\_rgba\_array(*pixel\_array*, *new\_array*)[[source]](../_modules/manim/camera/camera.html#Camera.overlay_rgba_array)[¶](#manim.camera.camera.Camera.overlay_rgba_array "Link to this definition")
    :   Overlays an RGBA array on top of the given Pixel array.

        Parameters:
        :   * **pixel\_array** (*ndarray*) – The original pixel array to modify.
            * **new\_array** (*ndarray*) – The new pixel array to overlay.

    reset()[[source]](../_modules/manim/camera/camera.html#Camera.reset)[¶](#manim.camera.camera.Camera.reset "Link to this definition")
    :   Resets the camera’s pixel array
        to that of the background

        Returns:
        :   The camera object after setting the pixel array.

        Return type:
        :   [Camera](#manim.camera.camera.Camera "manim.camera.camera.Camera")

    reset\_pixel\_shape(*new\_height*, *new\_width*)[[source]](../_modules/manim/camera/camera.html#Camera.reset_pixel_shape)[¶](#manim.camera.camera.Camera.reset_pixel_shape "Link to this definition")
    :   This method resets the height and width
        of a single pixel to the passed new\_height and new\_width.

        Parameters:
        :   * **new\_height** (*float*) – The new height of the entire scene in pixels
            * **new\_width** (*float*) – The new width of the entire scene in pixels

    resize\_frame\_shape(*fixed\_dimension=0*)[[source]](../_modules/manim/camera/camera.html#Camera.resize_frame_shape)[¶](#manim.camera.camera.Camera.resize_frame_shape "Link to this definition")
    :   Changes frame\_shape to match the aspect ratio
        of the pixels, where fixed\_dimension determines
        whether frame\_height or frame\_width
        remains fixed while the other changes accordingly.

        Parameters:
        :   **fixed\_dimension** (*int*) – If 0, height is scaled with respect to width
            else, width is scaled with respect to height.

    set\_background(*pixel\_array*, *convert\_from\_floats=False*)[[source]](../_modules/manim/camera/camera.html#Camera.set_background)[¶](#manim.camera.camera.Camera.set_background "Link to this definition")
    :   Sets the background to the passed pixel\_array after converting
        to valid RGB values.

        Parameters:
        :   * **pixel\_array** (*ndarray* *|* *list* *|* *tuple*) – The pixel array to set the background to.
            * **convert\_from\_floats** (*bool*) – Whether or not to convert floats values to proper RGB valid ones, by default False

    set\_background\_from\_func(*coords\_to\_colors\_func*)[[source]](../_modules/manim/camera/camera.html#Camera.set_background_from_func)[¶](#manim.camera.camera.Camera.set_background_from_func "Link to this definition")
    :   Sets the background to a pixel array using coords\_to\_colors\_func to determine each pixel’s color. Each input
        pixel’s color. Each input to coords\_to\_colors\_func is an (x, y) pair in space (in ordinary space coordinates; not
        pixel coordinates), and each output is expected to be an RGBA array of 4 floats.

        Parameters:
        :   **coords\_to\_colors\_func** (*Callable**[**[**ndarray**]**,* *ndarray**]*) – The function whose input is an (x,y) pair of coordinates and
            whose return values must be the colors for that point

    set\_cairo\_context\_color(*ctx*, *rgbas*, *vmobject*)[[source]](../_modules/manim/camera/camera.html#Camera.set_cairo_context_color)[¶](#manim.camera.camera.Camera.set_cairo_context_color "Link to this definition")
    :   Sets the color of the cairo context

        Parameters:
        :   * **ctx** (*Context*) – The cairo context
            * **rgbas** (*ndarray*) – The RGBA array with which to color the context.
            * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The VMobject with which to set the color.

        Returns:
        :   The camera object

        Return type:
        :   [Camera](#manim.camera.camera.Camera "manim.camera.camera.Camera")

    set\_cairo\_context\_path(*ctx*, *vmobject*)[[source]](../_modules/manim/camera/camera.html#Camera.set_cairo_context_path)[¶](#manim.camera.camera.Camera.set_cairo_context_path "Link to this definition")
    :   Sets a path for the cairo context with the vmobject passed

        Parameters:
        :   * **ctx** (*Context*) – The cairo context
            * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The VMobject

        Returns:
        :   Camera object after setting cairo\_context\_path

        Return type:
        :   [Camera](#manim.camera.camera.Camera "manim.camera.camera.Camera")

    set\_pixel\_array(*pixel\_array*, *convert\_from\_floats=False*)[[source]](../_modules/manim/camera/camera.html#Camera.set_pixel_array)[¶](#manim.camera.camera.Camera.set_pixel_array "Link to this definition")
    :   Sets the pixel array of the camera to the passed pixel array.

        Parameters:
        :   * **pixel\_array** (*ndarray* *|* *list* *|* *tuple*) – The pixel array to convert and then set as the camera’s pixel array.
            * **convert\_from\_floats** (*bool*) – Whether or not to convert float values to proper RGB values, by default False

    thickened\_coordinates(*pixel\_coords*, *thickness*)[[source]](../_modules/manim/camera/camera.html#Camera.thickened_coordinates)[¶](#manim.camera.camera.Camera.thickened_coordinates "Link to this definition")
    :   Returns thickened coordinates for a passed array of pixel coords and
        a thickness to thicken by.

        Parameters:
        :   * **pixel\_coords** (*ndarray*) – Pixel coordinates
            * **thickness** (*float*) – Thickness

        Returns:
        :   Array of thickened pixel coords.

        Return type:
        :   np.array

    type\_or\_raise(*mobject*)[[source]](../_modules/manim/camera/camera.html#Camera.type_or_raise)[¶](#manim.camera.camera.Camera.type_or_raise "Link to this definition")
    :   Return the type of mobject, if it is a type that can be rendered.

        If mobject is an instance of a class that inherits from a class that
        can be rendered, return the super class. For example, an instance of a
        Square is also an instance of VMobject, and these can be rendered.
        Therefore, type\_or\_raise(Square()) returns True.

        Parameters:
        :   **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The object to take the type of.

        Notes

        For a list of classes that can currently be rendered, see `display_funcs()`.

        Returns:
        :   The type of mobjects, if it can be rendered.

        Return type:
        :   Type[[`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")]

        Raises:
        :   **TypeError** – When mobject is not an instance of a class that can be rendered.

        Parameters:
        :   **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))