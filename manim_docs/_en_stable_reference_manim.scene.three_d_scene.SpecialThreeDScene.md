# Source: https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.SpecialThreeDScene.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

SpecialThreeDScene[¶](#specialthreedscene "Link to this heading")
=================================================================

Qualified name: `manim.scene.three\_d\_scene.SpecialThreeDScene`

*class* SpecialThreeDScene(*cut\_axes\_at\_radius=True*, *camera\_config={'exponential\_projection': True, 'should\_apply\_shading': True}*, *three\_d\_axes\_config={'axis\_config': {'numbers\_with\_elongated\_ticks': [0, 1, 2], 'stroke\_width': 2, 'tick\_frequency': 1, 'unit\_size': 2}, 'num\_axis\_pieces': 1}*, *sphere\_config={'radius': 2, 'resolution': (24, 48)}*, *default\_angled\_camera\_position={'phi': 1.2217304763960306, 'theta': -1.9198621771937625}*, *low\_quality\_config={'camera\_config': {'should\_apply\_shading': False}, 'sphere\_config': {'resolution': (12, 24)}, 'three\_d\_axes\_config': {'num\_axis\_pieces': 1}}*, *\*\*kwargs*)[[source]](../_modules/manim/scene/three_d_scene.html#SpecialThreeDScene)[¶](#manim.scene.three_d_scene.SpecialThreeDScene "Link to this definition")
:   Bases: [`ThreeDScene`](manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene "manim.scene.three_d_scene.ThreeDScene")

    An extension of [`ThreeDScene`](manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene "manim.scene.three_d_scene.ThreeDScene") with more settings.

    It has some extra configuration for axes, spheres,
    and an override for low quality rendering. Further key differences
    are:

    * The camera shades applicable 3DMobjects by default,
      except if rendering in low quality.
    * Some default params for Spheres and Axes have been added.

    Methods

    |  |  |
    | --- | --- |
    | [`get_axes`](#manim.scene.three_d_scene.SpecialThreeDScene.get_axes "manim.scene.three_d_scene.SpecialThreeDScene.get_axes") | Return a set of 3D axes. |
    | [`get_default_camera_position`](#manim.scene.three_d_scene.SpecialThreeDScene.get_default_camera_position "manim.scene.three_d_scene.SpecialThreeDScene.get_default_camera_position") | Returns the default\_angled\_camera position. |
    | [`get_sphere`](#manim.scene.three_d_scene.SpecialThreeDScene.get_sphere "manim.scene.three_d_scene.SpecialThreeDScene.get_sphere") | Returns a sphere with the passed keyword arguments as properties. |
    | [`set_camera_to_default_position`](#manim.scene.three_d_scene.SpecialThreeDScene.set_camera_to_default_position "manim.scene.three_d_scene.SpecialThreeDScene.set_camera_to_default_position") | Sets the camera to its default position. |

    Attributes

    |  |  |
    | --- | --- |
    | `camera` |  |
    | `time` | The time since the start of the scene. |

    get\_axes()[[source]](../_modules/manim/scene/three_d_scene.html#SpecialThreeDScene.get_axes)[¶](#manim.scene.three_d_scene.SpecialThreeDScene.get_axes "Link to this definition")
    :   Return a set of 3D axes.

        Returns:
        :   A set of 3D axes.

        Return type:
        :   [`ThreeDAxes`](manim.mobject.graphing.coordinate_systems.ThreeDAxes.html#manim.mobject.graphing.coordinate_systems.ThreeDAxes "manim.mobject.graphing.coordinate_systems.ThreeDAxes")

    get\_default\_camera\_position()[[source]](../_modules/manim/scene/three_d_scene.html#SpecialThreeDScene.get_default_camera_position)[¶](#manim.scene.three_d_scene.SpecialThreeDScene.get_default_camera_position "Link to this definition")
    :   Returns the default\_angled\_camera position.

        Returns:
        :   Dictionary of phi, theta, focal\_distance, and gamma.

        Return type:
        :   dict

    get\_sphere(*\*\*kwargs*)[[source]](../_modules/manim/scene/three_d_scene.html#SpecialThreeDScene.get_sphere)[¶](#manim.scene.three_d_scene.SpecialThreeDScene.get_sphere "Link to this definition")
    :   Returns a sphere with the passed keyword arguments as properties.

        Parameters:
        :   **\*\*kwargs** – Any valid parameter of [`Sphere`](manim.mobject.three_d.three_dimensions.Sphere.html#manim.mobject.three_d.three_dimensions.Sphere "manim.mobject.three_d.three_dimensions.Sphere") or [`Surface`](manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface").

        Returns:
        :   The sphere object.

        Return type:
        :   [`Sphere`](manim.mobject.three_d.three_dimensions.Sphere.html#manim.mobject.three_d.three_dimensions.Sphere "manim.mobject.three_d.three_dimensions.Sphere")

    set\_camera\_to\_default\_position()[[source]](../_modules/manim/scene/three_d_scene.html#SpecialThreeDScene.set_camera_to_default_position)[¶](#manim.scene.three_d_scene.SpecialThreeDScene.set_camera_to_default_position "Link to this definition")
    :   Sets the camera to its default position.