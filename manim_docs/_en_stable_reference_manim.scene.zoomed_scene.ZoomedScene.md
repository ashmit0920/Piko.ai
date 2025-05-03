# Source: https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ZoomedScene[¶](#zoomedscene "Link to this heading")
===================================================

Qualified name: `manim.scene.zoomed\_scene.ZoomedScene`

*class* ZoomedScene(*camera\_class=<class 'manim.camera.multi\_camera.MultiCamera'>*, *zoomed\_display\_height=3*, *zoomed\_display\_width=3*, *zoomed\_display\_center=None*, *zoomed\_display\_corner=array([1.*, *1.*, *0.])*, *zoomed\_display\_corner\_buff=0.5*, *zoomed\_camera\_config={'background\_opacity': 1*, *'default\_frame\_stroke\_width': 2}*, *zoomed\_camera\_image\_mobject\_config={}*, *zoomed\_camera\_frame\_starting\_position=array([0.*, *0.*, *0.])*, *zoom\_factor=0.15*, *image\_frame\_stroke\_width=3*, *zoom\_activated=False*, *\*\*kwargs*)[[source]](../_modules/manim/scene/zoomed_scene.html#ZoomedScene)[¶](#manim.scene.zoomed_scene.ZoomedScene "Link to this definition")
:   Bases: [`MovingCameraScene`](manim.scene.moving_camera_scene.MovingCameraScene.html#manim.scene.moving_camera_scene.MovingCameraScene "manim.scene.moving_camera_scene.MovingCameraScene")

    This is a Scene with special configurations made for when
    a particular part of the scene must be zoomed in on and displayed
    separately.

    Methods

    |  |  |
    | --- | --- |
    | [`activate_zooming`](#manim.scene.zoomed_scene.ZoomedScene.activate_zooming "manim.scene.zoomed_scene.ZoomedScene.activate_zooming") | This method is used to activate the zooming for the zoomed\_camera. |
    | [`get_zoom_factor`](#manim.scene.zoomed_scene.ZoomedScene.get_zoom_factor "manim.scene.zoomed_scene.ZoomedScene.get_zoom_factor") | Returns the Zoom factor of the Zoomed camera. |
    | [`get_zoom_in_animation`](#manim.scene.zoomed_scene.ZoomedScene.get_zoom_in_animation "manim.scene.zoomed_scene.ZoomedScene.get_zoom_in_animation") | Returns the animation of camera zooming in. |
    | [`get_zoomed_display_pop_out_animation`](#manim.scene.zoomed_scene.ZoomedScene.get_zoomed_display_pop_out_animation "manim.scene.zoomed_scene.ZoomedScene.get_zoomed_display_pop_out_animation") | This is the animation of the popping out of the mini-display that shows the content of the zoomed camera. |
    | [`setup`](#manim.scene.zoomed_scene.ZoomedScene.setup "manim.scene.zoomed_scene.ZoomedScene.setup") | This method is used internally by Manim to setup the scene for proper use. |

    Attributes

    |  |  |
    | --- | --- |
    | `camera` |  |
    | `time` | The time since the start of the scene. |

    activate\_zooming(*animate=False*)[[source]](../_modules/manim/scene/zoomed_scene.html#ZoomedScene.activate_zooming)[¶](#manim.scene.zoomed_scene.ZoomedScene.activate_zooming "Link to this definition")
    :   This method is used to activate the zooming for
        the zoomed\_camera.

        Parameters:
        :   **animate** (*bool*) – Whether or not to animate the activation
            of the zoomed camera.

    get\_zoom\_factor()[[source]](../_modules/manim/scene/zoomed_scene.html#ZoomedScene.get_zoom_factor)[¶](#manim.scene.zoomed_scene.ZoomedScene.get_zoom_factor "Link to this definition")
    :   Returns the Zoom factor of the Zoomed camera.
        Defined as the ratio between the height of the
        zoomed camera and the height of the zoomed mini
        display.
        :returns: The zoom factor.
        :rtype: float

    get\_zoom\_in\_animation(*run\_time=2*, *\*\*kwargs*)[[source]](../_modules/manim/scene/zoomed_scene.html#ZoomedScene.get_zoom_in_animation)[¶](#manim.scene.zoomed_scene.ZoomedScene.get_zoom_in_animation "Link to this definition")
    :   Returns the animation of camera zooming in.

        Parameters:
        :   * **run\_time** (*float*) – The run\_time of the animation of the camera zooming in.
            * **\*\*kwargs** – Any valid keyword arguments of ApplyMethod()

        Returns:
        :   The animation of the camera zooming in.

        Return type:
        :   [ApplyMethod](manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

    get\_zoomed\_display\_pop\_out\_animation(*\*\*kwargs*)[[source]](../_modules/manim/scene/zoomed_scene.html#ZoomedScene.get_zoomed_display_pop_out_animation)[¶](#manim.scene.zoomed_scene.ZoomedScene.get_zoomed_display_pop_out_animation "Link to this definition")
    :   This is the animation of the popping out of the
        mini-display that shows the content of the zoomed
        camera.

        Returns:
        :   The Animation of the Zoomed Display popping out.

        Return type:
        :   [ApplyMethod](manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

    setup()[[source]](../_modules/manim/scene/zoomed_scene.html#ZoomedScene.setup)[¶](#manim.scene.zoomed_scene.ZoomedScene.setup "Link to this definition")
    :   This method is used internally by Manim to
        setup the scene for proper use.