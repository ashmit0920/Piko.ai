# Source: https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.VectorScene.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

VectorScene[¶](#vectorscene "Link to this heading")
===================================================

Qualified name: `manim.scene.vector\_space\_scene.VectorScene`

*class* VectorScene(*basis\_vector\_stroke\_width=6*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#VectorScene)[¶](#manim.scene.vector_space_scene.VectorScene "Link to this definition")
:   Bases: [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")

    Methods

    |  |  |
    | --- | --- |
    | [`add_axes`](#manim.scene.vector_space_scene.VectorScene.add_axes "manim.scene.vector_space_scene.VectorScene.add_axes") | Adds a pair of Axes to the Scene. |
    | [`add_plane`](#manim.scene.vector_space_scene.VectorScene.add_plane "manim.scene.vector_space_scene.VectorScene.add_plane") | Adds a NumberPlane object to the background. |
    | [`add_vector`](#manim.scene.vector_space_scene.VectorScene.add_vector "manim.scene.vector_space_scene.VectorScene.add_vector") | Returns the Vector after adding it to the Plane. |
    | [`coords_to_vector`](#manim.scene.vector_space_scene.VectorScene.coords_to_vector "manim.scene.vector_space_scene.VectorScene.coords_to_vector") | This method writes the vector as a column matrix (henceforth called the label), takes the values in it one by one, and form the corresponding lines that make up the x and y components of the vector. |
    | [`get_basis_vector_labels`](#manim.scene.vector_space_scene.VectorScene.get_basis_vector_labels "manim.scene.vector_space_scene.VectorScene.get_basis_vector_labels") | Returns naming labels for the basis vectors. |
    | [`get_basis_vectors`](#manim.scene.vector_space_scene.VectorScene.get_basis_vectors "manim.scene.vector_space_scene.VectorScene.get_basis_vectors") | Returns a VGroup of the Basis Vectors (1,0) and (0,1) |
    | [`get_vector`](#manim.scene.vector_space_scene.VectorScene.get_vector "manim.scene.vector_space_scene.VectorScene.get_vector") | Returns an arrow on the Plane given an input numerical vector. |
    | [`get_vector_label`](#manim.scene.vector_space_scene.VectorScene.get_vector_label "manim.scene.vector_space_scene.VectorScene.get_vector_label") | Returns naming labels for the passed vector. |
    | [`label_vector`](#manim.scene.vector_space_scene.VectorScene.label_vector "manim.scene.vector_space_scene.VectorScene.label_vector") | Shortcut method for creating, and animating the addition of a label for the vector. |
    | [`lock_in_faded_grid`](#manim.scene.vector_space_scene.VectorScene.lock_in_faded_grid "manim.scene.vector_space_scene.VectorScene.lock_in_faded_grid") | This method freezes the NumberPlane and Axes that were already in the background, and adds new, manipulatable ones to the foreground. |
    | `position_x_coordinate` |  |
    | `position_y_coordinate` |  |
    | [`show_ghost_movement`](#manim.scene.vector_space_scene.VectorScene.show_ghost_movement "manim.scene.vector_space_scene.VectorScene.show_ghost_movement") | This method plays an animation that partially shows the entire plane moving in the direction of a particular vector. |
    | [`vector_to_coords`](#manim.scene.vector_space_scene.VectorScene.vector_to_coords "manim.scene.vector_space_scene.VectorScene.vector_to_coords") | This method displays vector as a Vector() based vector, and then shows the corresponding lines that make up the x and y components of the vector. |
    | [`write_vector_coordinates`](#manim.scene.vector_space_scene.VectorScene.write_vector_coordinates "manim.scene.vector_space_scene.VectorScene.write_vector_coordinates") | Returns a column matrix indicating the vector coordinates, after writing them to the screen. |

    Attributes

    |  |  |
    | --- | --- |
    | `camera` |  |
    | `time` | The time since the start of the scene. |

    add\_axes(*animate=False*, *color=ManimColor('#FFFFFF')*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#VectorScene.add_axes)[¶](#manim.scene.vector_space_scene.VectorScene.add_axes "Link to this definition")
    :   Adds a pair of Axes to the Scene.

        Parameters:
        :   * **animate** (*bool*) – Whether or not to animate the addition of the axes through Create.
            * **color** (*bool*) – The color of the axes. Defaults to WHITE.

    add\_plane(*animate=False*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#VectorScene.add_plane)[¶](#manim.scene.vector_space_scene.VectorScene.add_plane "Link to this definition")
    :   Adds a NumberPlane object to the background.

        Parameters:
        :   * **animate** (*bool*) – Whether or not to animate the addition of the plane via Create.
            * **\*\*kwargs** – Any valid keyword arguments accepted by NumberPlane.

        Returns:
        :   The NumberPlane object.

        Return type:
        :   [NumberPlane](manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane "manim.mobject.graphing.coordinate_systems.NumberPlane")

    add\_vector(*vector*, *color=ManimColor('#FFFF00')*, *animate=True*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#VectorScene.add_vector)[¶](#manim.scene.vector_space_scene.VectorScene.add_vector "Link to this definition")
    :   Returns the Vector after adding it to the Plane.

        Parameters:
        :   * **vector** ([*Arrow*](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow") *|* *list* *|* *tuple* *|* *ndarray*) – It can be a pre-made graphical vector, or the
              coordinates of one.
            * **color** (*str*) – The string of the hex color of the vector.
              This is only taken into consideration if
              ‘vector’ is not an Arrow. Defaults to YELLOW.
            * **animate** (*bool*) – Whether or not to animate the addition of the vector
              by using GrowArrow
            * **\*\*kwargs** – Any valid keyword argument of Arrow.
              These are only considered if vector is not
              an Arrow.

        Returns:
        :   The arrow representing the vector.

        Return type:
        :   [Arrow](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")

    coords\_to\_vector(*vector*, *coords\_start=array([2., 2., 0.])*, *clean\_up=True*)[[source]](../_modules/manim/scene/vector_space_scene.html#VectorScene.coords_to_vector)[¶](#manim.scene.vector_space_scene.VectorScene.coords_to_vector "Link to this definition")
    :   This method writes the vector as a column matrix (henceforth called the label),
        takes the values in it one by one, and form the corresponding
        lines that make up the x and y components of the vector. Then, an
        Vector() based vector is created between the lines on the Screen.

        Parameters:
        :   * **vector** (*ndarray* *|* *list* *|* *tuple*) – The vector to show.
            * **coords\_start** (*ndarray* *|* *list* *|* *tuple*) – The starting point of the location of
              the label of the vector that shows it
              numerically.
              Defaults to 2 \* RIGHT + 2 \* UP or (2,2)
            * **clean\_up** (*bool*) – Whether or not to remove whatever
              this method did after it’s done.

    get\_basis\_vector\_labels(*\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#VectorScene.get_basis_vector_labels)[¶](#manim.scene.vector_space_scene.VectorScene.get_basis_vector_labels "Link to this definition")
    :   Returns naming labels for the basis vectors.

        Parameters:
        :   **\*\*kwargs** –

            Any valid keyword arguments of get\_vector\_label:
            :   vector,
                label (str,MathTex)
                at\_tip (bool=False),
                direction (str=”left”),
                rotate (bool),
                color (str),
                label\_scale\_factor=VECTOR\_LABEL\_SCALE\_FACTOR (int, float),

    get\_basis\_vectors(*i\_hat\_color=ManimColor('#83C167')*, *j\_hat\_color=ManimColor('#FC6255')*)[[source]](../_modules/manim/scene/vector_space_scene.html#VectorScene.get_basis_vectors)[¶](#manim.scene.vector_space_scene.VectorScene.get_basis_vectors "Link to this definition")
    :   Returns a VGroup of the Basis Vectors (1,0) and (0,1)

        Parameters:
        :   * **i\_hat\_color** (*str*) – The hex colour to use for the basis vector in the x direction
            * **j\_hat\_color** (*str*) – The hex colour to use for the basis vector in the y direction

        Returns:
        :   VGroup of the Vector Mobjects representing the basis vectors.

        Return type:
        :   [VGroup](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

    get\_vector(*numerical\_vector*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#VectorScene.get_vector)[¶](#manim.scene.vector_space_scene.VectorScene.get_vector "Link to this definition")
    :   Returns an arrow on the Plane given an input numerical vector.

        Parameters:
        :   * **numerical\_vector** (*ndarray* *|* *list* *|* *tuple*) – The Vector to plot.
            * **\*\*kwargs** – Any valid keyword argument of Arrow.

        Returns:
        :   The Arrow representing the Vector.

        Return type:
        :   [Arrow](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")

    get\_vector\_label(*vector*, *label*, *at\_tip=False*, *direction='left'*, *rotate=False*, *color=None*, *label\_scale\_factor=0.8*)[[source]](../_modules/manim/scene/vector_space_scene.html#VectorScene.get_vector_label)[¶](#manim.scene.vector_space_scene.VectorScene.get_vector_label "Link to this definition")
    :   Returns naming labels for the passed vector.

        Parameters:
        :   * **vector** ([*Vector*](manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector "manim.mobject.geometry.line.Vector")) – Vector Object for which to get the label.
            * **at\_tip** (*bool*) – Whether or not to place the label at the tip of the vector.
            * **direction** (*str*) – If the label should be on the “left” or right of the vector.
            * **rotate** (*bool*) – Whether or not to rotate it to align it with the vector.
            * **color** (*str* *|* *None*) – The color to give the label.
            * **label\_scale\_factor** (*float*) – How much to scale the label by.

        Returns:
        :   The MathTex of the label.

        Return type:
        :   [MathTex](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex")

    label\_vector(*vector*, *label*, *animate=True*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#VectorScene.label_vector)[¶](#manim.scene.vector_space_scene.VectorScene.label_vector "Link to this definition")
    :   Shortcut method for creating, and animating the addition of
        a label for the vector.

        Parameters:
        :   * **vector** ([*Vector*](manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector "manim.mobject.geometry.line.Vector")) – The vector for which the label must be added.
            * **label** ([*MathTex*](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") *|* *str*) – The MathTex/string of the label.
            * **animate** (*bool*) – Whether or not to animate the labelling w/ Write
            * **\*\*kwargs** – Any valid keyword argument of get\_vector\_label

        Returns:
        :   The MathTex of the label.

        Return type:
        :   [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex")

    lock\_in\_faded\_grid(*dimness=0.7*, *axes\_dimness=0.5*)[[source]](../_modules/manim/scene/vector_space_scene.html#VectorScene.lock_in_faded_grid)[¶](#manim.scene.vector_space_scene.VectorScene.lock_in_faded_grid "Link to this definition")
    :   This method freezes the NumberPlane and Axes that were already
        in the background, and adds new, manipulatable ones to the foreground.

        Parameters:
        :   * **dimness** (*float*) – The required dimness of the NumberPlane
            * **axes\_dimness** (*float*) – The required dimness of the Axes.

    show\_ghost\_movement(*vector*)[[source]](../_modules/manim/scene/vector_space_scene.html#VectorScene.show_ghost_movement)[¶](#manim.scene.vector_space_scene.VectorScene.show_ghost_movement "Link to this definition")
    :   This method plays an animation that partially shows the entire plane moving
        in the direction of a particular vector. This is useful when you wish to
        convey the idea of mentally moving the entire plane in a direction, without
        actually moving the plane.

        Parameters:
        :   **vector** ([*Arrow*](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow") *|* *list* *|* *tuple* *|* *ndarray*) – The vector which indicates the direction of movement.

    vector\_to\_coords(*vector*, *integer\_labels=True*, *clean\_up=True*)[[source]](../_modules/manim/scene/vector_space_scene.html#VectorScene.vector_to_coords)[¶](#manim.scene.vector_space_scene.VectorScene.vector_to_coords "Link to this definition")
    :   This method displays vector as a Vector() based vector, and then shows
        the corresponding lines that make up the x and y components of the vector.
        Then, a column matrix (henceforth called the label) is created near the
        head of the Vector.

        Parameters:
        :   * **vector** (*ndarray* *|* *list* *|* *tuple*) – The vector to show.
            * **integer\_labels** (*bool*) – Whether or not to round the value displayed.
              in the vector’s label to the nearest integer
            * **clean\_up** (*bool*) – Whether or not to remove whatever
              this method did after it’s done.

    write\_vector\_coordinates(*vector*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#VectorScene.write_vector_coordinates)[¶](#manim.scene.vector_space_scene.VectorScene.write_vector_coordinates "Link to this definition")
    :   Returns a column matrix indicating the vector coordinates,
        after writing them to the screen.

        Parameters:
        :   * **vector** ([*Arrow*](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")) – The arrow representing the vector.
            * **\*\*kwargs** – Any valid keyword arguments of [`coordinate_label()`](manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector.coordinate_label "manim.mobject.geometry.line.Vector.coordinate_label"):

        Returns:
        :   The column matrix representing the vector.

        Return type:
        :   [`Matrix`](manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")