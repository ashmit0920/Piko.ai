# Source: https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

GenericGraph[¶](#genericgraph "Link to this heading")
=====================================================

Qualified name: `manim.mobject.graph.GenericGraph`

*class* GenericGraph(*vertices*, *edges*, *labels=False*, *label\_fill\_color=ManimColor('#000000')*, *layout='spring'*, *layout\_scale=2*, *layout\_config=None*, *vertex\_type=<class 'manim.mobject.geometry.arc.Dot'>*, *vertex\_config=None*, *vertex\_mobjects=None*, *edge\_type=<class 'manim.mobject.geometry.line.Line'>*, *partitions=None*, *root\_vertex=None*, *edge\_config=None*)[[source]](../_modules/manim/mobject/graph.html#GenericGraph)[¶](#manim.mobject.graph.GenericGraph "Link to this definition")
:   Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    Abstract base class for graphs (that is, a collection of vertices
    connected with edges).

    Graphs can be instantiated by passing both a list of (distinct, hashable)
    vertex names, together with list of edges (as tuples of vertex names). See
    the examples for concrete implementations of this class for details.

    Note

    This implementation uses updaters to make the edges move with
    the vertices.

    See also

    [`Graph`](manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph"), [`DiGraph`](manim.mobject.graph.DiGraph.html#manim.mobject.graph.DiGraph "manim.mobject.graph.DiGraph")

    Parameters:
    :   * **vertices** (*Sequence**[**Hashable**]*) – A list of vertices. Must be hashable elements.
        * **edges** (*Sequence**[**tuple**[**Hashable**,* *Hashable**]**]*) – A list of edges, specified as tuples `(u, v)` where both `u`
          and `v` are vertices.
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
          for automatic vertex positioning primarily using `networkx`
          (see [their documentation](https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout)
          for more details), a dictionary specifying a coordinate (value)
          for each vertex (key) for manual positioning, or a .:class:~.LayoutFunction with a user-defined automatic layout.
        * **layout\_config** (*dict* *|* *None*) – Only for automatic layouts. A dictionary whose entries
          are passed as keyword arguments to the named layout or automatic layout function
          specified via `layout`.
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
          Must be a subclass of [`Line`](manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line") for default updaters to work.
        * **edge\_config** (*dict* *|* *None*) – Either a dictionary containing keyword arguments to be passed
          to the class specified via `edge_type`, or a dictionary whose
          keys are the edges, and whose values are dictionaries containing
          keyword arguments for the mobject related to the corresponding edge.
        * **partitions** (*Sequence**[**Sequence**[**Hashable**]**]* *|* *None*)
        * **root\_vertex** (*Hashable* *|* *None*)

    Methods

    |  |  |
    | --- | --- |
    | [`add_edges`](#manim.mobject.graph.GenericGraph.add_edges "manim.mobject.graph.GenericGraph.add_edges") | Add new edges to the graph. |
    | [`add_vertices`](#manim.mobject.graph.GenericGraph.add_vertices "manim.mobject.graph.GenericGraph.add_vertices") | Add a list of vertices to the graph. |
    | [`change_layout`](#manim.mobject.graph.GenericGraph.change_layout "manim.mobject.graph.GenericGraph.change_layout") | Change the layout of this graph. |
    | [`from_networkx`](#manim.mobject.graph.GenericGraph.from_networkx "manim.mobject.graph.GenericGraph.from_networkx") | Build a [`Graph`](manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph") or [`DiGraph`](manim.mobject.graph.DiGraph.html#manim.mobject.graph.DiGraph "manim.mobject.graph.DiGraph") from a given `networkx` graph. |
    | [`remove_edges`](#manim.mobject.graph.GenericGraph.remove_edges "manim.mobject.graph.GenericGraph.remove_edges") | Remove several edges from the graph. |
    | [`remove_vertices`](#manim.mobject.graph.GenericGraph.remove_vertices "manim.mobject.graph.GenericGraph.remove_vertices") | Remove several vertices from the graph. |

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

    \_add\_edge(*edge*, *edge\_type=<class 'manim.mobject.geometry.line.Line'>*, *edge\_config=None*)[[source]](../_modules/manim/mobject/graph.html#GenericGraph._add_edge)[¶](#manim.mobject.graph.GenericGraph._add_edge "Link to this definition")
    :   Add a new edge to the graph.

        Parameters:
        :   * **edge** (*tuple**[**Hashable**,* *Hashable**]*) – The edge (as a tuple of vertex identifiers) to be added. If a non-existing
              vertex is passed, a new vertex with default settings will be created. Create
              new vertices yourself beforehand to customize them.
            * **edge\_type** (*type**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The mobject class used for displaying edges in the scene.
            * **edge\_config** (*dict* *|* *None*) – A dictionary containing keyword arguments to be passed
              to the class specified via `edge_type`.

        Returns:
        :   A group containing all newly added vertices and edges.

        Return type:
        :   [Group](manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group")

    \_add\_vertex(*vertex*, *position=None*, *label=False*, *label\_fill\_color=ManimColor('#000000')*, *vertex\_type=<class 'manim.mobject.geometry.arc.Dot'>*, *vertex\_config=None*, *vertex\_mobject=None*)[[source]](../_modules/manim/mobject/graph.html#GenericGraph._add_vertex)[¶](#manim.mobject.graph.GenericGraph._add_vertex "Link to this definition")
    :   Add a vertex to the graph.

        Parameters:
        :   * **vertex** (*Hashable*) – A hashable vertex identifier.
            * **position** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") *|* *None*) – The coordinates where the new vertex should be added. If `None`, the center
              of the graph is used.
            * **label** (*bool*) – Controls whether or not the vertex is labeled. If `False` (the default),
              the vertex is not labeled; if `True` it is labeled using its
              names (as specified in `vertex`) via [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex"). Alternatively,
              any [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") can be passed to be used as the label.
            * **label\_fill\_color** (*str*) – Sets the fill color of the default labels generated when `labels`
              is set to `True`. Has no effect for other values of `label`.
            * **vertex\_type** (*type**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The mobject class used for displaying vertices in the scene.
            * **vertex\_config** (*dict* *|* *None*) – A dictionary containing keyword arguments to be passed to
              the class specified via `vertex_type`.
            * **vertex\_mobject** (*dict* *|* *None*) – The mobject to be used as the vertex. Overrides all other
              vertex customization options.

        Return type:
        :   [Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

    *static* \_empty\_networkx\_graph()[[source]](../_modules/manim/mobject/graph.html#GenericGraph._empty_networkx_graph)[¶](#manim.mobject.graph.GenericGraph._empty_networkx_graph "Link to this definition")
    :   Return an empty networkx graph for the given graph type.

        Return type:
        :   *Graph*

    \_original\_\_init\_\_(*vertices*, *edges*, *labels=False*, *label\_fill\_color=ManimColor('#000000')*, *layout='spring'*, *layout\_scale=2*, *layout\_config=None*, *vertex\_type=<class 'manim.mobject.geometry.arc.Dot'>*, *vertex\_config=None*, *vertex\_mobjects=None*, *edge\_type=<class 'manim.mobject.geometry.line.Line'>*, *partitions=None*, *root\_vertex=None*, *edge\_config=None*)[¶](#manim.mobject.graph.GenericGraph._original__init__ "Link to this definition")
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

    \_populate\_edge\_dict(*edges*, *edge\_type*)[[source]](../_modules/manim/mobject/graph.html#GenericGraph._populate_edge_dict)[¶](#manim.mobject.graph.GenericGraph._populate_edge_dict "Link to this definition")
    :   Helper method for populating the edges of the graph.

        Parameters:
        :   * **edges** (*list**[**tuple**[**Hashable**,* *Hashable**]**]*)
            * **edge\_type** (*type**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*)

    \_remove\_edge(*edge*)[[source]](../_modules/manim/mobject/graph.html#GenericGraph._remove_edge)[¶](#manim.mobject.graph.GenericGraph._remove_edge "Link to this definition")
    :   Remove an edge from the graph.

        Parameters:
        :   **edge** (*tuple**[**Hashable**]*) – The edge (i.e., a tuple of vertex identifiers) to be removed from the graph.

        Returns:
        :   The removed edge.

        Return type:
        :   [Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

    \_remove\_vertex(*vertex*)[[source]](../_modules/manim/mobject/graph.html#GenericGraph._remove_vertex)[¶](#manim.mobject.graph.GenericGraph._remove_vertex "Link to this definition")
    :   Remove a vertex (as well as all incident edges) from the graph.

        Parameters:
        :   **vertex** – The identifier of a vertex to be removed.

        Returns:
        :   A mobject containing all removed objects.

        Return type:
        :   [Group](manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group")

    add\_edges(*\*edges*, *edge\_type=<class 'manim.mobject.geometry.line.Line'>*, *edge\_config=None*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/graph.html#GenericGraph.add_edges)[¶](#manim.mobject.graph.GenericGraph.add_edges "Link to this definition")
    :   Add new edges to the graph.

        Parameters:
        :   * **edges** (*tuple**[**Hashable**,* *Hashable**]*) – Edges (as tuples of vertex identifiers) to be added. If a non-existing
              vertex is passed, a new vertex with default settings will be created. Create
              new vertices yourself beforehand to customize them.
            * **edge\_type** (*type**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The mobject class used for displaying edges in the scene.
            * **edge\_config** (*dict* *|* *None*) – A dictionary either containing keyword arguments to be passed
              to the class specified via `edge_type`, or a dictionary
              whose keys are the edge tuples, and whose values are dictionaries
              containing keyword arguments to be passed for the construction
              of the corresponding edge.
            * **kwargs** – Any further keyword arguments are passed to [`add_vertices()`](#manim.mobject.graph.GenericGraph.add_vertices "manim.mobject.graph.GenericGraph.add_vertices")
              which is used to create new vertices in the passed edges.

        Returns:
        :   A group containing all newly added vertices and edges.

        Return type:
        :   [Group](manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group")

    add\_vertices(*\*vertices*, *positions=None*, *labels=False*, *label\_fill\_color=ManimColor('#000000')*, *vertex\_type=<class 'manim.mobject.geometry.arc.Dot'>*, *vertex\_config=None*, *vertex\_mobjects=None*)[[source]](../_modules/manim/mobject/graph.html#GenericGraph.add_vertices)[¶](#manim.mobject.graph.GenericGraph.add_vertices "Link to this definition")
    :   Add a list of vertices to the graph.

        Parameters:
        :   * **vertices** (*Hashable*) – Hashable vertex identifiers.
            * **positions** (*dict* *|* *None*) – A dictionary specifying the coordinates where the new vertices should be added.
              If `None`, all vertices are created at the center of the graph.
            * **labels** (*bool*) – Controls whether or not the vertex is labeled. If `False` (the default),
              the vertex is not labeled; if `True` it is labeled using its
              names (as specified in `vertex`) via [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex"). Alternatively,
              any [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") can be passed to be used as the label.
            * **label\_fill\_color** (*str*) – Sets the fill color of the default labels generated when `labels`
              is set to `True`. Has no effect for other values of `labels`.
            * **vertex\_type** (*type**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The mobject class used for displaying vertices in the scene.
            * **vertex\_config** (*dict* *|* *None*) – A dictionary containing keyword arguments to be passed to
              the class specified via `vertex_type`.
            * **vertex\_mobjects** (*dict* *|* *None*) – A dictionary whose keys are the vertex identifiers, and whose
              values are mobjects that should be used as vertices. Overrides
              all other vertex customization options.
            * **self** ([*Graph*](manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph"))

    change\_layout(*layout='spring'*, *layout\_scale=2*, *layout\_config=None*, *partitions=None*, *root\_vertex=None*)[[source]](../_modules/manim/mobject/graph.html#GenericGraph.change_layout)[¶](#manim.mobject.graph.GenericGraph.change_layout "Link to this definition")
    :   Change the layout of this graph.

        See the documentation of [`Graph`](manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph") for details about the
        keyword arguments.

        Examples

        Example: ChangeGraphLayout [¶](#changegraphlayout)

        [
        ](./ChangeGraphLayout-1.mp4)

        ```
        from manim import *

        class ChangeGraphLayout(Scene):
            def construct(self):
                G = Graph([1, 2, 3, 4, 5], [(1, 2), (2, 3), (3, 4), (4, 5)],
                          layout={1: [-2, 0, 0], 2: [-1, 0, 0], 3: [0, 0, 0],
                                  4: [1, 0, 0], 5: [2, 0, 0]}
                          )
                self.play(Create(G))
                self.play(G.animate.change_layout("circular"))
                self.wait()

        ```

        ```

        class ChangeGraphLayout(Scene):
            def construct(self):
                G = Graph([1, 2, 3, 4, 5], [(1, 2), (2, 3), (3, 4), (4, 5)],
                          layout={1: [-2, 0, 0], 2: [-1, 0, 0], 3: [0, 0, 0],
                                  4: [1, 0, 0], 5: [2, 0, 0]}
                          )
                self.play(Create(G))
                self.play(G.animate.change_layout("circular"))
                self.wait()


        ```

        Parameters:
        :   * **layout** (*Literal**[**'circular'**,* *'kamada\_kawai'**,* *'partite'**,* *'planar'**,* *'random'**,* *'shell'**,* *'spectral'**,* *'spiral'**,* *'spring'**,* *'tree'**]* *|* *dict**[**~collections.abc.Hashable**,* *~manim.typing.Point3DLike**]* *|* *~manim.mobject.graph.LayoutFunction*)
            * **layout\_scale** (*float* *|* *tuple**[**float**,* *float**,* *float**]*)
            * **layout\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            * **partitions** (*list**[**list**[**Hashable**]**]* *|* *None*)
            * **root\_vertex** (*Hashable* *|* *None*)

        Return type:
        :   [*Graph*](manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph")

    *classmethod* from\_networkx(*nxgraph*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/graph.html#GenericGraph.from_networkx)[¶](#manim.mobject.graph.GenericGraph.from_networkx "Link to this definition")
    :   Build a [`Graph`](manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph") or [`DiGraph`](manim.mobject.graph.DiGraph.html#manim.mobject.graph.DiGraph "manim.mobject.graph.DiGraph") from a
        given `networkx` graph.

        Parameters:
        :   * **nxgraph** (*Graph* *|* *DiGraph*) – A `networkx` graph or digraph.
            * **\*\*kwargs** – Keywords to be passed to the constructor of [`Graph`](manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph").

        Examples

        Example: ImportNetworkxGraph [¶](#importnetworkxgraph)

        [
        ](./ImportNetworkxGraph-1.mp4)

        ```
        from manim import *

        import networkx as nx

        nxgraph = nx.erdos_renyi_graph(14, 0.5)

        class ImportNetworkxGraph(Scene):
            def construct(self):
                G = Graph.from_networkx(nxgraph, layout="spring", layout_scale=3.5)
                self.play(Create(G))
                self.play(*[G[v].animate.move_to(5*RIGHT*np.cos(ind/7 * PI) +
                                                 3*UP*np.sin(ind/7 * PI))
                            for ind, v in enumerate(G.vertices)])
                self.play(Uncreate(G))

        ```

        ```

        import networkx as nx

        nxgraph = nx.erdos_renyi_graph(14, 0.5)

        class ImportNetworkxGraph(Scene):
            def construct(self):
                G = Graph.from_networkx(nxgraph, layout="spring", layout_scale=3.5)
                self.play(Create(G))
                self.play(*[G[v].animate.move_to(5*RIGHT*np.cos(ind/7 * PI) +
                                                 3*UP*np.sin(ind/7 * PI))
                            for ind, v in enumerate(G.vertices)])
                self.play(Uncreate(G))


        ```

    remove\_edges(*\*edges*)[[source]](../_modules/manim/mobject/graph.html#GenericGraph.remove_edges)[¶](#manim.mobject.graph.GenericGraph.remove_edges "Link to this definition")
    :   Remove several edges from the graph.

        Parameters:
        :   **edges** (*tuple**[**Hashable**]*) – Edges to be removed from the graph.

        Returns:
        :   A group containing all removed edges.

        Return type:
        :   [Group](manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group")

    remove\_vertices(*\*vertices*)[[source]](../_modules/manim/mobject/graph.html#GenericGraph.remove_vertices)[¶](#manim.mobject.graph.GenericGraph.remove_vertices "Link to this definition")
    :   Remove several vertices from the graph.

        Parameters:
        :   **vertices** – Vertices to be removed from the graph.

        Examples

        ```
        >>> G = Graph([1, 2, 3], [(1, 2), (2, 3)])
        >>> removed = G.remove_vertices(2, 3); removed
        VGroup(Line, Line, Dot, Dot)
        >>> G
        Undirected graph on 1 vertices and 0 edges

        ```