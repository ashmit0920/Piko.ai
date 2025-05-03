# Source: https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

LinearTransformationScene[¶](#lineartransformationscene "Link to this heading")
===============================================================================

Qualified name: `manim.scene.vector\_space\_scene.LinearTransformationScene`

*class* LinearTransformationScene(*include\_background\_plane=True*, *include\_foreground\_plane=True*, *background\_plane\_kwargs=None*, *foreground\_plane\_kwargs=None*, *show\_coordinates=False*, *show\_basis\_vectors=True*, *basis\_vector\_stroke\_width=6*, *i\_hat\_color=ManimColor('#83C167')*, *j\_hat\_color=ManimColor('#FC6255')*, *leave\_ghost\_vectors=False*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene)[¶](#manim.scene.vector_space_scene.LinearTransformationScene "Link to this definition")
:   Bases: [`VectorScene`](manim.scene.vector_space_scene.VectorScene.html#manim.scene.vector_space_scene.VectorScene "manim.scene.vector_space_scene.VectorScene")

    This scene contains special methods that make it
    especially suitable for showing linear transformations.

    Parameters:
    :   * **include\_background\_plane** (*bool*) – Whether or not to include the background plane in the scene.
        * **include\_foreground\_plane** (*bool*) – Whether or not to include the foreground plane in the scene.
        * **background\_plane\_kwargs** (*dict* *|* *None*) – Parameters to be passed to `NumberPlane` to adjust the background plane.
        * **foreground\_plane\_kwargs** (*dict* *|* *None*) – Parameters to be passed to `NumberPlane` to adjust the foreground plane.
        * **show\_coordinates** (*bool*) – Whether or not to include the coordinates for the background plane.
        * **show\_basis\_vectors** (*bool*) – Whether to show the basis x\_axis -> `i_hat` and y\_axis -> `j_hat` vectors.
        * **basis\_vector\_stroke\_width** (*float*) – The `stroke_width` of the basis vectors.
        * **i\_hat\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the `i_hat` vector.
        * **j\_hat\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the `j_hat` vector.
        * **leave\_ghost\_vectors** (*bool*) – Indicates the previous position of the basis vectors following a transformation.

    Examples

    Example: LinearTransformationSceneExample [¶](#lineartransformationsceneexample)

    [
    ](./LinearTransformationSceneExample-1.mp4)

    ```
    from manim import *

    class LinearTransformationSceneExample(LinearTransformationScene):
        def __init__(self, **kwargs):
            LinearTransformationScene.__init__(
                self,
                show_coordinates=True,
                leave_ghost_vectors=True,
                **kwargs
            )

        def construct(self):
            matrix = [[1, 1], [0, 1]]
            self.apply_matrix(matrix)
            self.wait()

    ```

    ```

    class LinearTransformationSceneExample(LinearTransformationScene):
        def __init__(self, **kwargs):
            LinearTransformationScene.__init__(
                self,
                show_coordinates=True,
                leave_ghost_vectors=True,
                **kwargs
            )

        def construct(self):
            matrix = [[1, 1], [0, 1]]
            self.apply_matrix(matrix)
            self.wait()


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`add_background_mobject`](#manim.scene.vector_space_scene.LinearTransformationScene.add_background_mobject "manim.scene.vector_space_scene.LinearTransformationScene.add_background_mobject") | Adds the mobjects to the special list self.background\_mobjects. |
    | [`add_foreground_mobject`](#manim.scene.vector_space_scene.LinearTransformationScene.add_foreground_mobject "manim.scene.vector_space_scene.LinearTransformationScene.add_foreground_mobject") | Adds the mobjects to the special list self.foreground\_mobjects. |
    | [`add_moving_mobject`](#manim.scene.vector_space_scene.LinearTransformationScene.add_moving_mobject "manim.scene.vector_space_scene.LinearTransformationScene.add_moving_mobject") | Adds the mobject to the special list self.moving\_mobject, and adds a property to the mobject called mobject.target, which keeps track of what the mobject will move to or become etc. |
    | [`add_special_mobjects`](#manim.scene.vector_space_scene.LinearTransformationScene.add_special_mobjects "manim.scene.vector_space_scene.LinearTransformationScene.add_special_mobjects") | Adds mobjects to a separate list that can be tracked, if these mobjects have some extra importance. |
    | [`add_title`](#manim.scene.vector_space_scene.LinearTransformationScene.add_title "manim.scene.vector_space_scene.LinearTransformationScene.add_title") | Adds a title, after scaling it, adding a background rectangle, moving it to the top and adding it to foreground\_mobjects adding it as a local variable of self. |
    | [`add_transformable_label`](#manim.scene.vector_space_scene.LinearTransformationScene.add_transformable_label "manim.scene.vector_space_scene.LinearTransformationScene.add_transformable_label") | Method for creating, and animating the addition of a transformable label for the vector. |
    | [`add_transformable_mobject`](#manim.scene.vector_space_scene.LinearTransformationScene.add_transformable_mobject "manim.scene.vector_space_scene.LinearTransformationScene.add_transformable_mobject") | Adds the mobjects to the special list self.transformable\_mobjects. |
    | [`add_unit_square`](#manim.scene.vector_space_scene.LinearTransformationScene.add_unit_square "manim.scene.vector_space_scene.LinearTransformationScene.add_unit_square") | Adds a unit square to the scene via self.get\_unit\_square. |
    | [`add_vector`](#manim.scene.vector_space_scene.LinearTransformationScene.add_vector "manim.scene.vector_space_scene.LinearTransformationScene.add_vector") | Adds a vector to the scene, and puts it in the special list self.moving\_vectors. |
    | [`apply_function`](#manim.scene.vector_space_scene.LinearTransformationScene.apply_function "manim.scene.vector_space_scene.LinearTransformationScene.apply_function") | Applies the given function to each of the mobjects in self.transformable\_mobjects, and plays the animation showing this. |
    | [`apply_inverse`](#manim.scene.vector_space_scene.LinearTransformationScene.apply_inverse "manim.scene.vector_space_scene.LinearTransformationScene.apply_inverse") | This method applies the linear transformation represented by the inverse of the passed matrix to the number plane, and each vector/similar mobject on it. |
    | [`apply_inverse_transpose`](#manim.scene.vector_space_scene.LinearTransformationScene.apply_inverse_transpose "manim.scene.vector_space_scene.LinearTransformationScene.apply_inverse_transpose") | Applies the inverse of the transformation represented by the given transposed matrix to the number plane and each vector/similar mobject on it. |
    | [`apply_matrix`](#manim.scene.vector_space_scene.LinearTransformationScene.apply_matrix "manim.scene.vector_space_scene.LinearTransformationScene.apply_matrix") | Applies the transformation represented by the given matrix to the number plane, and each vector/similar mobject on it. |
    | [`apply_nonlinear_transformation`](#manim.scene.vector_space_scene.LinearTransformationScene.apply_nonlinear_transformation "manim.scene.vector_space_scene.LinearTransformationScene.apply_nonlinear_transformation") | Applies the non-linear transformation represented by the given function to the number plane and each vector/similar mobject on it. |
    | [`apply_transposed_matrix`](#manim.scene.vector_space_scene.LinearTransformationScene.apply_transposed_matrix "manim.scene.vector_space_scene.LinearTransformationScene.apply_transposed_matrix") | Applies the transformation represented by the given transposed matrix to the number plane, and each vector/similar mobject on it. |
    | [`get_ghost_vectors`](#manim.scene.vector_space_scene.LinearTransformationScene.get_ghost_vectors "manim.scene.vector_space_scene.LinearTransformationScene.get_ghost_vectors") | Returns all ghost vectors ever added to `self`. |
    | [`get_matrix_transformation`](#manim.scene.vector_space_scene.LinearTransformationScene.get_matrix_transformation "manim.scene.vector_space_scene.LinearTransformationScene.get_matrix_transformation") | Returns a function corresponding to the linear transformation represented by the matrix passed. |
    | [`get_moving_mobject_movement`](#manim.scene.vector_space_scene.LinearTransformationScene.get_moving_mobject_movement "manim.scene.vector_space_scene.LinearTransformationScene.get_moving_mobject_movement") | This method returns an animation that moves a mobject in "self.moving\_mobjects" to its corresponding .target value. |
    | [`get_piece_movement`](#manim.scene.vector_space_scene.LinearTransformationScene.get_piece_movement "manim.scene.vector_space_scene.LinearTransformationScene.get_piece_movement") | This method returns an animation that moves an arbitrary mobject in "pieces" to its corresponding .target value. |
    | [`get_transformable_label_movement`](#manim.scene.vector_space_scene.LinearTransformationScene.get_transformable_label_movement "manim.scene.vector_space_scene.LinearTransformationScene.get_transformable_label_movement") | This method returns an animation that moves all labels in "self.transformable\_labels" to its corresponding .target . |
    | [`get_transposed_matrix_transformation`](#manim.scene.vector_space_scene.LinearTransformationScene.get_transposed_matrix_transformation "manim.scene.vector_space_scene.LinearTransformationScene.get_transposed_matrix_transformation") | Returns a function corresponding to the linear transformation represented by the transposed matrix passed. |
    | [`get_unit_square`](#manim.scene.vector_space_scene.LinearTransformationScene.get_unit_square "manim.scene.vector_space_scene.LinearTransformationScene.get_unit_square") | Returns a unit square for the current NumberPlane. |
    | [`get_vector_movement`](#manim.scene.vector_space_scene.LinearTransformationScene.get_vector_movement "manim.scene.vector_space_scene.LinearTransformationScene.get_vector_movement") | This method returns an animation that moves a mobject in "self.moving\_vectors" to its corresponding .target value. |
    | [`setup`](#manim.scene.vector_space_scene.LinearTransformationScene.setup "manim.scene.vector_space_scene.LinearTransformationScene.setup") | This is meant to be implemented by any scenes which are commonly subclassed, and have some common setup involved before the construct method is called. |
    | `update_default_configs` |  |
    | [`write_vector_coordinates`](#manim.scene.vector_space_scene.LinearTransformationScene.write_vector_coordinates "manim.scene.vector_space_scene.LinearTransformationScene.write_vector_coordinates") | Returns a column matrix indicating the vector coordinates, after writing them to the screen, and adding them to the special list self.foreground\_mobjects |

    Attributes

    |  |  |
    | --- | --- |
    | `camera` |  |
    | `time` | The time since the start of the scene. |

    add\_background\_mobject(*\*mobjects*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_background_mobject)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.add_background_mobject "Link to this definition")
    :   Adds the mobjects to the special list
        self.background\_mobjects.

        Parameters:
        :   **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to add to the list.

    add\_foreground\_mobject(*\*mobjects*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_foreground_mobject)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.add_foreground_mobject "Link to this definition")
    :   Adds the mobjects to the special list
        self.foreground\_mobjects.

        Parameters:
        :   **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to add to the list

    add\_moving\_mobject(*mobject*, *target\_mobject=None*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_moving_mobject)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.add_moving_mobject "Link to this definition")
    :   Adds the mobject to the special list
        self.moving\_mobject, and adds a property
        to the mobject called mobject.target, which
        keeps track of what the mobject will move to
        or become etc.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to add to the list
            * **target\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *|* *None*) – What the moving\_mobject goes to, etc.

    add\_special\_mobjects(*mob\_list*, *\*mobs\_to\_add*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_special_mobjects)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.add_special_mobjects "Link to this definition")
    :   Adds mobjects to a separate list that can be tracked,
        if these mobjects have some extra importance.

        Parameters:
        :   * **mob\_list** (*list*) – The special list to which you want to add
              these mobjects.
            * **\*mobs\_to\_add** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to add.

    add\_title(*title*, *scale\_factor=1.5*, *animate=False*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_title)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.add_title "Link to this definition")
    :   Adds a title, after scaling it, adding a background rectangle,
        moving it to the top and adding it to foreground\_mobjects adding
        it as a local variable of self. Returns the Scene.

        Parameters:
        :   * **title** (*str* *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex")) – What the title should be.
            * **scale\_factor** (*float*) – How much the title should be scaled by.
            * **animate** (*bool*) – Whether or not to animate the addition.

        Returns:
        :   The scene with the title added to it.

        Return type:
        :   [LinearTransformationScene](#manim.scene.vector_space_scene.LinearTransformationScene "manim.scene.vector_space_scene.LinearTransformationScene")

    add\_transformable\_label(*vector*, *label*, *transformation\_name='L'*, *new\_label=None*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_transformable_label)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.add_transformable_label "Link to this definition")
    :   Method for creating, and animating the addition of
        a transformable label for the vector.

        Parameters:
        :   * **vector** ([*Vector*](manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector "manim.mobject.geometry.line.Vector")) – The vector for which the label must be added.
            * **label** ([*MathTex*](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") *|* *str*) – The MathTex/string of the label.
            * **transformation\_name** (*str* *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex")) – The name to give the transformation as a label.
            * **new\_label** (*str* *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") *|* *None*) – What the label should display after a Linear Transformation
            * **\*\*kwargs** – Any valid keyword argument of get\_vector\_label

        Returns:
        :   The MathTex of the label.

        Return type:
        :   [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex")

    add\_transformable\_mobject(*\*mobjects*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_transformable_mobject)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.add_transformable_mobject "Link to this definition")
    :   Adds the mobjects to the special list
        self.transformable\_mobjects.

        Parameters:
        :   **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to add to the list.

    add\_unit\_square(*animate=False*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_unit_square)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.add_unit_square "Link to this definition")
    :   Adds a unit square to the scene via
        self.get\_unit\_square.

        Parameters:
        :   * **animate** (*bool*) – Whether or not to animate the addition
              with DrawBorderThenFill.
            * **\*\*kwargs** – Any valid keyword arguments of
              self.get\_unit\_square()

        Returns:
        :   The unit square.

        Return type:
        :   [Square](manim.mobject.geometry.polygram.Square.html#manim.mobject.geometry.polygram.Square "manim.mobject.geometry.polygram.Square")

    add\_vector(*vector*, *color=ManimColor('#FFFF00')*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_vector)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.add_vector "Link to this definition")
    :   Adds a vector to the scene, and puts it in the special
        list self.moving\_vectors.

        Parameters:
        :   * **vector** ([*Arrow*](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow") *|* *list* *|* *tuple* *|* *ndarray*) – It can be a pre-made graphical vector, or the
              coordinates of one.
            * **color** (*str*) – The string of the hex color of the vector.
              This is only taken into consideration if
              ‘vector’ is not an Arrow. Defaults to YELLOW.
            * **\*\*kwargs** – Any valid keyword argument of VectorScene.add\_vector.

        Returns:
        :   The arrow representing the vector.

        Return type:
        :   [Arrow](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")

    apply\_function(*function*, *added\_anims=[]*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.apply_function)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.apply_function "Link to this definition")
    :   Applies the given function to each of the mobjects in
        self.transformable\_mobjects, and plays the animation showing
        this.

        Parameters:
        :   * **function** (*Callable**[**[**ndarray**]**,* *ndarray**]*) – The function that affects each point
              of each mobject in self.transformable\_mobjects.
            * **added\_anims** (*list*) – Any other animations that need to be played
              simultaneously with this.
            * **\*\*kwargs** – Any valid keyword argument of a self.play() call.

    apply\_inverse(*matrix*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.apply_inverse)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.apply_inverse "Link to this definition")
    :   This method applies the linear transformation
        represented by the inverse of the passed matrix
        to the number plane, and each vector/similar mobject on it.

        Parameters:
        :   * **matrix** (*ndarray* *|* *list* *|* *tuple*) – The matrix whose inverse is to be applied.
            * **\*\*kwargs** – Any valid keyword argument of self.apply\_matrix()

    apply\_inverse\_transpose(*t\_matrix*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.apply_inverse_transpose)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.apply_inverse_transpose "Link to this definition")
    :   Applies the inverse of the transformation represented
        by the given transposed matrix to the number plane and each
        vector/similar mobject on it.

        Parameters:
        :   * **t\_matrix** (*ndarray* *|* *list* *|* *tuple*) – The matrix.
            * **\*\*kwargs** – Any valid keyword argument of self.apply\_transposed\_matrix()

    apply\_matrix(*matrix*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.apply_matrix)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.apply_matrix "Link to this definition")
    :   Applies the transformation represented by the
        given matrix to the number plane, and each vector/similar
        mobject on it.

        Parameters:
        :   * **matrix** (*ndarray* *|* *list* *|* *tuple*) – The matrix.
            * **\*\*kwargs** – Any valid keyword argument of self.apply\_transposed\_matrix()

    apply\_nonlinear\_transformation(*function*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.apply_nonlinear_transformation)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.apply_nonlinear_transformation "Link to this definition")
    :   Applies the non-linear transformation represented
        by the given function to the number plane and each
        vector/similar mobject on it.

        Parameters:
        :   * **function** (*Callable**[**[**ndarray**]**,* *ndarray**]*) – The function.
            * **\*\*kwargs** – Any valid keyword argument of self.apply\_function()

    apply\_transposed\_matrix(*transposed\_matrix*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.apply_transposed_matrix)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.apply_transposed_matrix "Link to this definition")
    :   Applies the transformation represented by the
        given transposed matrix to the number plane,
        and each vector/similar mobject on it.

        Parameters:
        :   * **transposed\_matrix** (*ndarray* *|* *list* *|* *tuple*) – The matrix.
            * **\*\*kwargs** – Any valid keyword argument of self.apply\_function()

    get\_ghost\_vectors()[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.get_ghost_vectors)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.get_ghost_vectors "Link to this definition")
    :   Returns all ghost vectors ever added to `self`. Each element is a `VGroup` of
        two ghost vectors.

        Return type:
        :   [*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

    get\_matrix\_transformation(*matrix*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.get_matrix_transformation)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.get_matrix_transformation "Link to this definition")
    :   Returns a function corresponding to the linear
        transformation represented by the matrix passed.

        Parameters:
        :   **matrix** (*ndarray* *|* *list* *|* *tuple*) – The matrix.

    get\_moving\_mobject\_movement(*func*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.get_moving_mobject_movement)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.get_moving_mobject_movement "Link to this definition")
    :   This method returns an animation that moves a mobject
        in “self.moving\_mobjects” to its corresponding .target value.
        func is a function that determines where the .target goes.

        Parameters:
        :   **func** (*Callable**[**[**ndarray**]**,* *ndarray**]*) – The function that determines where the .target of
            the moving mobject goes.

        Returns:
        :   The animation of the movement.

        Return type:
        :   [Animation](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    get\_piece\_movement(*pieces*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.get_piece_movement)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.get_piece_movement "Link to this definition")
    :   This method returns an animation that moves an arbitrary
        mobject in “pieces” to its corresponding .target value.
        If self.leave\_ghost\_vectors is True, ghosts of the original
        positions/mobjects are left on screen

        Parameters:
        :   **pieces** (*list* *|* *tuple* *|* *ndarray*) – The pieces for which the movement must be shown.

        Returns:
        :   The animation of the movement.

        Return type:
        :   [Animation](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    get\_transformable\_label\_movement()[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.get_transformable_label_movement)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.get_transformable_label_movement "Link to this definition")
    :   This method returns an animation that moves all labels
        in “self.transformable\_labels” to its corresponding .target .

        Returns:
        :   The animation of the movement.

        Return type:
        :   [Animation](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    get\_transposed\_matrix\_transformation(*transposed\_matrix*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.get_transposed_matrix_transformation)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.get_transposed_matrix_transformation "Link to this definition")
    :   Returns a function corresponding to the linear
        transformation represented by the transposed
        matrix passed.

        Parameters:
        :   **transposed\_matrix** (*ndarray* *|* *list* *|* *tuple*) – The matrix.

    get\_unit\_square(*color=ManimColor('#FFFF00')*, *opacity=0.3*, *stroke\_width=3*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.get_unit_square)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.get_unit_square "Link to this definition")
    :   Returns a unit square for the current NumberPlane.

        Parameters:
        :   * **color** (*str*) – The string of the hex color code of the color wanted.
            * **opacity** (*float*) – The opacity of the square
            * **stroke\_width** (*float*) – The stroke\_width in pixels of the border of the square

        Return type:
        :   [Square](manim.mobject.geometry.polygram.Square.html#manim.mobject.geometry.polygram.Square "manim.mobject.geometry.polygram.Square")

    get\_vector\_movement(*func*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.get_vector_movement)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.get_vector_movement "Link to this definition")
    :   This method returns an animation that moves a mobject
        in “self.moving\_vectors” to its corresponding .target value.
        func is a function that determines where the .target goes.

        Parameters:
        :   **func** (*Callable**[**[**ndarray**]**,* *ndarray**]*) – The function that determines where the .target of
            the moving mobject goes.

        Returns:
        :   The animation of the movement.

        Return type:
        :   [Animation](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    setup()[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.setup)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.setup "Link to this definition")
    :   This is meant to be implemented by any scenes which
        are commonly subclassed, and have some common setup
        involved before the construct method is called.

    write\_vector\_coordinates(*vector*, *\*\*kwargs*)[[source]](../_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.write_vector_coordinates)[¶](#manim.scene.vector_space_scene.LinearTransformationScene.write_vector_coordinates "Link to this definition")
    :   Returns a column matrix indicating the vector coordinates,
        after writing them to the screen, and adding them to the
        special list self.foreground\_mobjects

        Parameters:
        :   * **vector** ([*Arrow*](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")) – The arrow representing the vector.
            * **\*\*kwargs** – Any valid keyword arguments of VectorScene.write\_vector\_coordinates

        Returns:
        :   The column matrix representing the vector.

        Return type:
        :   [Matrix](manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")