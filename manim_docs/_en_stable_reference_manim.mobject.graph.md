# Source: https://docs.manim.community/en/stable/reference/manim.mobject.graph.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

graph[¶](#module-manim.mobject.graph "Link to this heading")
============================================================

Mobjects used to represent mathematical graphs (think graph theory, not plotting).

Type Aliases

*class* NxGraph[¶](#manim.mobject.graph.NxGraph "Link to this definition")
:   ```
    nx.classes.graph.Graph | nx.classes.digraph.DiGraph

    ```

Classes

|  |  |
| --- | --- |
| [`DiGraph`](manim.mobject.graph.DiGraph.html#manim.mobject.graph.DiGraph "manim.mobject.graph.DiGraph") | A directed graph. |
| [`GenericGraph`](manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph "manim.mobject.graph.GenericGraph") | Abstract base class for graphs (that is, a collection of vertices connected with edges). |
| [`Graph`](manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph") | An undirected graph (vertices connected with edges). |
| [`LayoutFunction`](manim.mobject.graph.LayoutFunction.html#manim.mobject.graph.LayoutFunction "manim.mobject.graph.LayoutFunction") | A protocol for automatic layout functions that compute a layout for a graph to be used in `change_layout()`. |