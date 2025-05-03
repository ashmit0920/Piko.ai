# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Transform[¶](#transform "Link to this heading")
===============================================

Qualified name: `manim.animation.transform.Transform`

*class* Transform(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform.html#Transform)[¶](#manim.animation.transform.Transform "Link to this definition")
:   Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    A Transform transforms a Mobject into a target Mobject.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *|* *None*) – The [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to be transformed. It will be mutated to become the `target_mobject`.
        * **target\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *|* *None*) – The target of the transformation.
        * **path\_func** (*Callable* *|* *None*) – A function defining the path that the points of the `mobject` are being moved
          along until they match the points of the `target_mobject`, see [`utils.paths`](manim.utils.paths.html#module-manim.utils.paths "manim.utils.paths").
        * **path\_arc** (*float*) – The arc angle (in radians) that the points of `mobject` will follow to reach
          the points of the target if using a circular path arc, see `path_arc_centers`.
          See also [`manim.utils.paths.path_along_arc()`](manim.utils.paths.html#manim.utils.paths.path_along_arc "manim.utils.paths.path_along_arc").
        * **path\_arc\_axis** (*np.ndarray*) – The axis to rotate along if using a circular path arc, see `path_arc_centers`.
        * **path\_arc\_centers** (*np.ndarray*) –

          The center of the circular arcs along which the points of `mobject` are
          moved by the transformation.

          If this is set and `path_func` is not set, then a `path_along_circles` path will be generated
          using the `path_arc` parameters and stored in `path_func`. If `path_func` is set, this and the
          other `path_arc` fields are set as attributes, but a `path_func` is not generated from it.
        * **replace\_mobject\_with\_target\_in\_scene** (*bool*) –

          Controls which mobject is replaced when the transformation is complete.

          If set to True, `mobject` will be removed from the scene and `target_mobject` will
          replace it. Otherwise, `target_mobject` is never added and `mobject` just takes its shape.

    Examples

    Example: TransformPathArc [¶](#transformpatharc)

    [
    ](./TransformPathArc-1.mp4)

    ```
    from manim import *

    class TransformPathArc(Scene):
        def construct(self):
            def make_arc_path(start, end, arc_angle):
                points = []
                p_fn = path_along_arc(arc_angle)
                # alpha animates between 0.0 and 1.0, where 0.0
                # is the beginning of the animation and 1.0 is the end.
                for alpha in range(0, 11):
                    points.append(p_fn(start, end, alpha / 10.0))
                path = VMobject(stroke_color=YELLOW)
                path.set_points_smoothly(points)
                return path

            left = Circle(stroke_color=BLUE_E, fill_opacity=1.0, radius=0.5).move_to(LEFT * 2)
            colors = [TEAL_A, TEAL_B, TEAL_C, TEAL_D, TEAL_E, GREEN_A]
            # Positive angles move counter-clockwise, negative angles move clockwise.
            examples = [-90, 0, 30, 90, 180, 270]
            anims = []
            for idx, angle in enumerate(examples):
                left_c = left.copy().shift((3 - idx) * UP)
                left_c.fill_color = colors[idx]
                right_c = left_c.copy().shift(4 * RIGHT)
                path_arc = make_arc_path(left_c.get_center(), right_c.get_center(),
                                         arc_angle=angle * DEGREES)
                desc = Text('%d°' % examples[idx]).next_to(left_c, LEFT)
                # Make the circles in front of the text in front of the arcs.
                self.add(
                    path_arc.set_z_index(1),
                    desc.set_z_index(2),
                    left_c.set_z_index(3),
                )
                anims.append(Transform(left_c, right_c, path_arc=angle * DEGREES))

            self.play(*anims, run_time=2)
            self.wait()

    ```

    ```

    class TransformPathArc(Scene):
        def construct(self):
            def make_arc_path(start, end, arc_angle):
                points = []
                p_fn = path_along_arc(arc_angle)
                # alpha animates between 0.0 and 1.0, where 0.0
                # is the beginning of the animation and 1.0 is the end.
                for alpha in range(0, 11):
                    points.append(p_fn(start, end, alpha / 10.0))
                path = VMobject(stroke_color=YELLOW)
                path.set_points_smoothly(points)
                return path

            left = Circle(stroke_color=BLUE_E, fill_opacity=1.0, radius=0.5).move_to(LEFT * 2)
            colors = [TEAL_A, TEAL_B, TEAL_C, TEAL_D, TEAL_E, GREEN_A]
            # Positive angles move counter-clockwise, negative angles move clockwise.
            examples = [-90, 0, 30, 90, 180, 270]
            anims = []
            for idx, angle in enumerate(examples):
                left_c = left.copy().shift((3 - idx) * UP)
                left_c.fill_color = colors[idx]
                right_c = left_c.copy().shift(4 * RIGHT)
                path_arc = make_arc_path(left_c.get_center(), right_c.get_center(),
                                         arc_angle=angle * DEGREES)
                desc = Text('%d°' % examples[idx]).next_to(left_c, LEFT)
                # Make the circles in front of the text in front of the arcs.
                self.add(
                    path_arc.set_z_index(1),
                    desc.set_z_index(2),
                    left_c.set_z_index(3),
                )
                anims.append(Transform(left_c, right_c, path_arc=angle * DEGREES))

            self.play(*anims, run_time=2)
            self.wait()


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`begin`](#manim.animation.transform.Transform.begin "manim.animation.transform.Transform.begin") | Begin the animation. |
    | [`clean_up_from_scene`](#manim.animation.transform.Transform.clean_up_from_scene "manim.animation.transform.Transform.clean_up_from_scene") | Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
    | `create_target` |  |
    | `get_all_families_zipped` |  |
    | [`get_all_mobjects`](#manim.animation.transform.Transform.get_all_mobjects "manim.animation.transform.Transform.get_all_mobjects") | Get all mobjects involved in the animation. |
    | `interpolate_submobject` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *target\_mobject=None*, *path\_func=None*, *path\_arc=0*, *path\_arc\_axis=array([0., 0., 1.])*, *path\_arc\_centers=None*, *replace\_mobject\_with\_target\_in\_scene=False*, *\*\*kwargs*)[¶](#manim.animation.transform.Transform._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *|* *None*)
            * **target\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *|* *None*)
            * **path\_func** (*Callable* *|* *None*)
            * **path\_arc** (*float*)
            * **path\_arc\_axis** (*ndarray*)
            * **path\_arc\_centers** (*ndarray*)
            * **replace\_mobject\_with\_target\_in\_scene** (*bool*)

        Return type:
        :   None

    begin()[[source]](../_modules/manim/animation/transform.html#Transform.begin)[¶](#manim.animation.transform.Transform.begin "Link to this definition")
    :   Begin the animation.

        This method is called right as an animation is being played. As much
        initialization as possible, especially any mobject copying, should live in this
        method.

        Return type:
        :   None

    clean\_up\_from\_scene(*scene*)[[source]](../_modules/manim/animation/transform.html#Transform.clean_up_from_scene)[¶](#manim.animation.transform.Transform.clean_up_from_scene "Link to this definition")
    :   Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.

        This includes to [`remove()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
        [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.

        Parameters:
        :   **scene** ([*Scene*](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.

        Return type:
        :   None

    get\_all\_mobjects()[[source]](../_modules/manim/animation/transform.html#Transform.get_all_mobjects)[¶](#manim.animation.transform.Transform.get_all_mobjects "Link to this definition")
    :   Get all mobjects involved in the animation.

        Ordering must match the ordering of arguments to interpolate\_submobject

        Returns:
        :   The sequence of mobjects.

        Return type:
        :   Sequence[[Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")]