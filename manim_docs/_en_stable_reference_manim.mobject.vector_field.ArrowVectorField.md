# Source: https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.ArrowVectorField.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ArrowVectorField[¶](#arrowvectorfield "Link to this heading")
=============================================================

Qualified name: `manim.mobject.vector\_field.ArrowVectorField`

*class* ArrowVectorField(*func, color=None, color\_scheme=None, min\_color\_scheme\_value=0, max\_color\_scheme\_value=2, colors=[ManimColor('#236B8E'), ManimColor('#83C167'), ManimColor('#FFFF00'), ManimColor('#FC6255')], x\_range=None, y\_range=None, z\_range=None, three\_dimensions=False, length\_func=<function ArrowVectorField.<lambda>>, opacity=1.0, vector\_config=None, \*\*kwargs*)[[source]](../_modules/manim/mobject/vector_field.html#ArrowVectorField)[¶](#manim.mobject.vector_field.ArrowVectorField "Link to this definition")
:   Bases: [`VectorField`](manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField")

    A [`VectorField`](manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField") represented by a set of change vectors.

    Vector fields are always based on a function defining the [`Vector`](manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector "manim.mobject.geometry.line.Vector") at every position.
    The values of this functions is displayed as a grid of vectors.
    By default the color of each vector is determined by it’s magnitude.
    Other color schemes can be used however.

    Parameters:
    :   * **func** (*Callable**[**[**np.ndarray**]**,* *np.ndarray**]*) – The function defining the rate of change at every position of the vector field.
        * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *|* *None*) – The color of the vector field. If set, position-specific coloring is disabled.
        * **color\_scheme** (*Callable**[**[**np.ndarray**]**,* *float**]* *|* *None*) – A function mapping a vector to a single value. This value gives the position in the color gradient defined using min\_color\_scheme\_value, max\_color\_scheme\_value and colors.
        * **min\_color\_scheme\_value** (*float*) – The value of the color\_scheme function to be mapped to the first color in colors. Lower values also result in the first color of the gradient.
        * **max\_color\_scheme\_value** (*float*) – The value of the color\_scheme function to be mapped to the last color in colors. Higher values also result in the last color of the gradient.
        * **colors** (*Sequence**[*[*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")*]*) – The colors defining the color gradient of the vector field.
        * **x\_range** (*Sequence**[**float**]*) – A sequence of x\_min, x\_max, delta\_x
        * **y\_range** (*Sequence**[**float**]*) – A sequence of y\_min, y\_max, delta\_y
        * **z\_range** (*Sequence**[**float**]*) – A sequence of z\_min, z\_max, delta\_z
        * **three\_dimensions** (*bool*) – Enables three\_dimensions. Default set to False, automatically turns True if
          z\_range is not None.
        * **length\_func** (*Callable**[**[**float**]**,* *float**]*) – The function determining the displayed size of the vectors. The actual size
          of the vector is passed, the returned value will be used as display size for the
          vector. By default this is used to cap the displayed size of vectors to reduce the clutter.
        * **opacity** (*float*) – The opacity of the arrows.
        * **vector\_config** (*dict* *|* *None*) – Additional arguments to be passed to the [`Vector`](manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector "manim.mobject.geometry.line.Vector") constructor
        * **kwargs** – Additional arguments to be passed to the [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") constructor

    Examples

    Example: BasicUsage [¶](#basicusage)

    ![../_images/BasicUsage-1.png](../_images/BasicUsage-1.png)

    ```
    from manim import *

    class BasicUsage(Scene):
        def construct(self):
            func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
            self.add(ArrowVectorField(func))

    ```

    ```

    class BasicUsage(Scene):
        def construct(self):
            func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
            self.add(ArrowVectorField(func))


    ```

    Example: SizingAndSpacing [¶](#sizingandspacing)

    [
    ](./SizingAndSpacing-1.mp4)

    ```
    from manim import *

    class SizingAndSpacing(Scene):
        def construct(self):
            func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
            vf = ArrowVectorField(func, x_range=[-7, 7, 1])
            self.add(vf)
            self.wait()

            length_func = lambda x: x / 3
            vf2 = ArrowVectorField(func, x_range=[-7, 7, 1], length_func=length_func)
            self.play(vf.animate.become(vf2))
            self.wait()

    ```

    ```

    class SizingAndSpacing(Scene):
        def construct(self):
            func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
            vf = ArrowVectorField(func, x_range=[-7, 7, 1])
            self.add(vf)
            self.wait()

            length_func = lambda x: x / 3
            vf2 = ArrowVectorField(func, x_range=[-7, 7, 1], length_func=length_func)
            self.play(vf.animate.become(vf2))
            self.wait()


    ```

    Example: Coloring [¶](#coloring)

    ![../_images/Coloring-1.png](../_images/Coloring-1.png)

    ```
    from manim import *

    class Coloring(Scene):
        def construct(self):
            func = lambda pos: pos - LEFT * 5
            colors = [RED, YELLOW, BLUE, DARK_GRAY]
            min_radius = Circle(radius=2, color=colors[0]).shift(LEFT * 5)
            max_radius = Circle(radius=10, color=colors[-1]).shift(LEFT * 5)
            vf = ArrowVectorField(
                func, min_color_scheme_value=2, max_color_scheme_value=10, colors=colors
            )
            self.add(vf, min_radius, max_radius)

    ```

    ```

    class Coloring(Scene):
        def construct(self):
            func = lambda pos: pos - LEFT * 5
            colors = [RED, YELLOW, BLUE, DARK_GRAY]
            min_radius = Circle(radius=2, color=colors[0]).shift(LEFT * 5)
            max_radius = Circle(radius=10, color=colors[-1]).shift(LEFT * 5)
            vf = ArrowVectorField(
                func, min_color_scheme_value=2, max_color_scheme_value=10, colors=colors
            )
            self.add(vf, min_radius, max_radius)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`get_vector`](#manim.mobject.vector_field.ArrowVectorField.get_vector "manim.mobject.vector_field.ArrowVectorField.get_vector") | Creates a vector in the vector field. |

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

    \_original\_\_init\_\_(*func, color=None, color\_scheme=None, min\_color\_scheme\_value=0, max\_color\_scheme\_value=2, colors=[ManimColor('#236B8E'), ManimColor('#83C167'), ManimColor('#FFFF00'), ManimColor('#FC6255')], x\_range=None, y\_range=None, z\_range=None, three\_dimensions=False, length\_func=<function ArrowVectorField.<lambda>>, opacity=1.0, vector\_config=None, \*\*kwargs*)[¶](#manim.mobject.vector_field.ArrowVectorField._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **func** (*Callable**[**[**np.ndarray**]**,* *np.ndarray**]*)
            * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *|* *None*)
            * **color\_scheme** (*Callable**[**[**np.ndarray**]**,* *float**]* *|* *None*)
            * **min\_color\_scheme\_value** (*float*)
            * **max\_color\_scheme\_value** (*float*)
            * **colors** (*Sequence**[*[*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")*]*)
            * **x\_range** (*Sequence**[**float**]*)
            * **y\_range** (*Sequence**[**float**]*)
            * **z\_range** (*Sequence**[**float**]*)
            * **three\_dimensions** (*bool*)
            * **length\_func** (*Callable**[**[**float**]**,* *float**]*)
            * **opacity** (*float*)
            * **vector\_config** (*dict* *|* *None*)

    get\_vector(*point*)[[source]](../_modules/manim/mobject/vector_field.html#ArrowVectorField.get_vector)[¶](#manim.mobject.vector_field.ArrowVectorField.get_vector "Link to this definition")
    :   Creates a vector in the vector field.

        The created vector is based on the function of the vector field and is
        rooted in the given point. Color and length fit the specifications of
        this vector field.

        Parameters:
        :   **point** (*ndarray*) – The root point of the vector.