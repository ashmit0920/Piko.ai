# Source: https://docs.manim.community/en/stable/reference/manim.mobject.graph.DiGraph.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

DiGraph[¶](#digraph "Link to this heading")
===========================================

Qualified name: `manim.mobject.graph.DiGraph`

*class* DiGraph(*vertices*, *edges*, *labels=False*, *label\_fill\_color=ManimColor('#000000')*, *layout='spring'*, *layout\_scale=2*, *layout\_config=None*, *vertex\_type=<class 'manim.mobject.geometry.arc.Dot'>*, *vertex\_config=None*, *vertex\_mobjects=None*, *edge\_type=<class 'manim.mobject.geometry.line.Line'>*, *partitions=None*, *root\_vertex=None*, *edge\_config=None*)[[source]](../_modules/manim/mobject/graph.html#DiGraph)[¶](#manim.mobject.graph.DiGraph "Link to this definition")
:   Bases: [`GenericGraph`](manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph "manim.mobject.graph.GenericGraph")

    A directed graph.

    Note

    In contrast to undirected graphs, the order in which vertices in a given
    edge are specified is relevant here.

    See also

    [`GenericGraph`](manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph "manim.mobject.graph.GenericGraph")

    Parameters:
    :   * **vertices** (*Sequence**[**Hashable**]*) – A list of vertices. Must be hashable elements.
        * **edges** (*Sequence**[**tuple**[**Hashable**,* *Hashable**]**]*) – A list of edges, specified as tuples `(u, v)` where both `u`
          and `v` are vertices. The edge is directed from `u` to `v`.
        * **labels** (*bool* *|* *dict*) – Controls whether or not vertices are labeled. If `False` (the default),
          the vertices are not labeled; if `True` they are labeled using their
          names (as specified in `vertices`) via [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex"). Alternatively,
          custom labels can be specified by passing a dictionary whose keys are
          the vertices, and whose values are the corresponding vertex labels
          (rendered via, e.g., [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") or [`Tex`](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex")).
        * **label\_fill\_color** (*str*) – Sets the fill color of the default labels generated when `labels`
          is set to `True`. Has no effect for other values of `labels`.
        * **layout** (*LayoutName* *|* *dict**[**Hashable**,* [*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")*]* *|* [*LayoutFunction*](manim.mobject.graph.LayoutFunction.html#manim.mobject.graph.LayoutFunction "manim.mobject.graph.LayoutFunction")) – Either one of `"spring"` (the default), `"circular"`, `"kamada_kawai"`,
          `"planar"`, `"random"`, `"shell"`, `"spectral"`, `"spiral"`, `"tree"`, and `"partite"`
          for automatic vertex positioning using `networkx`
          (see [their documentation](https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout)
          for more details), or a dictionary specifying a coordinate (value)
          for each vertex (key) for manual positioning.
        * **layout\_config** (*dict* *|* *None*) – Only for automatically generated layouts. A dictionary whose entries
          are passed as keyword arguments to the automatic layout algorithm
          specified via `layout` of `networkx`.
          The `tree` layout also accepts a special parameter `vertex_spacing`
          passed as a keyword argument inside the `layout_config` dictionary.
          Passing a tuple `(space_x, space_y)` as this argument overrides
          the value of `layout_scale` and ensures that vertices are arranged
          in a way such that the centers of siblings in the same layer are
          at least `space_x` units apart horizontally, and neighboring layers
          are spaced `space_y` units vertically.
        * **layout\_scale** (*float* *|* *tuple**[**float**,* *float**,* *float**]*) – The scale of automatically generated layouts: the vertices will
          be arranged such that the coordinates are located within the
          interval `[-scale, scale]`. Some layouts accept a tuple `(scale_x, scale_y)`
          causing the first coordinate to be in the interval `[-scale_x, scale_x]`,
          and the second in `[-scale_y, scale_y]`. Default: 2.
        * **vertex\_type** (*type**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The mobject class used for displaying vertices in the scene.
        * **vertex\_config** (*dict* *|* *None*) – Either a dictionary containing keyword arguments to be passed to
          the class specified via `vertex_type`, or a dictionary whose keys
          are the vertices, and whose values are dictionaries containing keyword
          arguments for the mobject related to the corresponding vertex.
        * **vertex\_mobjects** (*dict* *|* *None*) – A dictionary whose keys are the vertices, and whose values are
          mobjects to be used as vertices. Passing vertices here overrides
          all other configuration options for a vertex.
        * **edge\_type** (*type**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The mobject class used for displaying edges in the scene.
        * **edge\_config** (*dict* *|* *None*) – Either a dictionary containing keyword arguments to be passed
          to the class specified via `edge_type`, or a dictionary whose
          keys are the edges, and whose values are dictionaries containing
          keyword arguments for the mobject related to the corresponding edge.
          You can further customize the tip by adding a `tip_config` dictionary
          for global styling, or by adding the dict to a specific `edge_config`.
        * **partitions** (*Sequence**[**Sequence**[**Hashable**]**]* *|* *None*)
        * **root\_vertex** (*Hashable* *|* *None*)

    Examples

    Example: MovingDiGraph [¶](#movingdigraph)

    [
    ](./MovingDiGraph-1.mp4)

    ```
    from manim import *

    class MovingDiGraph(Scene):
        def construct(self):
            vertices = [1, 2, 3, 4]
            edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]

            g = DiGraph(vertices, edges)

            self.add(g)
            self.play(
                g[1].animate.move_to([1, 1, 1]),
                g[2].animate.move_to([-1, 1, 2]),
                g[3].animate.move_to([1, -1, -1]),
                g[4].animate.move_to([-1, -1, 0]),
            )
            self.wait()

    ```

    ```

    class MovingDiGraph(Scene):
        def construct(self):
            vertices = [1, 2, 3, 4]
            edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]

            g = DiGraph(vertices, edges)

            self.add(g)
            self.play(
                g[1].animate.move_to([1, 1, 1]),
                g[2].animate.move_to([-1, 1, 2]),
                g[3].animate.move_to([1, -1, -1]),
                g[4].animate.move_to([-1, -1, 0]),
            )
            self.wait()


    ```

    You can customize the edges and arrow tips globally or locally.

    Example: CustomDiGraph [¶](#customdigraph)

    [
    ](./CustomDiGraph-1.mp4)

    ```
    from manim import *

    class CustomDiGraph(Scene):
        def construct(self):
            vertices = [i for i in range(5)]
            edges = [
                (0, 1),
                (1, 2),
                (3, 2),
                (3, 4),
            ]

            edge_config = {
                "stroke_width": 2,
                "tip_config": {
                    "tip_shape": ArrowSquareTip,
                    "tip_length": 0.15,
                },
                (3, 4): {
                    "color": RED,
                    "tip_config": {"tip_length": 0.25, "tip_width": 0.25}
                },
            }

            g = DiGraph(
                vertices,
                edges,
                labels=True,
                layout="circular",
                edge_config=edge_config,
            ).scale(1.4)

            self.play(Create(g))
            self.wait()

    ```

    ```

    class CustomDiGraph(Scene):
        def construct(self):
            vertices = [i for i in range(5)]
            edges = [
                (0, 1),
                (1, 2),
                (3, 2),
                (3, 4),
            ]

            edge_config = {
                "stroke_width": 2,
                "tip_config": {
                    "tip_shape": ArrowSquareTip,
                    "tip_length": 0.15,
                },
                (3, 4): {
                    "color": RED,
                    "tip_config": {"tip_length": 0.25, "tip_width": 0.25}
                },
            }

            g = DiGraph(
                vertices,
                edges,
                labels=True,
                layout="circular",
                edge_config=edge_config,
            ).scale(1.4)

            self.play(Create(g))
            self.wait()


    ```

    Since this implementation respects the labels boundary you can also use
    it for an undirected moving graph with labels.

    Example: UndirectedMovingDiGraph [¶](#undirectedmovingdigraph)

    [
    ](./UndirectedMovingDiGraph-1.mp4)

    ```
    from manim import *

    class UndirectedMovingDiGraph(Scene):
        def construct(self):
            vertices = [i for i in range(5)]
            edges = [
                (0, 1),
                (1, 2),
                (3, 2),
                (3, 4),
            ]

            edge_config = {
                "stroke_width": 2,
                "tip_config": {"tip_length": 0, "tip_width": 0},
                (3, 4): {"color": RED},
            }

            g = DiGraph(
                vertices,
                edges,
                labels=True,
                layout="circular",
                edge_config=edge_config,
            ).scale(1.4)

            self.play(Create(g))
            self.wait()

            self.play(
                g[1].animate.move_to([1, 1, 1]),
                g[2].animate.move_to([-1, 1, 2]),
                g[3].animate.move_to([-1.5, -1.5, -1]),
                g[4].animate.move_to([1, -2, -1]),
            )
            self.wait()

    ```

    ```

    class UndirectedMovingDiGraph(Scene):
        def construct(self):
            vertices = [i for i in range(5)]
            edges = [
                (0, 1),
                (1, 2),
                (3, 2),
                (3, 4),
            ]

            edge_config = {
                "stroke_width": 2,
                "tip_config": {"tip_length": 0, "tip_width": 0},
                (3, 4): {"color": RED},
            }

            g = DiGraph(
                vertices,
                edges,
                labels=True,
                layout="circular",
                edge_config=edge_config,
            ).scale(1.4)

            self.play(Create(g))
            self.wait()

            self.play(
                g[1].animate.move_to([1, 1, 1]),
                g[2].animate.move_to([-1, 1, 2]),
                g[3].animate.move_to([-1.5, -1.5, -1]),
                g[4].animate.move_to([1, -2, -1]),
            )
            self.wait()


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`update_edges`](#manim.mobject.graph.DiGraph.update_edges "manim.mobject.graph.DiGraph.update_edges") | Updates the edges to stick at their corresponding vertices. |

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

    *static* \_empty\_networkx\_graph()[[source]](../_modules/manim/mobject/graph.html#DiGraph._empty_networkx_graph)[¶](#manim.mobject.graph.DiGraph._empty_networkx_graph "Link to this definition")
    :   Return an empty networkx graph for the given graph type.

        Return type:
        :   *DiGraph*

    \_original\_\_init\_\_(*vertices*, *edges*, *labels=False*, *label\_fill\_color=ManimColor('#000000')*, *layout='spring'*, *layout\_scale=2*, *layout\_config=None*, *vertex\_type=<class 'manim.mobject.geometry.arc.Dot'>*, *vertex\_config=None*, *vertex\_mobjects=None*, *edge\_type=<class 'manim.mobject.geometry.line.Line'>*, *partitions=None*, *root\_vertex=None*, *edge\_config=None*)[¶](#manim.mobject.graph.DiGraph._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **vertices** (*Sequence**[**Hashable**]*)
            * **edges** (*Sequence**[**tuple**[**Hashable**,* *Hashable**]**]*)
            * **labels** (*bool* *|* *dict*)
            * **label\_fill\_color** (*str*)
            * **layout** (*Literal**[**'circular'**,* *'kamada\_kawai'**,* *'partite'**,* *'planar'**,* *'random'**,* *'shell'**,* *'spectral'**,* *'spiral'**,* *'spring'**,* *'tree'**]* *|* *dict**[**~collections.abc.Hashable**,* *~manim.typing.Point3DLike**]* *|* *~manim.mobject.graph.LayoutFunction*)
            * **layout\_scale** (*float* *|* *tuple**[**float**,* *float**,* *float**]*)
            * **layout\_config** (*dict* *|* *None*)
            * **vertex\_type** (*type**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*)
            * **vertex\_config** (*dict* *|* *None*)
            * **vertex\_mobjects** (*dict* *|* *None*)
            * **edge\_type** (*type**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*)
            * **partitions** (*Sequence**[**Sequence**[**Hashable**]**]* *|* *None*)
            * **root\_vertex** (*Hashable* *|* *None*)
            * **edge\_config** (*dict* *|* *None*)

        Return type:
        :   None

    \_populate\_edge\_dict(*edges*, *edge\_type*)[[source]](../_modules/manim/mobject/graph.html#DiGraph._populate_edge_dict)[¶](#manim.mobject.graph.DiGraph._populate_edge_dict "Link to this definition")
    :   Helper method for populating the edges of the graph.

        Parameters:
        :   * **edges** (*list**[**tuple**[**Hashable**,* *Hashable**]**]*)
            * **edge\_type** (*type**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*)

    update\_edges(*graph*)[[source]](../_modules/manim/mobject/graph.html#DiGraph.update_edges)[¶](#manim.mobject.graph.DiGraph.update_edges "Link to this definition")
    :   Updates the edges to stick at their corresponding vertices.

        Arrow tips need to be repositioned since otherwise they can be
        deformed.