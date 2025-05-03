# Source: https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ThreeDAxes.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ThreeDAxes[¶](#threedaxes "Link to this heading")
=================================================

Qualified name: `manim.mobject.graphing.coordinate\_systems.ThreeDAxes`

*class* ThreeDAxes(*x\_range=(-6, 6, 1)*, *y\_range=(-5, 5, 1)*, *z\_range=(-4, 4, 1)*, *x\_length=10.5*, *y\_length=10.5*, *z\_length=6.5*, *z\_axis\_config=None*, *z\_normal=array([0., -1., 0.])*, *num\_axis\_pieces=20*, *light\_source=array([-7., -9., 10.])*, *depth=None*, *gloss=0.5*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#ThreeDAxes)[¶](#manim.mobject.graphing.coordinate_systems.ThreeDAxes "Link to this definition")
:   Bases: [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes")

    A 3-dimensional set of axes.

    Parameters:
    :   * **x\_range** (*Sequence**[**float**]* *|* *None*) – The `[x_min, x_max, x_step]` values of the x-axis.
        * **y\_range** (*Sequence**[**float**]* *|* *None*) – The `[y_min, y_max, y_step]` values of the y-axis.
        * **z\_range** (*Sequence**[**float**]* *|* *None*) – The `[z_min, z_max, z_step]` values of the z-axis.
        * **x\_length** (*float* *|* *None*) – The length of the x-axis.
        * **y\_length** (*float* *|* *None*) – The length of the y-axis.
        * **z\_length** (*float* *|* *None*) – The length of the z-axis.
        * **z\_axis\_config** (*dict**[**str**,* *Any**]* *|* *None*) – Arguments to be passed to [`NumberLine`](manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine") that influence the z-axis.
        * **z\_normal** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The direction of the normal.
        * **num\_axis\_pieces** (*int*) – The number of pieces used to construct the axes.
        * **light\_source** (*Sequence**[**float**]*) – The direction of the light source.
        * **depth** – Currently non-functional.
        * **gloss** – Currently non-functional.
        * **kwargs** (*dict**[**str**,* *Any**]*) – Additional arguments to be passed to [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes").

    Methods

    |  |  |
    | --- | --- |
    | [`get_axis_labels`](#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_axis_labels "manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_axis_labels") | Defines labels for the x\_axis and y\_axis of the graph. |
    | [`get_y_axis_label`](#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_y_axis_label "manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_y_axis_label") | Generate a y-axis label. |
    | [`get_z_axis_label`](#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label "manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label") | Generate a z-axis label. |

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*x\_range=(-6, 6, 1)*, *y\_range=(-5, 5, 1)*, *z\_range=(-4, 4, 1)*, *x\_length=10.5*, *y\_length=10.5*, *z\_length=6.5*, *z\_axis\_config=None*, *z\_normal=array([0., -1., 0.])*, *num\_axis\_pieces=20*, *light\_source=array([-7., -9., 10.])*, *depth=None*, *gloss=0.5*, *\*\*kwargs*)[¶](#manim.mobject.graphing.coordinate_systems.ThreeDAxes._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **x\_range** (*Sequence**[**float**]* *|* *None*)
            * **y\_range** (*Sequence**[**float**]* *|* *None*)
            * **z\_range** (*Sequence**[**float**]* *|* *None*)
            * **x\_length** (*float* *|* *None*)
            * **y\_length** (*float* *|* *None*)
            * **z\_length** (*float* *|* *None*)
            * **z\_axis\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            * **z\_normal** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))
            * **num\_axis\_pieces** (*int*)
            * **light\_source** (*Sequence**[**float**]*)
            * **kwargs** (*dict**[**str**,* *Any**]*)

        Return type:
        :   None

    get\_axis\_labels(*x\_label='x'*, *y\_label='y'*, *z\_label='z'*)[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#ThreeDAxes.get_axis_labels)[¶](#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_axis_labels "Link to this definition")
    :   Defines labels for the x\_axis and y\_axis of the graph.

        For increased control over the position of the labels,
        use [`get_x_axis_label()`](manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_x_axis_label "manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_x_axis_label"),
        [`get_y_axis_label()`](#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_y_axis_label "manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_y_axis_label"), and
        [`get_z_axis_label()`](#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label "manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label").

        Parameters:
        :   * **x\_label** (*float* *|* *str* *|* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The label for the x\_axis. Defaults to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") for `str` and `float` inputs.
            * **y\_label** (*float* *|* *str* *|* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The label for the y\_axis. Defaults to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") for `str` and `float` inputs.
            * **z\_label** (*float* *|* *str* *|* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The label for the z\_axis. Defaults to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") for `str` and `float` inputs.

        Returns:
        :   A [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") of the labels for the x\_axis, y\_axis, and z\_axis.

        Return type:
        :   [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

        See also

        [`get_x_axis_label()`](manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_x_axis_label "manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_x_axis_label")
        [`get_y_axis_label()`](#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_y_axis_label "manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_y_axis_label")
        [`get_z_axis_label()`](#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label "manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label")

        Examples

        Example: GetAxisLabelsExample [¶](#getaxislabelsexample)

        ![../_images/GetAxisLabelsExample-2.png](../_images/GetAxisLabelsExample-2.png)

        ```
        from manim import *

        class GetAxisLabelsExample(ThreeDScene):
            def construct(self):
                self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
                axes = ThreeDAxes()
                labels = axes.get_axis_labels(
                    Text("x-axis").scale(0.7), Text("y-axis").scale(0.45), Text("z-axis").scale(0.45)
                )
                self.add(axes, labels)

        ```

        ```

        class GetAxisLabelsExample(ThreeDScene):
            def construct(self):
                self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
                axes = ThreeDAxes()
                labels = axes.get_axis_labels(
                    Text("x-axis").scale(0.7), Text("y-axis").scale(0.45), Text("z-axis").scale(0.45)
                )
                self.add(axes, labels)


        ```

    get\_y\_axis\_label(*label*, *edge=array([1., 1., 0.])*, *direction=array([1., 1., 0.])*, *buff=0.1*, *rotation=1.5707963267948966*, *rotation\_axis=array([0., 0., 1.])*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#ThreeDAxes.get_y_axis_label)[¶](#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_y_axis_label "Link to this definition")
    :   Generate a y-axis label.

        Parameters:
        :   * **label** (*float* *|* *str* *|* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The label. Defaults to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") for `str` and `float` inputs.
            * **edge** (*Sequence**[**float**]*) – The edge of the y-axis to which the label will be added, by default `UR`.
            * **direction** (*Sequence**[**float**]*) – Allows for further positioning of the label from an edge, by default `UR`.
            * **buff** (*float*) – The distance of the label from the line, by default `SMALL_BUFF`.
            * **rotation** (*float*) – The angle at which to rotate the label, by default `PI/2`.
            * **rotation\_axis** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The axis about which to rotate the label, by default `OUT`.

        Returns:
        :   The positioned label.

        Return type:
        :   [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

        Examples

        Example: GetYAxisLabelExample [¶](#getyaxislabelexample)

        ![../_images/GetYAxisLabelExample-2.png](../_images/GetYAxisLabelExample-2.png)

        ```
        from manim import *

        class GetYAxisLabelExample(ThreeDScene):
            def construct(self):
                ax = ThreeDAxes()
                lab = ax.get_y_axis_label(Tex("$y$-label"))
                self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
                self.add(ax, lab)

        ```

        ```

        class GetYAxisLabelExample(ThreeDScene):
            def construct(self):
                ax = ThreeDAxes()
                lab = ax.get_y_axis_label(Tex("$y$-label"))
                self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
                self.add(ax, lab)


        ```

    get\_z\_axis\_label(*label*, *edge=array([0., 0., 1.])*, *direction=array([1., 0., 0.])*, *buff=0.1*, *rotation=1.5707963267948966*, *rotation\_axis=array([1., 0., 0.])*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#ThreeDAxes.get_z_axis_label)[¶](#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label "Link to this definition")
    :   Generate a z-axis label.

        Parameters:
        :   * **label** (*float* *|* *str* *|* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The label. Defaults to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") for `str` and `float` inputs.
            * **edge** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The edge of the z-axis to which the label will be added, by default `OUT`.
            * **direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – Allows for further positioning of the label from an edge, by default `RIGHT`.
            * **buff** (*float*) – The distance of the label from the line, by default `SMALL_BUFF`.
            * **rotation** (*float*) – The angle at which to rotate the label, by default `PI/2`.
            * **rotation\_axis** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The axis about which to rotate the label, by default `RIGHT`.
            * **kwargs** (*Any*)

        Returns:
        :   The positioned label.

        Return type:
        :   [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

        Examples

        Example: GetZAxisLabelExample [¶](#getzaxislabelexample)

        ![../_images/GetZAxisLabelExample-1.png](../_images/GetZAxisLabelExample-1.png)

        ```
        from manim import *

        class GetZAxisLabelExample(ThreeDScene):
            def construct(self):
                ax = ThreeDAxes()
                lab = ax.get_z_axis_label(Tex("$z$-label"))
                self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
                self.add(ax, lab)

        ```

        ```

        class GetZAxisLabelExample(ThreeDScene):
            def construct(self):
                ax = ThreeDAxes()
                lab = ax.get_z_axis_label(Tex("$z$-label"))
                self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
                self.add(ax, lab)


        ```