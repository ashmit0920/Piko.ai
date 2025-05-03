# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcPolygonFromArcs.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ArcPolygonFromArcs[¶](#arcpolygonfromarcs "Link to this heading")
=================================================================

Qualified name: `manim.mobject.geometry.arc.ArcPolygonFromArcs`

*class* ArcPolygonFromArcs(*\*arcs*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/arc.html#ArcPolygonFromArcs)[¶](#manim.mobject.geometry.arc.ArcPolygonFromArcs "Link to this definition")
:   Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    A generalized polygon allowing for points to be connected with arcs.

    This version takes in pre-defined arcs to generate the arcpolygon and introduces
    little new syntax. However unlike `Polygon` it can’t be created with points
    directly.

    For proper appearance the passed arcs should connect seamlessly:
    `[a,b][b,c][c,a]`

    If there are any gaps between the arcs, those will be filled in
    with straight lines, which can be used deliberately for any straight
    sections. Arcs can also be passed as straight lines such as an arc
    initialized with `angle=0`.

    Parameters:
    :   * **arcs** ([*Arc*](manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc") *|* [*ArcBetweenPoints*](manim.mobject.geometry.arc.ArcBetweenPoints.html#manim.mobject.geometry.arc.ArcBetweenPoints "manim.mobject.geometry.arc.ArcBetweenPoints")) – These are the arcs from which the arcpolygon is assembled.
        * **kwargs** (*Any*) – Keyword arguments that are passed to the constructor of
          [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"). Affects how the ArcPolygon itself is drawn,
          but doesn’t affect passed arcs.

    arcs[¶](#manim.mobject.geometry.arc.ArcPolygonFromArcs.arcs "Link to this definition")
    :   The arcs used to initialize the ArcPolygonFromArcs:

        ```
        >>> from manim import ArcPolygonFromArcs, Arc, ArcBetweenPoints
        >>> ap = ArcPolygonFromArcs(Arc(), ArcBetweenPoints([1,0,0], [0,1,0]), Arc())
        >>> ap.arcs
        [Arc, ArcBetweenPoints, Arc]

        ```

    Tip

    Two instances of [`ArcPolygon`](manim.mobject.geometry.arc.ArcPolygon.html#manim.mobject.geometry.arc.ArcPolygon "manim.mobject.geometry.arc.ArcPolygon") can be transformed properly into
    one another as well. Be advised that any arc initialized with `angle=0`
    will actually be a straight line, so if a straight section should seamlessly
    transform into an arced section or vice versa, initialize the straight
    section with a negligible angle instead (such as `angle=0.0001`).

    Note

    There is an alternative version ([`ArcPolygon`](manim.mobject.geometry.arc.ArcPolygon.html#manim.mobject.geometry.arc.ArcPolygon "manim.mobject.geometry.arc.ArcPolygon")) that can be instantiated
    with points.

    See also

    [`ArcPolygon`](manim.mobject.geometry.arc.ArcPolygon.html#manim.mobject.geometry.arc.ArcPolygon "manim.mobject.geometry.arc.ArcPolygon")

    Examples

    One example of an arcpolygon is the Reuleaux triangle.
    Instead of 3 straight lines connecting the outer points,
    a Reuleaux triangle has 3 arcs connecting those points,
    making a shape with constant width.

    Passed arcs are stored as submobjects in the arcpolygon.
    This means that the arcs are changed along with the arcpolygon,
    for example when it’s shifted, and these arcs can be manipulated
    after the arcpolygon has been initialized.

    Also both the arcs contained in an [`ArcPolygonFromArcs`](#manim.mobject.geometry.arc.ArcPolygonFromArcs "manim.mobject.geometry.arc.ArcPolygonFromArcs"), as well as the
    arcpolygon itself are drawn, which affects draw time in [`Create`](manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create")
    for example. In most cases the arcs themselves don’t
    need to be drawn, in which case they can be passed as invisible.

    Example: ArcPolygonExample [¶](#arcpolygonexample)

    [
    ](./ArcPolygonExample-1.mp4)

    ```
    from manim import *

    class ArcPolygonExample(Scene):
        def construct(self):
            arc_conf = {"stroke_width": 0}
            poly_conf = {"stroke_width": 10, "stroke_color": BLUE,
                  "fill_opacity": 1, "color": PURPLE}
            a = [-1, 0, 0]
            b = [1, 0, 0]
            c = [0, np.sqrt(3), 0]
            arc0 = ArcBetweenPoints(a, b, radius=2, **arc_conf)
            arc1 = ArcBetweenPoints(b, c, radius=2, **arc_conf)
            arc2 = ArcBetweenPoints(c, a, radius=2, **arc_conf)
            reuleaux_tri = ArcPolygonFromArcs(arc0, arc1, arc2, **poly_conf)
            self.play(FadeIn(reuleaux_tri))
            self.wait(2)

    ```

    ```

    class ArcPolygonExample(Scene):
        def construct(self):
            arc_conf = {"stroke_width": 0}
            poly_conf = {"stroke_width": 10, "stroke_color": BLUE,
                  "fill_opacity": 1, "color": PURPLE}
            a = [-1, 0, 0]
            b = [1, 0, 0]
            c = [0, np.sqrt(3), 0]
            arc0 = ArcBetweenPoints(a, b, radius=2, **arc_conf)
            arc1 = ArcBetweenPoints(b, c, radius=2, **arc_conf)
            arc2 = ArcBetweenPoints(c, a, radius=2, **arc_conf)
            reuleaux_tri = ArcPolygonFromArcs(arc0, arc1, arc2, **poly_conf)
            self.play(FadeIn(reuleaux_tri))
            self.wait(2)


    ```

    The arcpolygon itself can also be hidden so that instead only the contained
    arcs are drawn. This can be used to easily debug arcs or to highlight them.

    Example: ArcPolygonExample2 [¶](#arcpolygonexample2)

    [
    ](./ArcPolygonExample2-1.mp4)

    ```
    from manim import *

    class ArcPolygonExample2(Scene):
        def construct(self):
            arc_conf = {"stroke_width": 3, "stroke_color": BLUE,
                "fill_opacity": 0.5, "color": GREEN}
            poly_conf = {"color": None}
            a = [-1, 0, 0]
            b = [1, 0, 0]
            c = [0, np.sqrt(3), 0]
            arc0 = ArcBetweenPoints(a, b, radius=2, **arc_conf)
            arc1 = ArcBetweenPoints(b, c, radius=2, **arc_conf)
            arc2 = ArcBetweenPoints(c, a, radius=2, stroke_color=RED)
            reuleaux_tri = ArcPolygonFromArcs(arc0, arc1, arc2, **poly_conf)
            self.play(FadeIn(reuleaux_tri))
            self.wait(2)

    ```

    ```

    class ArcPolygonExample2(Scene):
        def construct(self):
            arc_conf = {"stroke_width": 3, "stroke_color": BLUE,
                "fill_opacity": 0.5, "color": GREEN}
            poly_conf = {"color": None}
            a = [-1, 0, 0]
            b = [1, 0, 0]
            c = [0, np.sqrt(3), 0]
            arc0 = ArcBetweenPoints(a, b, radius=2, **arc_conf)
            arc1 = ArcBetweenPoints(b, c, radius=2, **arc_conf)
            arc2 = ArcBetweenPoints(c, a, radius=2, stroke_color=RED)
            reuleaux_tri = ArcPolygonFromArcs(arc0, arc1, arc2, **poly_conf)
            self.play(FadeIn(reuleaux_tri))
            self.wait(2)


    ```

    Methods

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

    \_original\_\_init\_\_(*\*arcs*, *\*\*kwargs*)[¶](#manim.mobject.geometry.arc.ArcPolygonFromArcs._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **arcs** ([*Arc*](manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc") *|* [*ArcBetweenPoints*](manim.mobject.geometry.arc.ArcBetweenPoints.html#manim.mobject.geometry.arc.ArcBetweenPoints "manim.mobject.geometry.arc.ArcBetweenPoints"))
            * **kwargs** (*Any*)

        Return type:
        :   None