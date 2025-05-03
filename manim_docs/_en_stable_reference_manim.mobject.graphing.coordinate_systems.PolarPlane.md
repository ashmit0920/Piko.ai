# Source: https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.PolarPlane.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

PolarPlane[¶](#polarplane "Link to this heading")
=================================================

Qualified name: `manim.mobject.graphing.coordinate\_systems.PolarPlane`

*class* PolarPlane(*radius\_max=4.0*, *size=None*, *radius\_step=1*, *azimuth\_step=None*, *azimuth\_units='PI radians'*, *azimuth\_compact\_fraction=True*, *azimuth\_offset=0*, *azimuth\_direction='CCW'*, *azimuth\_label\_buff=0.1*, *azimuth\_label\_font\_size=24*, *radius\_config=None*, *background\_line\_style=None*, *faded\_line\_style=None*, *faded\_line\_ratio=1*, *make\_smooth\_after\_applying\_functions=True*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane)[¶](#manim.mobject.graphing.coordinate_systems.PolarPlane "Link to this definition")
:   Bases: [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes")

    Creates a polar plane with background lines.

    Parameters:
    :   * **azimuth\_step** (*float* *|* *None*) –

          The number of divisions in the azimuth (also known as the angular coordinate or polar angle). If `None` is specified then it will use the default
          specified by `azimuth_units`:

          + `"PI radians"` or `"TAU radians"`: 20
          + `"degrees"`: 36
          + `"gradians"`: 40
          + `None`: 1

          A non-integer value will result in a partial division at the end of the circle.
        * **size** (*float* *|* *None*) – The diameter of the plane.
        * **radius\_step** (*float*) – The distance between faded radius lines.
        * **radius\_max** (*float*) – The maximum value of the radius.
        * **azimuth\_units** (*str* *|* *None*) –

          Specifies a default labelling system for the azimuth. Choices are:

          + `"PI radians"`: Fractional labels in the interval \(\left[0, 2\pi\right]\) with \(\pi\) as a constant.
          + `"TAU radians"`: Fractional labels in the interval \(\left[0, \tau\right]\) (where \(\tau = 2\pi\)) with \(\tau\) as a constant.
          + `"degrees"`: Decimal labels in the interval \(\left[0, 360\right]\) with a degree (\(^{\circ}\)) symbol.
          + `"gradians"`: Decimal labels in the interval \(\left[0, 400\right]\) with a superscript “g” (\(^{g}\)).
          + `None`: Decimal labels in the interval \(\left[0, 1\right]\).
        * **azimuth\_compact\_fraction** (*bool*) – If the `azimuth_units` choice has fractional labels, choose whether to
          combine the constant in a compact form \(\tfrac{xu}{y}\) as opposed to
          \(\tfrac{x}{y}u\), where \(u\) is the constant.
        * **azimuth\_offset** (*float*) – The angle offset of the azimuth, expressed in radians.
        * **azimuth\_direction** (*str*) –

          The direction of the azimuth.

          + `"CW"`: Clockwise.
          + `"CCW"`: Anti-clockwise.
        * **azimuth\_label\_buff** (*float*) – The buffer for the azimuth labels.
        * **azimuth\_label\_font\_size** (*float*) – The font size of the azimuth labels.
        * **radius\_config** (*dict**[**str**,* *Any**]* *|* *None*) – The axis config for the radius.
        * **background\_line\_style** (*dict**[**str**,* *Any**]* *|* *None*)
        * **faded\_line\_style** (*dict**[**str**,* *Any**]* *|* *None*)
        * **faded\_line\_ratio** (*int*)
        * **make\_smooth\_after\_applying\_functions** (*bool*)
        * **kwargs** (*Any*)

    Examples

    Example: PolarPlaneExample [¶](#polarplaneexample)

    ![../_images/PolarPlaneExample-1.png](../_images/PolarPlaneExample-1.png)

    ```
    from manim import *

    class PolarPlaneExample(Scene):
        def construct(self):
            polarplane_pi = PolarPlane(
                azimuth_units="PI radians",
                size=6,
                azimuth_label_font_size=33.6,
                radius_config={"font_size": 33.6},
            ).add_coordinates()
            self.add(polarplane_pi)

    ```

    ```

    class PolarPlaneExample(Scene):
        def construct(self):
            polarplane_pi = PolarPlane(
                azimuth_units="PI radians",
                size=6,
                azimuth_label_font_size=33.6,
                radius_config={"font_size": 33.6},
            ).add_coordinates()
            self.add(polarplane_pi)


    ```

    References: [`PolarPlane`](#manim.mobject.graphing.coordinate_systems.PolarPlane "manim.mobject.graphing.coordinate_systems.PolarPlane")

    Methods

    |  |  |
    | --- | --- |
    | [`add_coordinates`](#manim.mobject.graphing.coordinate_systems.PolarPlane.add_coordinates "manim.mobject.graphing.coordinate_systems.PolarPlane.add_coordinates") | Adds the coordinates. |
    | [`get_axes`](#manim.mobject.graphing.coordinate_systems.PolarPlane.get_axes "manim.mobject.graphing.coordinate_systems.PolarPlane.get_axes") | Gets the axes. |
    | [`get_coordinate_labels`](#manim.mobject.graphing.coordinate_systems.PolarPlane.get_coordinate_labels "manim.mobject.graphing.coordinate_systems.PolarPlane.get_coordinate_labels") | Gets labels for the coordinates |
    | `get_radian_label` |  |
    | `get_vector` |  |
    | `prepare_for_nonlinear_transform` |  |

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

    \_get\_lines()[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane._get_lines)[¶](#manim.mobject.graphing.coordinate_systems.PolarPlane._get_lines "Link to this definition")
    :   Generate all the lines and circles, faded and not faded.

        Returns:
        :   The first (i.e the non faded lines and circles) and second (i.e the faded lines and circles) sets of lines and circles, respectively.

        Return type:
        :   Tuple[[`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup"), [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")]

    \_init\_background\_lines()[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane._init_background_lines)[¶](#manim.mobject.graphing.coordinate_systems.PolarPlane._init_background_lines "Link to this definition")
    :   Will init all the lines of NumberPlanes (faded or not)

        Return type:
        :   None

    \_original\_\_init\_\_(*radius\_max=4.0*, *size=None*, *radius\_step=1*, *azimuth\_step=None*, *azimuth\_units='PI radians'*, *azimuth\_compact\_fraction=True*, *azimuth\_offset=0*, *azimuth\_direction='CCW'*, *azimuth\_label\_buff=0.1*, *azimuth\_label\_font\_size=24*, *radius\_config=None*, *background\_line\_style=None*, *faded\_line\_style=None*, *faded\_line\_ratio=1*, *make\_smooth\_after\_applying\_functions=True*, *\*\*kwargs*)[¶](#manim.mobject.graphing.coordinate_systems.PolarPlane._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **radius\_max** (*float*)
            * **size** (*float* *|* *None*)
            * **radius\_step** (*float*)
            * **azimuth\_step** (*float* *|* *None*)
            * **azimuth\_units** (*str* *|* *None*)
            * **azimuth\_compact\_fraction** (*bool*)
            * **azimuth\_offset** (*float*)
            * **azimuth\_direction** (*str*)
            * **azimuth\_label\_buff** (*float*)
            * **azimuth\_label\_font\_size** (*float*)
            * **radius\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            * **background\_line\_style** (*dict**[**str**,* *Any**]* *|* *None*)
            * **faded\_line\_style** (*dict**[**str**,* *Any**]* *|* *None*)
            * **faded\_line\_ratio** (*int*)
            * **make\_smooth\_after\_applying\_functions** (*bool*)
            * **kwargs** (*Any*)

        Return type:
        :   None

    add\_coordinates(*r\_values=None*, *a\_values=None*)[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane.add_coordinates)[¶](#manim.mobject.graphing.coordinate_systems.PolarPlane.add_coordinates "Link to this definition")
    :   Adds the coordinates.

        Parameters:
        :   * **r\_values** (*Iterable**[**float**]* *|* *None*) – Iterable of values along the radius, by default None.
            * **a\_values** (*Iterable**[**float**]* *|* *None*) – Iterable of values along the azimuth, by default None.

        Return type:
        :   *Self*

    get\_axes()[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane.get_axes)[¶](#manim.mobject.graphing.coordinate_systems.PolarPlane.get_axes "Link to this definition")
    :   Gets the axes.

        Returns:
        :   A pair of axes.

        Return type:
        :   [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

    get\_coordinate\_labels(*r\_values=None*, *a\_values=None*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane.get_coordinate_labels)[¶](#manim.mobject.graphing.coordinate_systems.PolarPlane.get_coordinate_labels "Link to this definition")
    :   Gets labels for the coordinates

        Parameters:
        :   * **r\_values** (*Iterable**[**float**]* *|* *None*) – Iterable of values along the radius, by default None.
            * **a\_values** (*Iterable**[**float**]* *|* *None*) – Iterable of values along the azimuth, by default None.
            * **kwargs** (*Any*)

        Returns:
        :   Labels for the radius and azimuth values.

        Return type:
        :   [VDict](manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "manim.mobject.types.vectorized_mobject.VDict")