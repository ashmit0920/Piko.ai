# Source: https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ComplexPlane[¶](#complexplane "Link to this heading")
=====================================================

Qualified name: `manim.mobject.graphing.coordinate\_systems.ComplexPlane`

*class* ComplexPlane(*\*\*kwargs*)[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#ComplexPlane)[¶](#manim.mobject.graphing.coordinate_systems.ComplexPlane "Link to this definition")
:   Bases: [`NumberPlane`](manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane "manim.mobject.graphing.coordinate_systems.NumberPlane")

    A [`NumberPlane`](manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane "manim.mobject.graphing.coordinate_systems.NumberPlane") specialized for use with complex numbers.

    Examples

    Example: ComplexPlaneExample [¶](#complexplaneexample)

    ![../_images/ComplexPlaneExample-1.png](../_images/ComplexPlaneExample-1.png)

    ```
    from manim import *

    class ComplexPlaneExample(Scene):
        def construct(self):
            plane = ComplexPlane().add_coordinates()
            self.add(plane)
            d1 = Dot(plane.n2p(2 + 1j), color=YELLOW)
            d2 = Dot(plane.n2p(-3 - 2j), color=YELLOW)
            label1 = MathTex("2+i").next_to(d1, UR, 0.1)
            label2 = MathTex("-3-2i").next_to(d2, UR, 0.1)
            self.add(
                d1,
                label1,
                d2,
                label2,
            )

    ```

    ```

    class ComplexPlaneExample(Scene):
        def construct(self):
            plane = ComplexPlane().add_coordinates()
            self.add(plane)
            d1 = Dot(plane.n2p(2 + 1j), color=YELLOW)
            d2 = Dot(plane.n2p(-3 - 2j), color=YELLOW)
            label1 = MathTex("2+i").next_to(d1, UR, 0.1)
            label2 = MathTex("-3-2i").next_to(d2, UR, 0.1)
            self.add(
                d1,
                label1,
                d2,
                label2,
            )


    ```

    References: [`Dot`](manim.mobject.geometry.arc.Dot.html#manim.mobject.geometry.arc.Dot "manim.mobject.geometry.arc.Dot") [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex")

    Methods

    |  |  |
    | --- | --- |
    | [`add_coordinates`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.add_coordinates "manim.mobject.graphing.coordinate_systems.ComplexPlane.add_coordinates") | Adds the labels produced from `get_coordinate_labels()` to the plane. |
    | [`get_coordinate_labels`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.get_coordinate_labels "manim.mobject.graphing.coordinate_systems.ComplexPlane.get_coordinate_labels") | Generates the [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") mobjects for the coordinates of the plane. |
    | [`n2p`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.n2p "manim.mobject.graphing.coordinate_systems.ComplexPlane.n2p") | Abbreviation for [`number_to_point()`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point "manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point"). |
    | [`number_to_point`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point "manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point") | Accepts a float/complex number and returns the equivalent point on the plane. |
    | [`p2n`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.p2n "manim.mobject.graphing.coordinate_systems.ComplexPlane.p2n") | Abbreviation for [`point_to_number()`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number "manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number"). |
    | [`point_to_number`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number "manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number") | Accepts a point and returns a complex number equivalent to that point on the plane. |

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

    Parameters:
    :   **kwargs** (*Any*)

    \_get\_default\_coordinate\_values()[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#ComplexPlane._get_default_coordinate_values)[¶](#manim.mobject.graphing.coordinate_systems.ComplexPlane._get_default_coordinate_values "Link to this definition")
    :   Generate a list containing the numerical values of the plane’s labels.

        Returns:
        :   A list of floats representing the x-axis and complex numbers representing the y-axis.

        Return type:
        :   List[float | complex]

    \_original\_\_init\_\_(*\*\*kwargs*)[¶](#manim.mobject.graphing.coordinate_systems.ComplexPlane._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   **kwargs** (*Any*)

        Return type:
        :   None

    add\_coordinates(*\*numbers*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#ComplexPlane.add_coordinates)[¶](#manim.mobject.graphing.coordinate_systems.ComplexPlane.add_coordinates "Link to this definition")
    :   Adds the labels produced from `get_coordinate_labels()` to the plane.

        Parameters:
        :   * **numbers** (*Iterable**[**float* *|* *complex**]*) – An iterable of floats/complex numbers. Floats are positioned along the x-axis, complex numbers along the y-axis.
            * **kwargs** (*Any*) – Additional arguments to be passed to [`get_number_mobject()`](manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine.get_number_mobject "manim.mobject.graphing.number_line.NumberLine.get_number_mobject"), i.e. [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber").

        Return type:
        :   *Self*

    get\_coordinate\_labels(*\*numbers*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#ComplexPlane.get_coordinate_labels)[¶](#manim.mobject.graphing.coordinate_systems.ComplexPlane.get_coordinate_labels "Link to this definition")
    :   Generates the [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") mobjects for the coordinates of the plane.

        Parameters:
        :   * **numbers** (*Iterable**[**float* *|* *complex**]*) – An iterable of floats/complex numbers. Floats are positioned along the x-axis, complex numbers along the y-axis.
            * **kwargs** (*Any*) – Additional arguments to be passed to [`get_number_mobject()`](manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine.get_number_mobject "manim.mobject.graphing.number_line.NumberLine.get_number_mobject"), i.e. [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber").

        Returns:
        :   A [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") containing the positioned label mobjects.

        Return type:
        :   [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

    n2p(*number*)[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#ComplexPlane.n2p)[¶](#manim.mobject.graphing.coordinate_systems.ComplexPlane.n2p "Link to this definition")
    :   Abbreviation for [`number_to_point()`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point "manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point").

        Parameters:
        :   **number** (*float* *|* *complex*)

        Return type:
        :   *ndarray*

    number\_to\_point(*number*)[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#ComplexPlane.number_to_point)[¶](#manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point "Link to this definition")
    :   Accepts a float/complex number and returns the equivalent point on the plane.

        Parameters:
        :   **number** (*float* *|* *complex*) – The number. Can be a float or a complex number.

        Returns:
        :   The point on the plane.

        Return type:
        :   np.ndarray

    p2n(*point*)[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#ComplexPlane.p2n)[¶](#manim.mobject.graphing.coordinate_systems.ComplexPlane.p2n "Link to this definition")
    :   Abbreviation for [`point_to_number()`](#manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number "manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number").

        Parameters:
        :   **point** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

        Return type:
        :   complex

    point\_to\_number(*point*)[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#ComplexPlane.point_to_number)[¶](#manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number "Link to this definition")
    :   Accepts a point and returns a complex number equivalent to that point on the plane.

        Parameters:
        :   **point** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – The point in manim’s coordinate-system

        Returns:
        :   A complex number consisting of real and imaginary components.

        Return type:
        :   complex