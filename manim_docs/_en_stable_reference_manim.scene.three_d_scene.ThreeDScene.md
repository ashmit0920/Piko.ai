# Source: https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ThreeDScene[¶](#threedscene "Link to this heading")
===================================================

Qualified name: `manim.scene.three\_d\_scene.ThreeDScene`

*class* ThreeDScene(*camera\_class=<class 'manim.camera.three\_d\_camera.ThreeDCamera'>*, *ambient\_camera\_rotation=None*, *default\_angled\_camera\_orientation\_kwargs=None*, *\*\*kwargs*)[[source]](../_modules/manim/scene/three_d_scene.html#ThreeDScene)[¶](#manim.scene.three_d_scene.ThreeDScene "Link to this definition")
:   Bases: [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")

    This is a Scene, with special configurations and properties that
    make it suitable for Three Dimensional Scenes.

    Methods

    |  |  |
    | --- | --- |
    | [`add_fixed_in_frame_mobjects`](#manim.scene.three_d_scene.ThreeDScene.add_fixed_in_frame_mobjects "manim.scene.three_d_scene.ThreeDScene.add_fixed_in_frame_mobjects") | This method is used to prevent the rotation and movement of mobjects as the camera moves around. |
    | [`add_fixed_orientation_mobjects`](#manim.scene.three_d_scene.ThreeDScene.add_fixed_orientation_mobjects "manim.scene.three_d_scene.ThreeDScene.add_fixed_orientation_mobjects") | This method is used to prevent the rotation and tilting of mobjects as the camera moves around. |
    | [`begin_3dillusion_camera_rotation`](#manim.scene.three_d_scene.ThreeDScene.begin_3dillusion_camera_rotation "manim.scene.three_d_scene.ThreeDScene.begin_3dillusion_camera_rotation") | This method creates a 3D camera rotation illusion around the current camera orientation. |
    | [`begin_ambient_camera_rotation`](#manim.scene.three_d_scene.ThreeDScene.begin_ambient_camera_rotation "manim.scene.three_d_scene.ThreeDScene.begin_ambient_camera_rotation") | This method begins an ambient rotation of the camera about the Z\_AXIS, in the anticlockwise direction |
    | [`get_moving_mobjects`](#manim.scene.three_d_scene.ThreeDScene.get_moving_mobjects "manim.scene.three_d_scene.ThreeDScene.get_moving_mobjects") | This method returns a list of all of the Mobjects in the Scene that are moving, that are also in the animations passed. |
    | [`move_camera`](#manim.scene.three_d_scene.ThreeDScene.move_camera "manim.scene.three_d_scene.ThreeDScene.move_camera") | This method animates the movement of the camera to the given spherical coordinates. |
    | [`remove_fixed_in_frame_mobjects`](#manim.scene.three_d_scene.ThreeDScene.remove_fixed_in_frame_mobjects "manim.scene.three_d_scene.ThreeDScene.remove_fixed_in_frame_mobjects") | This method undoes what add\_fixed\_in\_frame\_mobjects does. |
    | [`remove_fixed_orientation_mobjects`](#manim.scene.three_d_scene.ThreeDScene.remove_fixed_orientation_mobjects "manim.scene.three_d_scene.ThreeDScene.remove_fixed_orientation_mobjects") | This method "unfixes" the orientation of the mobjects passed, meaning they will no longer be at the same angle relative to the camera. |
    | [`set_camera_orientation`](#manim.scene.three_d_scene.ThreeDScene.set_camera_orientation "manim.scene.three_d_scene.ThreeDScene.set_camera_orientation") | This method sets the orientation of the camera in the scene. |
    | [`set_to_default_angled_camera_orientation`](#manim.scene.three_d_scene.ThreeDScene.set_to_default_angled_camera_orientation "manim.scene.three_d_scene.ThreeDScene.set_to_default_angled_camera_orientation") | This method sets the default\_angled\_camera\_orientation to the keyword arguments passed, and sets the camera to that orientation. |
    | [`stop_3dillusion_camera_rotation`](#manim.scene.three_d_scene.ThreeDScene.stop_3dillusion_camera_rotation "manim.scene.three_d_scene.ThreeDScene.stop_3dillusion_camera_rotation") | This method stops all illusion camera rotations. |
    | [`stop_ambient_camera_rotation`](#manim.scene.three_d_scene.ThreeDScene.stop_ambient_camera_rotation "manim.scene.three_d_scene.ThreeDScene.stop_ambient_camera_rotation") | This method stops all ambient camera rotation. |

    Attributes

    |  |  |
    | --- | --- |
    | `camera` |  |
    | `time` | The time since the start of the scene. |

    add\_fixed\_in\_frame\_mobjects(*\*mobjects*)[[source]](../_modules/manim/scene/three_d_scene.html#ThreeDScene.add_fixed_in_frame_mobjects)[¶](#manim.scene.three_d_scene.ThreeDScene.add_fixed_in_frame_mobjects "Link to this definition")
    :   This method is used to prevent the rotation and movement
        of mobjects as the camera moves around. The mobject is
        essentially overlaid, and is not impacted by the camera’s
        movement in any way.

        Parameters:
        :   **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The Mobjects whose orientation must be fixed.

    add\_fixed\_orientation\_mobjects(*\*mobjects*, *\*\*kwargs*)[[source]](../_modules/manim/scene/three_d_scene.html#ThreeDScene.add_fixed_orientation_mobjects)[¶](#manim.scene.three_d_scene.ThreeDScene.add_fixed_orientation_mobjects "Link to this definition")
    :   This method is used to prevent the rotation and tilting
        of mobjects as the camera moves around. The mobject can
        still move in the x,y,z directions, but will always be
        at the angle (relative to the camera) that it was at
        when it was passed through this method.)

        Parameters:
        :   * **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The Mobject(s) whose orientation must be fixed.
            * **\*\*kwargs** –

              Some valid kwargs are
              :   use\_static\_center\_func : bool
                  center\_func : function

    begin\_3dillusion\_camera\_rotation(*rate=1*, *origin\_phi=None*, *origin\_theta=None*)[[source]](../_modules/manim/scene/three_d_scene.html#ThreeDScene.begin_3dillusion_camera_rotation)[¶](#manim.scene.three_d_scene.ThreeDScene.begin_3dillusion_camera_rotation "Link to this definition")
    :   This method creates a 3D camera rotation illusion around
        the current camera orientation.

        Parameters:
        :   * **rate** (*float*) – The rate at which the camera rotation illusion should operate.
            * **origin\_phi** (*float* *|* *None*) – The polar angle the camera should move around. Defaults
              to the current phi angle.
            * **origin\_theta** (*float* *|* *None*) – The azimutal angle the camera should move around. Defaults
              to the current theta angle.

    begin\_ambient\_camera\_rotation(*rate=0.02*, *about='theta'*)[[source]](../_modules/manim/scene/three_d_scene.html#ThreeDScene.begin_ambient_camera_rotation)[¶](#manim.scene.three_d_scene.ThreeDScene.begin_ambient_camera_rotation "Link to this definition")
    :   This method begins an ambient rotation of the camera about the Z\_AXIS,
        in the anticlockwise direction

        Parameters:
        :   * **rate** (*float*) – The rate at which the camera should rotate about the Z\_AXIS.
              Negative rate means clockwise rotation.
            * **about** (*str*) – one of 3 options: [“theta”, “phi”, “gamma”]. defaults to theta.

    get\_moving\_mobjects(*\*animations*)[[source]](../_modules/manim/scene/three_d_scene.html#ThreeDScene.get_moving_mobjects)[¶](#manim.scene.three_d_scene.ThreeDScene.get_moving_mobjects "Link to this definition")
    :   This method returns a list of all of the Mobjects in the Scene that
        are moving, that are also in the animations passed.

        Parameters:
        :   **\*animations** ([*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")) – The animations whose mobjects will be checked.

    move\_camera(*phi=None*, *theta=None*, *gamma=None*, *zoom=None*, *focal\_distance=None*, *frame\_center=None*, *added\_anims=[]*, *\*\*kwargs*)[[source]](../_modules/manim/scene/three_d_scene.html#ThreeDScene.move_camera)[¶](#manim.scene.three_d_scene.ThreeDScene.move_camera "Link to this definition")
    :   This method animates the movement of the camera
        to the given spherical coordinates.

        Parameters:
        :   * **phi** (*float* *|* *None*) – The polar angle i.e the angle between Z\_AXIS and Camera through ORIGIN in radians.
            * **theta** (*float* *|* *None*) – The azimuthal angle i.e the angle that spins the camera around the Z\_AXIS.
            * **focal\_distance** (*float* *|* *None*) – The radial focal\_distance between ORIGIN and Camera.
            * **gamma** (*float* *|* *None*) – The rotation of the camera about the vector from the ORIGIN to the Camera.
            * **zoom** (*float* *|* *None*) – The zoom factor of the camera.
            * **frame\_center** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *|* *Sequence**[**float**]* *|* *None*) – The new center of the camera frame in cartesian coordinates.
            * **added\_anims** (*Iterable**[*[*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")*]*) – Any other animations to be played at the same time.

    remove\_fixed\_in\_frame\_mobjects(*\*mobjects*)[[source]](../_modules/manim/scene/three_d_scene.html#ThreeDScene.remove_fixed_in_frame_mobjects)[¶](#manim.scene.three_d_scene.ThreeDScene.remove_fixed_in_frame_mobjects "Link to this definition")
    :   > This method undoes what add\_fixed\_in\_frame\_mobjects does.
        > It allows the mobject to be affected by the movement of
        > the camera.

        Parameters:
        :   **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The Mobjects whose position and orientation must be unfixed.

    remove\_fixed\_orientation\_mobjects(*\*mobjects*)[[source]](../_modules/manim/scene/three_d_scene.html#ThreeDScene.remove_fixed_orientation_mobjects)[¶](#manim.scene.three_d_scene.ThreeDScene.remove_fixed_orientation_mobjects "Link to this definition")
    :   This method “unfixes” the orientation of the mobjects
        passed, meaning they will no longer be at the same angle
        relative to the camera. This only makes sense if the
        mobject was passed through add\_fixed\_orientation\_mobjects first.

        Parameters:
        :   **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The Mobjects whose orientation must be unfixed.

    set\_camera\_orientation(*phi=None*, *theta=None*, *gamma=None*, *zoom=None*, *focal\_distance=None*, *frame\_center=None*, *\*\*kwargs*)[[source]](../_modules/manim/scene/three_d_scene.html#ThreeDScene.set_camera_orientation)[¶](#manim.scene.three_d_scene.ThreeDScene.set_camera_orientation "Link to this definition")
    :   This method sets the orientation of the camera in the scene.

        Parameters:
        :   * **phi** (*float* *|* *None*) – The polar angle i.e the angle between Z\_AXIS and Camera through ORIGIN in radians.
            * **theta** (*float* *|* *None*) – The azimuthal angle i.e the angle that spins the camera around the Z\_AXIS.
            * **focal\_distance** (*float* *|* *None*) – The focal\_distance of the Camera.
            * **gamma** (*float* *|* *None*) – The rotation of the camera about the vector from the ORIGIN to the Camera.
            * **zoom** (*float* *|* *None*) – The zoom factor of the scene.
            * **frame\_center** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *|* *Sequence**[**float**]* *|* *None*) – The new center of the camera frame in cartesian coordinates.

    set\_to\_default\_angled\_camera\_orientation(*\*\*kwargs*)[[source]](../_modules/manim/scene/three_d_scene.html#ThreeDScene.set_to_default_angled_camera_orientation)[¶](#manim.scene.three_d_scene.ThreeDScene.set_to_default_angled_camera_orientation "Link to this definition")
    :   This method sets the default\_angled\_camera\_orientation to the
        keyword arguments passed, and sets the camera to that orientation.

        Parameters:
        :   **\*\*kwargs** – Some recognised kwargs are phi, theta, focal\_distance, gamma,
            which have the same meaning as the parameters in set\_camera\_orientation.

    stop\_3dillusion\_camera\_rotation()[[source]](../_modules/manim/scene/three_d_scene.html#ThreeDScene.stop_3dillusion_camera_rotation)[¶](#manim.scene.three_d_scene.ThreeDScene.stop_3dillusion_camera_rotation "Link to this definition")
    :   This method stops all illusion camera rotations.

    stop\_ambient\_camera\_rotation(*about='theta'*)[[source]](../_modules/manim/scene/three_d_scene.html#ThreeDScene.stop_ambient_camera_rotation)[¶](#manim.scene.three_d_scene.ThreeDScene.stop_ambient_camera_rotation "Link to this definition")
    :   This method stops all ambient camera rotation.