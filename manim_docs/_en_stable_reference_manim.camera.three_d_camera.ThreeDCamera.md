# Source: https://docs.manim.community/en/stable/reference/manim.camera.three_d_camera.ThreeDCamera.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ThreeDCamera[¶](#threedcamera "Link to this heading")
=====================================================

Qualified name: `manim.camera.three\_d\_camera.ThreeDCamera`

*class* ThreeDCamera(*focal\_distance=20.0*, *shading\_factor=0.2*, *default\_distance=5.0*, *light\_source\_start\_point=array([-7., -9., 10.])*, *should\_apply\_shading=True*, *exponential\_projection=False*, *phi=0*, *theta=-1.5707963267948966*, *gamma=0*, *zoom=1*, *\*\*kwargs*)[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera)[¶](#manim.camera.three_d_camera.ThreeDCamera "Link to this definition")
:   Bases: [`Camera`](manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera")

    Initializes the ThreeDCamera

    Parameters:
    :   **\*kwargs** – Any keyword argument of Camera.

    Methods

    |  |  |
    | --- | --- |
    | [`add_fixed_in_frame_mobjects`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_in_frame_mobjects "manim.camera.three_d_camera.ThreeDCamera.add_fixed_in_frame_mobjects") | This method allows the mobject to have a fixed position, even when the camera moves around. |
    | [`add_fixed_orientation_mobjects`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_orientation_mobjects "manim.camera.three_d_camera.ThreeDCamera.add_fixed_orientation_mobjects") | This method allows the mobject to have a fixed orientation, even when the camera moves around. |
    | [`capture_mobjects`](#manim.camera.three_d_camera.ThreeDCamera.capture_mobjects "manim.camera.three_d_camera.ThreeDCamera.capture_mobjects") | Capture mobjects by printing them on `pixel_array`. |
    | [`generate_rotation_matrix`](#manim.camera.three_d_camera.ThreeDCamera.generate_rotation_matrix "manim.camera.three_d_camera.ThreeDCamera.generate_rotation_matrix") | Generates a rotation matrix based off the current position of the camera. |
    | [`get_fill_rgbas`](#manim.camera.three_d_camera.ThreeDCamera.get_fill_rgbas "manim.camera.three_d_camera.ThreeDCamera.get_fill_rgbas") | Returns the RGBA array of the fill of the passed VMobject |
    | [`get_focal_distance`](#manim.camera.three_d_camera.ThreeDCamera.get_focal_distance "manim.camera.three_d_camera.ThreeDCamera.get_focal_distance") | Returns focal\_distance of the Camera. |
    | [`get_gamma`](#manim.camera.three_d_camera.ThreeDCamera.get_gamma "manim.camera.three_d_camera.ThreeDCamera.get_gamma") | Returns the rotation of the camera about the vector from the ORIGIN to the Camera. |
    | [`get_mobjects_to_display`](#manim.camera.three_d_camera.ThreeDCamera.get_mobjects_to_display "manim.camera.three_d_camera.ThreeDCamera.get_mobjects_to_display") | Used to get the list of mobjects to display with the camera. |
    | [`get_phi`](#manim.camera.three_d_camera.ThreeDCamera.get_phi "manim.camera.three_d_camera.ThreeDCamera.get_phi") | Returns the Polar angle (the angle off Z\_AXIS) phi. |
    | [`get_rotation_matrix`](#manim.camera.three_d_camera.ThreeDCamera.get_rotation_matrix "manim.camera.three_d_camera.ThreeDCamera.get_rotation_matrix") | Returns the matrix corresponding to the current position of the camera. |
    | [`get_stroke_rgbas`](#manim.camera.three_d_camera.ThreeDCamera.get_stroke_rgbas "manim.camera.three_d_camera.ThreeDCamera.get_stroke_rgbas") | Gets the RGBA array for the stroke of the passed VMobject. |
    | [`get_theta`](#manim.camera.three_d_camera.ThreeDCamera.get_theta "manim.camera.three_d_camera.ThreeDCamera.get_theta") | Returns the Azimuthal i.e the angle that spins the camera around the Z\_AXIS. |
    | [`get_value_trackers`](#manim.camera.three_d_camera.ThreeDCamera.get_value_trackers "manim.camera.three_d_camera.ThreeDCamera.get_value_trackers") | A list of [`ValueTrackers`](manim.mobject.value_tracker.ValueTracker.html#manim.mobject.value_tracker.ValueTracker "manim.mobject.value_tracker.ValueTracker") of phi, theta, focal\_distance, gamma and zoom. |
    | [`get_zoom`](#manim.camera.three_d_camera.ThreeDCamera.get_zoom "manim.camera.three_d_camera.ThreeDCamera.get_zoom") | Returns the zoom amount of the camera. |
    | `modified_rgbas` |  |
    | [`project_point`](#manim.camera.three_d_camera.ThreeDCamera.project_point "manim.camera.three_d_camera.ThreeDCamera.project_point") | Applies the current rotation\_matrix as a projection matrix to the passed point. |
    | [`project_points`](#manim.camera.three_d_camera.ThreeDCamera.project_points "manim.camera.three_d_camera.ThreeDCamera.project_points") | Applies the current rotation\_matrix as a projection matrix to the passed array of points. |
    | [`remove_fixed_in_frame_mobjects`](#manim.camera.three_d_camera.ThreeDCamera.remove_fixed_in_frame_mobjects "manim.camera.three_d_camera.ThreeDCamera.remove_fixed_in_frame_mobjects") | If a mobject was fixed in frame by passing it through [`add_fixed_in_frame_mobjects()`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_in_frame_mobjects "manim.camera.three_d_camera.ThreeDCamera.add_fixed_in_frame_mobjects"), then this undoes that fixing. |
    | [`remove_fixed_orientation_mobjects`](#manim.camera.three_d_camera.ThreeDCamera.remove_fixed_orientation_mobjects "manim.camera.three_d_camera.ThreeDCamera.remove_fixed_orientation_mobjects") | If a mobject was fixed in its orientation by passing it through [`add_fixed_orientation_mobjects()`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_orientation_mobjects "manim.camera.three_d_camera.ThreeDCamera.add_fixed_orientation_mobjects"), then this undoes that fixing. |
    | [`reset_rotation_matrix`](#manim.camera.three_d_camera.ThreeDCamera.reset_rotation_matrix "manim.camera.three_d_camera.ThreeDCamera.reset_rotation_matrix") | Sets the value of self.rotation\_matrix to the matrix corresponding to the current position of the camera |
    | [`set_focal_distance`](#manim.camera.three_d_camera.ThreeDCamera.set_focal_distance "manim.camera.three_d_camera.ThreeDCamera.set_focal_distance") | Sets the focal\_distance of the Camera. |
    | [`set_gamma`](#manim.camera.three_d_camera.ThreeDCamera.set_gamma "manim.camera.three_d_camera.ThreeDCamera.set_gamma") | Sets the angle of rotation of the camera about the vector from the ORIGIN to the Camera. |
    | [`set_phi`](#manim.camera.three_d_camera.ThreeDCamera.set_phi "manim.camera.three_d_camera.ThreeDCamera.set_phi") | Sets the polar angle i.e the angle between Z\_AXIS and Camera through ORIGIN in radians. |
    | [`set_theta`](#manim.camera.three_d_camera.ThreeDCamera.set_theta "manim.camera.three_d_camera.ThreeDCamera.set_theta") | Sets the azimuthal angle i.e the angle that spins the camera around Z\_AXIS in radians. |
    | [`set_zoom`](#manim.camera.three_d_camera.ThreeDCamera.set_zoom "manim.camera.three_d_camera.ThreeDCamera.set_zoom") | Sets the zoom amount of the camera. |
    | `transform_points_pre_display` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `background_color` |  |
    | `background_opacity` |  |
    | `frame_center` |  |

    add\_fixed\_in\_frame\_mobjects(*\*mobjects*)[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.add_fixed_in_frame_mobjects)[¶](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_in_frame_mobjects "Link to this definition")
    :   This method allows the mobject to have a fixed position,
        even when the camera moves around.
        E.G If it was passed through this method, at the top of the frame, it
        will continue to be displayed at the top of the frame.

        Highly useful when displaying Titles or formulae or the like.

        Parameters:
        :   **\*\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to fix in frame.

    add\_fixed\_orientation\_mobjects(*\*mobjects*, *use\_static\_center\_func=False*, *center\_func=None*)[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.add_fixed_orientation_mobjects)[¶](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_orientation_mobjects "Link to this definition")
    :   This method allows the mobject to have a fixed orientation,
        even when the camera moves around.
        E.G If it was passed through this method, facing the camera, it
        will continue to face the camera even as the camera moves.
        Highly useful when adding labels to graphs and the like.

        Parameters:
        :   * **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject whose orientation must be fixed.
            * **use\_static\_center\_func** (*bool*) – Whether or not to use the function that takes the mobject’s
              center as centerpoint, by default False
            * **center\_func** (*Callable**[**[**]**,* *ndarray**]* *|* *None*) – The function which returns the centerpoint
              with respect to which the mobject will be oriented, by default None

    capture\_mobjects(*mobjects*, *\*\*kwargs*)[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.capture_mobjects)[¶](#manim.camera.three_d_camera.ThreeDCamera.capture_mobjects "Link to this definition")
    :   Capture mobjects by printing them on `pixel_array`.

        This is the essential function that converts the contents of a Scene
        into an array, which is then converted to an image or video.

        Parameters:
        :   * **mobjects** – Mobjects to capture.
            * **kwargs** – Keyword arguments to be passed to [`get_mobjects_to_display()`](#manim.camera.three_d_camera.ThreeDCamera.get_mobjects_to_display "manim.camera.three_d_camera.ThreeDCamera.get_mobjects_to_display").

        Notes

        For a list of classes that can currently be rendered, see `display_funcs()`.

    generate\_rotation\_matrix()[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.generate_rotation_matrix)[¶](#manim.camera.three_d_camera.ThreeDCamera.generate_rotation_matrix "Link to this definition")
    :   Generates a rotation matrix based off the current position of the camera.

        Returns:
        :   The matrix corresponding to the current position of the camera.

        Return type:
        :   np.array

    get\_fill\_rgbas(*vmobject*)[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.get_fill_rgbas)[¶](#manim.camera.three_d_camera.ThreeDCamera.get_fill_rgbas "Link to this definition")
    :   Returns the RGBA array of the fill of the passed VMobject

        Parameters:
        :   **vmobject** – The VMobject

        Returns:
        :   The RGBA Array of the fill of the VMobject

        Return type:
        :   np.array

    get\_focal\_distance()[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.get_focal_distance)[¶](#manim.camera.three_d_camera.ThreeDCamera.get_focal_distance "Link to this definition")
    :   Returns focal\_distance of the Camera.

        Returns:
        :   The focal\_distance of the Camera in MUnits.

        Return type:
        :   float

    get\_gamma()[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.get_gamma)[¶](#manim.camera.three_d_camera.ThreeDCamera.get_gamma "Link to this definition")
    :   Returns the rotation of the camera about the vector from the ORIGIN to the Camera.

        Returns:
        :   The angle of rotation of the camera about the vector
            from the ORIGIN to the Camera in radians

        Return type:
        :   float

    get\_mobjects\_to\_display(*\*args*, *\*\*kwargs*)[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.get_mobjects_to_display)[¶](#manim.camera.three_d_camera.ThreeDCamera.get_mobjects_to_display "Link to this definition")
    :   Used to get the list of mobjects to display
        with the camera.

        Parameters:
        :   * **mobjects** – The Mobjects
            * **include\_submobjects** – Whether or not to include the submobjects of mobjects, by default True
            * **excluded\_mobjects** – Any mobjects to exclude, by default None

        Returns:
        :   list of mobjects

        Return type:
        :   list

    get\_phi()[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.get_phi)[¶](#manim.camera.three_d_camera.ThreeDCamera.get_phi "Link to this definition")
    :   Returns the Polar angle (the angle off Z\_AXIS) phi.

        Returns:
        :   The Polar angle in radians.

        Return type:
        :   float

    get\_rotation\_matrix()[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.get_rotation_matrix)[¶](#manim.camera.three_d_camera.ThreeDCamera.get_rotation_matrix "Link to this definition")
    :   Returns the matrix corresponding to the current position of the camera.

        Returns:
        :   The matrix corresponding to the current position of the camera.

        Return type:
        :   np.array

    get\_stroke\_rgbas(*vmobject*, *background=False*)[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.get_stroke_rgbas)[¶](#manim.camera.three_d_camera.ThreeDCamera.get_stroke_rgbas "Link to this definition")
    :   Gets the RGBA array for the stroke of the passed
        VMobject.

        Parameters:
        :   * **vmobject** – The VMobject
            * **background** – Whether or not to consider the background when getting the stroke
              RGBAs, by default False

        Returns:
        :   The RGBA array of the stroke.

        Return type:
        :   np.ndarray

    get\_theta()[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.get_theta)[¶](#manim.camera.three_d_camera.ThreeDCamera.get_theta "Link to this definition")
    :   Returns the Azimuthal i.e the angle that spins the camera around the Z\_AXIS.

        Returns:
        :   The Azimuthal angle in radians.

        Return type:
        :   float

    get\_value\_trackers()[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.get_value_trackers)[¶](#manim.camera.three_d_camera.ThreeDCamera.get_value_trackers "Link to this definition")
    :   A list of [`ValueTrackers`](manim.mobject.value_tracker.ValueTracker.html#manim.mobject.value_tracker.ValueTracker "manim.mobject.value_tracker.ValueTracker") of phi, theta, focal\_distance,
        gamma and zoom.

        Returns:
        :   list of ValueTracker objects

        Return type:
        :   list

    get\_zoom()[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.get_zoom)[¶](#manim.camera.three_d_camera.ThreeDCamera.get_zoom "Link to this definition")
    :   Returns the zoom amount of the camera.

        Returns:
        :   The zoom amount of the camera.

        Return type:
        :   float

    project\_point(*point*)[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.project_point)[¶](#manim.camera.three_d_camera.ThreeDCamera.project_point "Link to this definition")
    :   Applies the current rotation\_matrix as a projection
        matrix to the passed point.

        Parameters:
        :   **point** (*list* *|* *ndarray*) – The point to project.

        Returns:
        :   The point after projection.

        Return type:
        :   np.array

    project\_points(*points*)[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.project_points)[¶](#manim.camera.three_d_camera.ThreeDCamera.project_points "Link to this definition")
    :   Applies the current rotation\_matrix as a projection
        matrix to the passed array of points.

        Parameters:
        :   **points** (*ndarray* *|* *list*) – The list of points to project.

        Returns:
        :   The points after projecting.

        Return type:
        :   np.array

    remove\_fixed\_in\_frame\_mobjects(*\*mobjects*)[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.remove_fixed_in_frame_mobjects)[¶](#manim.camera.three_d_camera.ThreeDCamera.remove_fixed_in_frame_mobjects "Link to this definition")
    :   If a mobject was fixed in frame by passing it through
        [`add_fixed_in_frame_mobjects()`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_in_frame_mobjects "manim.camera.three_d_camera.ThreeDCamera.add_fixed_in_frame_mobjects"), then this undoes that fixing.
        The Mobject will no longer be fixed in frame.

        Parameters:
        :   **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects which need not be fixed in frame any longer.

    remove\_fixed\_orientation\_mobjects(*\*mobjects*)[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.remove_fixed_orientation_mobjects)[¶](#manim.camera.three_d_camera.ThreeDCamera.remove_fixed_orientation_mobjects "Link to this definition")
    :   If a mobject was fixed in its orientation by passing it through
        [`add_fixed_orientation_mobjects()`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_orientation_mobjects "manim.camera.three_d_camera.ThreeDCamera.add_fixed_orientation_mobjects"), then this undoes that fixing.
        The Mobject will no longer have a fixed orientation.

        Parameters:
        :   **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects whose orientation need not be fixed any longer.

    reset\_rotation\_matrix()[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.reset_rotation_matrix)[¶](#manim.camera.three_d_camera.ThreeDCamera.reset_rotation_matrix "Link to this definition")
    :   Sets the value of self.rotation\_matrix to
        the matrix corresponding to the current position of the camera

    set\_focal\_distance(*value*)[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.set_focal_distance)[¶](#manim.camera.three_d_camera.ThreeDCamera.set_focal_distance "Link to this definition")
    :   Sets the focal\_distance of the Camera.

        Parameters:
        :   **value** (*float*) – The focal\_distance of the Camera.

    set\_gamma(*value*)[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.set_gamma)[¶](#manim.camera.three_d_camera.ThreeDCamera.set_gamma "Link to this definition")
    :   Sets the angle of rotation of the camera about the vector from the ORIGIN to the Camera.

        Parameters:
        :   **value** (*float*) – The new angle of rotation of the camera.

    set\_phi(*value*)[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.set_phi)[¶](#manim.camera.three_d_camera.ThreeDCamera.set_phi "Link to this definition")
    :   Sets the polar angle i.e the angle between Z\_AXIS and Camera through ORIGIN in radians.

        Parameters:
        :   **value** (*float*) – The new value of the polar angle in radians.

    set\_theta(*value*)[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.set_theta)[¶](#manim.camera.three_d_camera.ThreeDCamera.set_theta "Link to this definition")
    :   Sets the azimuthal angle i.e the angle that spins the camera around Z\_AXIS in radians.

        Parameters:
        :   **value** (*float*) – The new value of the azimuthal angle in radians.

    set\_zoom(*value*)[[source]](../_modules/manim/camera/three_d_camera.html#ThreeDCamera.set_zoom)[¶](#manim.camera.three_d_camera.ThreeDCamera.set_zoom "Link to this definition")
    :   Sets the zoom amount of the camera.

        Parameters:
        :   **value** (*float*) – The zoom amount of the camera.