# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygram.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Polygram[¶](#polygram "Link to this heading")
=============================================

Qualified name: `manim.mobject.geometry.polygram.Polygram`

*class* Polygram(*\*vertex\_groups*, *color=ManimColor('#58C4DD')*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/polygram.html#Polygram)[¶](#manim.mobject.geometry.polygram.Polygram "Link to this definition")
:   Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    A generalized [`Polygon`](manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon"), allowing for disconnected sets of edges.

    Parameters:
    :   * **vertex\_groups** ([*Point3DLike\_Array*](manim.typing.html#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array")) –

          The groups of vertices making up the [`Polygram`](#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram").

          The first vertex in each group is repeated to close the shape.
          Each point must be 3-dimensional: `[x,y,z]`
        * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram").
        * **kwargs** (*Any*) – Forwarded to the parent constructor.

    Examples

    Example: PolygramExample [¶](#polygramexample)

    [
    ](./PolygramExample-1.mp4)

    ```
    from manim import *

    import numpy as np

    class PolygramExample(Scene):
        def construct(self):
            hexagram = Polygram(
                [[0, 2, 0], [-np.sqrt(3), -1, 0], [np.sqrt(3), -1, 0]],
                [[-np.sqrt(3), 1, 0], [0, -2, 0], [np.sqrt(3), 1, 0]],
            )
            self.add(hexagram)

            dot = Dot()
            self.play(MoveAlongPath(dot, hexagram), run_time=5, rate_func=linear)
            self.remove(dot)
            self.wait()

    ```

    ```

    import numpy as np

    class PolygramExample(Scene):
        def construct(self):
            hexagram = Polygram(
                [[0, 2, 0], [-np.sqrt(3), -1, 0], [np.sqrt(3), -1, 0]],
                [[-np.sqrt(3), 1, 0], [0, -2, 0], [np.sqrt(3), 1, 0]],
            )
            self.add(hexagram)

            dot = Dot()
            self.play(MoveAlongPath(dot, hexagram), run_time=5, rate_func=linear)
            self.remove(dot)
            self.wait()


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`get_vertex_groups`](#manim.mobject.geometry.polygram.Polygram.get_vertex_groups "manim.mobject.geometry.polygram.Polygram.get_vertex_groups") | Gets the vertex groups of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram"). |
    | [`get_vertices`](#manim.mobject.geometry.polygram.Polygram.get_vertices "manim.mobject.geometry.polygram.Polygram.get_vertices") | Gets the vertices of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram"). |
    | [`round_corners`](#manim.mobject.geometry.polygram.Polygram.round_corners "manim.mobject.geometry.polygram.Polygram.round_corners") | Rounds off the corners of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram"). |

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

    \_original\_\_init\_\_(*\*vertex\_groups*, *color=ManimColor('#58C4DD')*, *\*\*kwargs*)[¶](#manim.mobject.geometry.polygram.Polygram._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **vertex\_groups** ([*Point3DLike\_Array*](manim.typing.html#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array"))
            * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
            * **kwargs** (*Any*)

    get\_vertex\_groups()[[source]](../_modules/manim/mobject/geometry/polygram.html#Polygram.get_vertex_groups)[¶](#manim.mobject.geometry.polygram.Polygram.get_vertex_groups "Link to this definition")
    :   Gets the vertex groups of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram").

        Returns:
        :   The vertex groups of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram").

        Return type:
        :   `numpy.ndarray`

        Examples

        ```
        >>> poly = Polygram([ORIGIN, RIGHT, UP], [LEFT, LEFT + UP, 2 * LEFT])
        >>> poly.get_vertex_groups()
        array([[[ 0.,  0.,  0.],
                [ 1.,  0.,  0.],
                [ 0.,  1.,  0.]],

               [[-1.,  0.,  0.],
                [-1.,  1.,  0.],
                [-2.,  0.,  0.]]])

        ```

    get\_vertices()[[source]](../_modules/manim/mobject/geometry/polygram.html#Polygram.get_vertices)[¶](#manim.mobject.geometry.polygram.Polygram.get_vertices "Link to this definition")
    :   Gets the vertices of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram").

        Returns:
        :   The vertices of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram").

        Return type:
        :   `numpy.ndarray`

        Examples

        ```
        >>> sq = Square()
        >>> sq.get_vertices()
        array([[ 1.,  1.,  0.],
               [-1.,  1.,  0.],
               [-1., -1.,  0.],
               [ 1., -1.,  0.]])

        ```

    round\_corners(*radius=0.5*, *evenly\_distribute\_anchors=False*, *components\_per\_rounded\_corner=2*)[[source]](../_modules/manim/mobject/geometry/polygram.html#Polygram.round_corners)[¶](#manim.mobject.geometry.polygram.Polygram.round_corners "Link to this definition")
    :   Rounds off the corners of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram").

        Parameters:
        :   * **radius** (*float* *|* *list**[**float**]*) – The curvature of the corners of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram").
            * **evenly\_distribute\_anchors** (*bool*) – Break long line segments into proportionally-sized segments.
            * **components\_per\_rounded\_corner** (*int*) – The number of points used to represent the rounded corner curve.

        Return type:
        :   Self

        See also

        `RoundedRectangle`

        Note

        If radius is supplied as a single value, then the same radius
        will be applied to all corners. If radius is a list, then the
        individual values will be applied sequentially, with the first
        corner receiving radius[0], the second corner receiving
        radius[1], etc. The radius list will be repeated as necessary.

        The components\_per\_rounded\_corner value is provided so that the
        fidelity of the rounded corner may be fine-tuned as needed. 2 is
        an appropriate value for most shapes, however a larger value may be
        need if the rounded corner is particularly large. 2 is the minimum
        number allowed, representing the start and end of the curve. 3 will
        result in a start, middle, and end point, meaning 2 curves will be
        generated.

        The option to evenly\_distribute\_anchors is provided so that the
        line segments (the part part of each line remaining after rounding
        off the corners) can be subdivided to a density similar to that of
        the average density of the rounded corners. This may be desirable
        in situations in which an even distribution of curves is desired
        for use in later transformation animations. Be aware, though, that
        enabling this option can result in an an object containing
        significantly more points than the original, especially when the
        rounded corner curves are small.

        Examples

        Example: PolygramRoundCorners [¶](#polygramroundcorners)

        ![../_images/PolygramRoundCorners-1.png](../_images/PolygramRoundCorners-1.png)

        ```
        from manim import *

        class PolygramRoundCorners(Scene):
            def construct(self):
                star = Star(outer_radius=2)

                shapes = VGroup(star)
                shapes.add(star.copy().round_corners(radius=0.1))
                shapes.add(star.copy().round_corners(radius=0.25))

                shapes.arrange(RIGHT)
                self.add(shapes)

        ```

        ```

        class PolygramRoundCorners(Scene):
            def construct(self):
                star = Star(outer_radius=2)

                shapes = VGroup(star)
                shapes.add(star.copy().round_corners(radius=0.1))
                shapes.add(star.copy().round_corners(radius=0.25))

                shapes.arrange(RIGHT)
                self.add(shapes)


        ```