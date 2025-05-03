# Source: https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Surface[¶](#surface "Link to this heading")
===========================================

Qualified name: `manim.mobject.three\_d.three\_dimensions.Surface`

*class* Surface(*func*, *u\_range=[0, 1]*, *v\_range=[0, 1]*, *resolution=32*, *surface\_piece\_config={}*, *fill\_color=ManimColor('#29ABCA')*, *fill\_opacity=1.0*, *checkerboard\_colors=[ManimColor('#29ABCA'), ManimColor('#236B8E')]*, *stroke\_color=ManimColor('#BBBBBB')*, *stroke\_width=0.5*, *should\_make\_jagged=False*, *pre\_function\_handle\_to\_anchor\_scale\_factor=1e-05*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Surface)[¶](#manim.mobject.three_d.three_dimensions.Surface "Link to this definition")
:   Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

    Creates a Parametric Surface using a checkerboard pattern.

    Parameters:
    :   * **func** (*Callable**[**[**float**,* *float**]**,* *np.ndarray**]*) – The function defining the [`Surface`](#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface").
        * **u\_range** (*Sequence**[**float**]*) – The range of the `u` variable: `(u_min, u_max)`.
        * **v\_range** (*Sequence**[**float**]*) – The range of the `v` variable: `(v_min, v_max)`.
        * **resolution** (*Sequence**[**int**]*) – The number of samples taken of the [`Surface`](#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface"). A tuple can be
          used to define different resolutions for `u` and `v` respectively.
        * **fill\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the [`Surface`](#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface"). Ignored if `checkerboard_colors`
          is set.
        * **fill\_opacity** (*float*) – The opacity of the [`Surface`](#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface"), from 0 being fully transparent
          to 1 being fully opaque. Defaults to 1.
        * **checkerboard\_colors** (*Sequence**[*[*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")*]* *|* *bool*) – ng individual faces alternating colors. Overrides `fill_color`.
        * **stroke\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – Color of the stroke surrounding each face of [`Surface`](#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface").
        * **stroke\_width** (*float*) – Width of the stroke surrounding each face of [`Surface`](#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface").
          Defaults to 0.5.
        * **should\_make\_jagged** (*bool*) – Changes the anchor mode of the Bézier curves from smooth to jagged.
          Defaults to `False`.
        * **surface\_piece\_config** (*dict*)
        * **pre\_function\_handle\_to\_anchor\_scale\_factor** (*float*)
        * **kwargs** (*Any*)

    Examples

    Example: ParaSurface [¶](#parasurface)

    ![../_images/ParaSurface-1.png](../_images/ParaSurface-1.png)

    ```
    from manim import *

    class ParaSurface(ThreeDScene):
        def func(self, u, v):
            return np.array([np.cos(u) * np.cos(v), np.cos(u) * np.sin(v), u])

        def construct(self):
            axes = ThreeDAxes(x_range=[-4,4], x_length=8)
            surface = Surface(
                lambda u, v: axes.c2p(*self.func(u, v)),
                u_range=[-PI, PI],
                v_range=[0, TAU],
                resolution=8,
            )
            self.set_camera_orientation(theta=70 * DEGREES, phi=75 * DEGREES)
            self.add(axes, surface)

    ```

    ```

    class ParaSurface(ThreeDScene):
        def func(self, u, v):
            return np.array([np.cos(u) * np.cos(v), np.cos(u) * np.sin(v), u])

        def construct(self):
            axes = ThreeDAxes(x_range=[-4,4], x_length=8)
            surface = Surface(
                lambda u, v: axes.c2p(*self.func(u, v)),
                u_range=[-PI, PI],
                v_range=[0, TAU],
                resolution=8,
            )
            self.set_camera_orientation(theta=70 * DEGREES, phi=75 * DEGREES)
            self.add(axes, surface)


    ```

    Methods

    |  |  |
    | --- | --- |
    | `func` |  |
    | [`set_fill_by_checkerboard`](#manim.mobject.three_d.three_dimensions.Surface.set_fill_by_checkerboard "manim.mobject.three_d.three_dimensions.Surface.set_fill_by_checkerboard") | Sets the fill\_color of each face of [`Surface`](#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface") in an alternating pattern. |
    | [`set_fill_by_value`](#manim.mobject.three_d.three_dimensions.Surface.set_fill_by_value "manim.mobject.three_d.three_dimensions.Surface.set_fill_by_value") | Sets the color of each mobject of a parametric surface to a color relative to its axis-value. |

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

    \_original\_\_init\_\_(*func*, *u\_range=[0, 1]*, *v\_range=[0, 1]*, *resolution=32*, *surface\_piece\_config={}*, *fill\_color=ManimColor('#29ABCA')*, *fill\_opacity=1.0*, *checkerboard\_colors=[ManimColor('#29ABCA'), ManimColor('#236B8E')]*, *stroke\_color=ManimColor('#BBBBBB')*, *stroke\_width=0.5*, *should\_make\_jagged=False*, *pre\_function\_handle\_to\_anchor\_scale\_factor=1e-05*, *\*\*kwargs*)[¶](#manim.mobject.three_d.three_dimensions.Surface._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **func** (*Callable**[**[**float**,* *float**]**,* *ndarray**]*)
            * **u\_range** (*Sequence**[**float**]*)
            * **v\_range** (*Sequence**[**float**]*)
            * **resolution** (*Sequence**[**int**]*)
            * **surface\_piece\_config** (*dict*)
            * **fill\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
            * **fill\_opacity** (*float*)
            * **checkerboard\_colors** (*Sequence**[*[*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")*]* *|* *bool*)
            * **stroke\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
            * **stroke\_width** (*float*)
            * **should\_make\_jagged** (*bool*)
            * **pre\_function\_handle\_to\_anchor\_scale\_factor** (*float*)
            * **kwargs** (*Any*)

        Return type:
        :   None

    set\_fill\_by\_checkerboard(*\*colors*, *opacity=None*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Surface.set_fill_by_checkerboard)[¶](#manim.mobject.three_d.three_dimensions.Surface.set_fill_by_checkerboard "Link to this definition")
    :   Sets the fill\_color of each face of [`Surface`](#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface") in
        an alternating pattern.

        Parameters:
        :   * **colors** (*Iterable**[*[*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")*]*) – List of colors for alternating pattern.
            * **opacity** (*float* *|* *None*) – The fill\_opacity of [`Surface`](#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface"), from 0 being fully transparent
              to 1 being fully opaque.

        Returns:
        :   The parametric surface with an alternating pattern.

        Return type:
        :   [`Surface`](#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface")

    set\_fill\_by\_value(*axes*, *colorscale=None*, *axis=2*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Surface.set_fill_by_value)[¶](#manim.mobject.three_d.three_dimensions.Surface.set_fill_by_value "Link to this definition")
    :   Sets the color of each mobject of a parametric surface to a color
        relative to its axis-value.

        Parameters:
        :   * **axes** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The axes for the parametric surface, which will be used to map
              axis-values to colors.
            * **colorscale** (*list**[*[*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")*]* *|* [*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *|* *None*) – A list of colors, ordered from lower axis-values to higher axis-values.
              If a list of tuples is passed containing colors paired with numbers,
              then those numbers will be used as the pivots.
            * **axis** (*int*) – The chosen axis to use for the color mapping. (0 = x, 1 = y, 2 = z)

        Returns:
        :   The parametric surface with a gradient applied by value. For chaining.

        Return type:
        :   [`Surface`](#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface")

        Examples

        Example: FillByValueExample [¶](#fillbyvalueexample)

        ![../_images/FillByValueExample-1.png](../_images/FillByValueExample-1.png)

        ```
        from manim import *

        class FillByValueExample(ThreeDScene):
            def construct(self):
                resolution_fa = 8
                self.set_camera_orientation(phi=75 * DEGREES, theta=-160 * DEGREES)
                axes = ThreeDAxes(x_range=(0, 5, 1), y_range=(0, 5, 1), z_range=(-1, 1, 0.5))
                def param_surface(u, v):
                    x = u
                    y = v
                    z = np.sin(x) * np.cos(y)
                    return z
                surface_plane = Surface(
                    lambda u, v: axes.c2p(u, v, param_surface(u, v)),
                    resolution=(resolution_fa, resolution_fa),
                    v_range=[0, 5],
                    u_range=[0, 5],
                    )
                surface_plane.set_style(fill_opacity=1)
                surface_plane.set_fill_by_value(axes=axes, colorscale=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
                self.add(axes, surface_plane)

        ```

        ```

        class FillByValueExample(ThreeDScene):
            def construct(self):
                resolution_fa = 8
                self.set_camera_orientation(phi=75 * DEGREES, theta=-160 * DEGREES)
                axes = ThreeDAxes(x_range=(0, 5, 1), y_range=(0, 5, 1), z_range=(-1, 1, 0.5))
                def param_surface(u, v):
                    x = u
                    y = v
                    z = np.sin(x) * np.cos(y)
                    return z
                surface_plane = Surface(
                    lambda u, v: axes.c2p(u, v, param_surface(u, v)),
                    resolution=(resolution_fa, resolution_fa),
                    v_range=[0, 5],
                    u_range=[0, 5],
                    )
                surface_plane.set_style(fill_opacity=1)
                surface_plane.set_fill_by_value(axes=axes, colorscale=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
                self.add(axes, surface_plane)


        ```