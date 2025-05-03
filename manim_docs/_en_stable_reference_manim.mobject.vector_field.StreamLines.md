# Source: https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

StreamLines[¶](#streamlines "Link to this heading")
===================================================

Qualified name: `manim.mobject.vector\_field.StreamLines`

*class* StreamLines(*func*, *color=None*, *color\_scheme=None*, *min\_color\_scheme\_value=0*, *max\_color\_scheme\_value=2*, *colors=[ManimColor('#236B8E'), ManimColor('#83C167'), ManimColor('#FFFF00'), ManimColor('#FC6255')]*, *x\_range=None*, *y\_range=None*, *z\_range=None*, *three\_dimensions=False*, *noise\_factor=None*, *n\_repeats=1*, *dt=0.05*, *virtual\_time=3*, *max\_anchors\_per\_line=100*, *padding=3*, *stroke\_width=1*, *opacity=1*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/vector_field.html#StreamLines)[¶](#manim.mobject.vector_field.StreamLines "Link to this definition")
:   Bases: [`VectorField`](manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField")

    StreamLines represent the flow of a [`VectorField`](manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField") using the trace of moving agents.

    Vector fields are always based on a function defining the vector at every position.
    The values of this functions is displayed by moving many agents along the vector field
    and showing their trace.

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
        * **noise\_factor** (*float* *|* *None*) – The amount by which the starting position of each agent is altered along each axis. Defaults to `delta_y / 2` if not defined.
        * **n\_repeats** – The number of agents generated at each starting point.
        * **dt** – The factor by which the distance an agent moves per step is stretched. Lower values result in a better approximation of the trajectories in the vector field.
        * **virtual\_time** – The time the agents get to move in the vector field. Higher values therefore result in longer stream lines. However, this whole time gets simulated upon creation.
        * **max\_anchors\_per\_line** – The maximum number of anchors per line. Lines with more anchors get reduced in complexity, not in length.
        * **padding** – The distance agents can move out of the generation area before being terminated.
        * **stroke\_width** – The stroke with of the stream lines.
        * **opacity** – The opacity of the stream lines.

    Examples

    Example: BasicUsage [¶](#basicusage)

    ![../_images/BasicUsage-2.png](../_images/BasicUsage-2.png)

    ```
    from manim import *

    class BasicUsage(Scene):
        def construct(self):
            func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
            self.add(StreamLines(func))

    ```

    ```

    class BasicUsage(Scene):
        def construct(self):
            func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
            self.add(StreamLines(func))


    ```

    Example: SpawningAndFlowingArea [¶](#spawningandflowingarea)

    ![../_images/SpawningAndFlowingArea-1.png](../_images/SpawningAndFlowingArea-1.png)

    ```
    from manim import *

    class SpawningAndFlowingArea(Scene):
        def construct(self):
            func = lambda pos: np.sin(pos[0]) * UR + np.cos(pos[1]) * LEFT + pos / 5
            stream_lines = StreamLines(
                func, x_range=[-3, 3, 0.2], y_range=[-2, 2, 0.2], padding=1
            )

            spawning_area = Rectangle(width=6, height=4)
            flowing_area = Rectangle(width=8, height=6)
            labels = [Tex("Spawning Area"), Tex("Flowing Area").shift(DOWN * 2.5)]
            for lbl in labels:
                lbl.add_background_rectangle(opacity=0.6, buff=0.05)

            self.add(stream_lines, spawning_area, flowing_area, *labels)

    ```

    ```

    class SpawningAndFlowingArea(Scene):
        def construct(self):
            func = lambda pos: np.sin(pos[0]) * UR + np.cos(pos[1]) * LEFT + pos / 5
            stream_lines = StreamLines(
                func, x_range=[-3, 3, 0.2], y_range=[-2, 2, 0.2], padding=1
            )

            spawning_area = Rectangle(width=6, height=4)
            flowing_area = Rectangle(width=8, height=6)
            labels = [Tex("Spawning Area"), Tex("Flowing Area").shift(DOWN * 2.5)]
            for lbl in labels:
                lbl.add_background_rectangle(opacity=0.6, buff=0.05)

            self.add(stream_lines, spawning_area, flowing_area, *labels)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`create`](#manim.mobject.vector_field.StreamLines.create "manim.mobject.vector_field.StreamLines.create") | The creation animation of the stream lines. |
    | [`end_animation`](#manim.mobject.vector_field.StreamLines.end_animation "manim.mobject.vector_field.StreamLines.end_animation") | End the stream line animation smoothly. |
    | [`start_animation`](#manim.mobject.vector_field.StreamLines.start_animation "manim.mobject.vector_field.StreamLines.start_animation") | Animates the stream lines using an updater. |

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

    \_original\_\_init\_\_(*func*, *color=None*, *color\_scheme=None*, *min\_color\_scheme\_value=0*, *max\_color\_scheme\_value=2*, *colors=[ManimColor('#236B8E'), ManimColor('#83C167'), ManimColor('#FFFF00'), ManimColor('#FC6255')]*, *x\_range=None*, *y\_range=None*, *z\_range=None*, *three\_dimensions=False*, *noise\_factor=None*, *n\_repeats=1*, *dt=0.05*, *virtual\_time=3*, *max\_anchors\_per\_line=100*, *padding=3*, *stroke\_width=1*, *opacity=1*, *\*\*kwargs*)[¶](#manim.mobject.vector_field.StreamLines._original__init__ "Link to this definition")
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
            * **noise\_factor** (*float* *|* *None*)

    create(*lag\_ratio=None*, *run\_time=None*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/vector_field.html#StreamLines.create)[¶](#manim.mobject.vector_field.StreamLines.create "Link to this definition")
    :   The creation animation of the stream lines.

        The stream lines appear in random order.

        Parameters:
        :   * **lag\_ratio** (*float* *|* *None*) – The lag ratio of the animation.
              If undefined, it will be selected so that the total animation length is 1.5 times the run time of each stream line creation.
            * **run\_time** (*Callable**[**[**float**]**,* *float**]* *|* *None*) – The run time of every single stream line creation. The runtime of the whole animation might be longer due to the lag\_ratio.
              If undefined, the virtual time of the stream lines is used as run time.

        Returns:
        :   The creation animation of the stream lines.

        Return type:
        :   [`AnimationGroup`](manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")

        Examples

        Example: StreamLineCreation [¶](#streamlinecreation)

        [
        ](./StreamLineCreation-1.mp4)

        ```
        from manim import *

        class StreamLineCreation(Scene):
            def construct(self):
                func = lambda pos: (pos[0] * UR + pos[1] * LEFT) - pos
                stream_lines = StreamLines(
                    func,
                    color=YELLOW,
                    x_range=[-7, 7, 1],
                    y_range=[-4, 4, 1],
                    stroke_width=3,
                    virtual_time=1,  # use shorter lines
                    max_anchors_per_line=5,  # better performance with fewer anchors
                )
                self.play(stream_lines.create())  # uses virtual_time as run_time
                self.wait()

        ```

        ```

        class StreamLineCreation(Scene):
            def construct(self):
                func = lambda pos: (pos[0] * UR + pos[1] * LEFT) - pos
                stream_lines = StreamLines(
                    func,
                    color=YELLOW,
                    x_range=[-7, 7, 1],
                    y_range=[-4, 4, 1],
                    stroke_width=3,
                    virtual_time=1,  # use shorter lines
                    max_anchors_per_line=5,  # better performance with fewer anchors
                )
                self.play(stream_lines.create())  # uses virtual_time as run_time
                self.wait()


        ```

    end\_animation()[[source]](../_modules/manim/mobject/vector_field.html#StreamLines.end_animation)[¶](#manim.mobject.vector_field.StreamLines.end_animation "Link to this definition")
    :   End the stream line animation smoothly.

        Returns an animation resulting in fully displayed stream lines without a noticeable cut.

        Returns:
        :   The animation fading out the running stream animation.

        Return type:
        :   [`AnimationGroup`](manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")

        Raises:
        :   **ValueError** – if no stream line animation is running

        Examples

        Example: EndAnimation [¶](#endanimation)

        [
        ](./EndAnimation-1.mp4)

        ```
        from manim import *

        class EndAnimation(Scene):
            def construct(self):
                func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
                stream_lines = StreamLines(
                    func, stroke_width=3, max_anchors_per_line=5, virtual_time=1, color=BLUE
                )
                self.add(stream_lines)
                stream_lines.start_animation(warm_up=False, flow_speed=1.5, time_width=0.5)
                self.wait(1)
                self.play(stream_lines.end_animation())

        ```

        ```

        class EndAnimation(Scene):
            def construct(self):
                func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
                stream_lines = StreamLines(
                    func, stroke_width=3, max_anchors_per_line=5, virtual_time=1, color=BLUE
                )
                self.add(stream_lines)
                stream_lines.start_animation(warm_up=False, flow_speed=1.5, time_width=0.5)
                self.wait(1)
                self.play(stream_lines.end_animation())


        ```

    start\_animation(*warm\_up=True*, *flow\_speed=1*, *time\_width=0.3*, *rate\_func=<function linear>*, *line\_animation\_class=<class 'manim.animation.indication.ShowPassingFlash'>*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/vector_field.html#StreamLines.start_animation)[¶](#manim.mobject.vector_field.StreamLines.start_animation "Link to this definition")
    :   Animates the stream lines using an updater.

        The stream lines will continuously flow

        Parameters:
        :   * **warm\_up** (*bool*) – If True the animation is initialized line by line. Otherwise it starts with all lines shown.
            * **flow\_speed** (*float*) – At flow\_speed=1 the distance the flow moves per second is equal to the magnitude of the vector field along its path. The speed value scales the speed of this flow.
            * **time\_width** (*float*) – The proportion of the stream line shown while being animated
            * **rate\_func** (*Callable**[**[**float**]**,* *float**]*) – The rate function of each stream line flashing
            * **line\_animation\_class** (*type**[*[*ShowPassingFlash*](manim.animation.indication.ShowPassingFlash.html#manim.animation.indication.ShowPassingFlash "manim.animation.indication.ShowPassingFlash")*]*) – The animation class being used

        Return type:
        :   None

        Examples

        Example: ContinuousMotion [¶](#continuousmotion)

        [
        ](./ContinuousMotion-1.mp4)

        ```
        from manim import *

        class ContinuousMotion(Scene):
            def construct(self):
                func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
                stream_lines = StreamLines(func, stroke_width=3, max_anchors_per_line=30)
                self.add(stream_lines)
                stream_lines.start_animation(warm_up=False, flow_speed=1.5)
                self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

        ```

        ```

        class ContinuousMotion(Scene):
            def construct(self):
                func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
                stream_lines = StreamLines(func, stroke_width=3, max_anchors_per_line=30)
                self.add(stream_lines)
                stream_lines.start_animation(warm_up=False, flow_speed=1.5)
                self.wait(stream_lines.virtual_time / stream_lines.flow_speed)


        ```