# Source: https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Polyhedron.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Polyhedron[¶](#polyhedron "Link to this heading")
=================================================

Qualified name: `manim.mobject.three\_d.polyhedra.Polyhedron`

*class* Polyhedron(*vertex\_coords*, *faces\_list*, *faces\_config={}*, *graph\_config={}*)[[source]](../_modules/manim/mobject/three_d/polyhedra.html#Polyhedron)[¶](#manim.mobject.three_d.polyhedra.Polyhedron "Link to this definition")
:   Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

    An abstract polyhedra class.

    In this implementation, polyhedra are defined with a list of vertex coordinates in space, and a list
    of faces. This implementation mirrors that of a standard polyhedral data format (OFF, object file format).

    Parameters:
    :   * **vertex\_coords** (*list**[**list**[**float**]* *|* *np.ndarray**]*) – A list of coordinates of the corresponding vertices in the polyhedron. Each coordinate will correspond to
          a vertex. The vertices are indexed with the usual indexing of Python.
        * **faces\_list** (*list**[**list**[**int**]**]*) – A list of faces. Each face is a sublist containing the indices of the vertices that form the corners of that face.
        * **faces\_config** (*dict**[**str**,* *str* *|* *int* *|* *float* *|* *bool**]*) – Configuration for the polygons representing the faces of the polyhedron.
        * **graph\_config** (*dict**[**str**,* *str* *|* *int* *|* *float* *|* *bool**]*) – Configuration for the graph containing the vertices and edges of the polyhedron.

    Examples

    To understand how to create a custom polyhedra, let’s use the example of a rather simple one - a square pyramid.

    Example: SquarePyramidScene [¶](#squarepyramidscene)

    ![../_images/SquarePyramidScene-1.png](../_images/SquarePyramidScene-1.png)

    ```
    from manim import *

    class SquarePyramidScene(ThreeDScene):
        def construct(self):
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            vertex_coords = [
                [1, 1, 0],
                [1, -1, 0],
                [-1, -1, 0],
                [-1, 1, 0],
                [0, 0, 2]
            ]
            faces_list = [
                [0, 1, 4],
                [1, 2, 4],
                [2, 3, 4],
                [3, 0, 4],
                [0, 1, 2, 3]
            ]
            pyramid = Polyhedron(vertex_coords, faces_list)
            self.add(pyramid)

    ```

    ```

    class SquarePyramidScene(ThreeDScene):
        def construct(self):
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            vertex_coords = [
                [1, 1, 0],
                [1, -1, 0],
                [-1, -1, 0],
                [-1, 1, 0],
                [0, 0, 2]
            ]
            faces_list = [
                [0, 1, 4],
                [1, 2, 4],
                [2, 3, 4],
                [3, 0, 4],
                [0, 1, 2, 3]
            ]
            pyramid = Polyhedron(vertex_coords, faces_list)
            self.add(pyramid)


    ```

    In defining the polyhedron above, we first defined the coordinates of the vertices.
    These are the corners of the square base, given as the first four coordinates in the vertex list,
    and the apex, the last coordinate in the list.

    Next, we define the faces of the polyhedron. The triangular surfaces of the pyramid are polygons
    with two adjacent vertices in the base and the vertex at the apex as corners. We thus define these
    surfaces in the first four elements of our face list. The last element defines the base of the pyramid.

    The graph and faces of polyhedra can also be accessed and modified directly, after instantiation.
    They are stored in the graph and faces attributes respectively.

    Example: PolyhedronSubMobjects [¶](#polyhedronsubmobjects)

    ![../_images/PolyhedronSubMobjects-1.png](../_images/PolyhedronSubMobjects-1.png)

    ```
    from manim import *

    class PolyhedronSubMobjects(ThreeDScene):
        def construct(self):
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            octahedron = Octahedron(edge_length = 3)
            octahedron.graph[0].set_color(RED)
            octahedron.faces[2].set_color(YELLOW)
            self.add(octahedron)

    ```

    ```

    class PolyhedronSubMobjects(ThreeDScene):
        def construct(self):
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            octahedron = Octahedron(edge_length = 3)
            octahedron.graph[0].set_color(RED)
            octahedron.faces[2].set_color(YELLOW)
            self.add(octahedron)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`create_faces`](#manim.mobject.three_d.polyhedra.Polyhedron.create_faces "manim.mobject.three_d.polyhedra.Polyhedron.create_faces") | Creates VGroup of faces from a list of face coordinates. |
    | [`extract_face_coords`](#manim.mobject.three_d.polyhedra.Polyhedron.extract_face_coords "manim.mobject.three_d.polyhedra.Polyhedron.extract_face_coords") | Extracts the coordinates of the vertices in the graph. |
    | [`get_edges`](#manim.mobject.three_d.polyhedra.Polyhedron.get_edges "manim.mobject.three_d.polyhedra.Polyhedron.get_edges") | Creates list of cyclic pairwise tuples. |
    | `update_faces` |  |

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

    \_original\_\_init\_\_(*vertex\_coords*, *faces\_list*, *faces\_config={}*, *graph\_config={}*)[¶](#manim.mobject.three_d.polyhedra.Polyhedron._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **vertex\_coords** (*list**[**list**[**float**]* *|* *ndarray**]*)
            * **faces\_list** (*list**[**list**[**int**]**]*)
            * **faces\_config** (*dict**[**str**,* *str* *|* *int* *|* *float* *|* *bool**]*)
            * **graph\_config** (*dict**[**str**,* *str* *|* *int* *|* *float* *|* *bool**]*)

    create\_faces(*face\_coords*)[[source]](../_modules/manim/mobject/three_d/polyhedra.html#Polyhedron.create_faces)[¶](#manim.mobject.three_d.polyhedra.Polyhedron.create_faces "Link to this definition")
    :   Creates VGroup of faces from a list of face coordinates.

        Parameters:
        :   **face\_coords** (*list**[**list**[**list* *|* *ndarray**]**]*)

        Return type:
        :   [*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

    extract\_face\_coords()[[source]](../_modules/manim/mobject/three_d/polyhedra.html#Polyhedron.extract_face_coords)[¶](#manim.mobject.three_d.polyhedra.Polyhedron.extract_face_coords "Link to this definition")
    :   Extracts the coordinates of the vertices in the graph.
        Used for updating faces.

        Return type:
        :   list[list[*ndarray*]]

    get\_edges(*faces\_list*)[[source]](../_modules/manim/mobject/three_d/polyhedra.html#Polyhedron.get_edges)[¶](#manim.mobject.three_d.polyhedra.Polyhedron.get_edges "Link to this definition")
    :   Creates list of cyclic pairwise tuples.

        Parameters:
        :   **faces\_list** (*list**[**list**[**int**]**]*)

        Return type:
        :   list[tuple[int, int]]