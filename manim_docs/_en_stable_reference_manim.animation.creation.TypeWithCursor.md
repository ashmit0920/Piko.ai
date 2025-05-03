# Source: https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

TypeWithCursor[¶](#typewithcursor "Link to this heading")
=========================================================

Qualified name: `manim.animation.creation.TypeWithCursor`

*class* TypeWithCursor(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/creation.html#TypeWithCursor)[¶](#manim.animation.creation.TypeWithCursor "Link to this definition")
:   Bases: [`AddTextLetterByLetter`](manim.animation.creation.AddTextLetterByLetter.html#manim.animation.creation.AddTextLetterByLetter "manim.animation.creation.AddTextLetterByLetter")

    Similar to [`AddTextLetterByLetter`](manim.animation.creation.AddTextLetterByLetter.html#manim.animation.creation.AddTextLetterByLetter "manim.animation.creation.AddTextLetterByLetter") , but with an additional cursor mobject at the end.

    Parameters:
    :   * **time\_per\_char** (*float*) – Frequency of appearance of the letters.
        * **cursor** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") shown after the last added letter.
        * **buff** (*float*) – Controls how far away the cursor is to the right of the last added letter.
        * **keep\_cursor\_y** (*bool*) – If `True`, the cursor’s y-coordinate is set to the center of the `Text` and remains the same throughout the animation. Otherwise, it is set to the center of the last added letter.
        * **leave\_cursor\_on** (*bool*) – Whether to show the cursor after the animation.
        * **tip::** (*..*) – This is currently only possible for class:~.Text and not for class:~.MathTex.
        * **text** ([*Text*](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"))

    Examples

    Example: InsertingTextExample [¶](#insertingtextexample)

    [
    ](./InsertingTextExample-1.mp4)

    ```
    from manim import *

    class InsertingTextExample(Scene):
        def construct(self):
            text = Text("Inserting", color=PURPLE).scale(1.5).to_edge(LEFT)
            cursor = Rectangle(
                color = GREY_A,
                fill_color = GREY_A,
                fill_opacity = 1.0,
                height = 1.1,
                width = 0.5,
            ).move_to(text[0]) # Position the cursor

            self.play(TypeWithCursor(text, cursor))
            self.play(Blink(cursor, blinks=2))

    ```

    ```

    class InsertingTextExample(Scene):
        def construct(self):
            text = Text("Inserting", color=PURPLE).scale(1.5).to_edge(LEFT)
            cursor = Rectangle(
                color = GREY_A,
                fill_color = GREY_A,
                fill_opacity = 1.0,
                height = 1.1,
                width = 0.5,
            ).move_to(text[0]) # Position the cursor

            self.play(TypeWithCursor(text, cursor))
            self.play(Blink(cursor, blinks=2))


    ```

    References: [`Blink`](manim.animation.indication.Blink.html#manim.animation.indication.Blink "manim.animation.indication.Blink")

    Methods

    |  |  |
    | --- | --- |
    | [`begin`](#manim.animation.creation.TypeWithCursor.begin "manim.animation.creation.TypeWithCursor.begin") | Begin the animation. |
    | [`clean_up_from_scene`](#manim.animation.creation.TypeWithCursor.clean_up_from_scene "manim.animation.creation.TypeWithCursor.clean_up_from_scene") | Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
    | [`finish`](#manim.animation.creation.TypeWithCursor.finish "manim.animation.creation.TypeWithCursor.finish") | Finish the animation. |
    | `update_submobject_list` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*text*, *cursor*, *buff=0.1*, *keep\_cursor\_y=True*, *leave\_cursor\_on=True*, *time\_per\_char=0.1*, *reverse\_rate\_function=False*, *introducer=True*, *\*\*kwargs*)[¶](#manim.animation.creation.TypeWithCursor._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **text** ([*Text*](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"))
            * **cursor** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **buff** (*float*)
            * **keep\_cursor\_y** (*bool*)
            * **leave\_cursor\_on** (*bool*)
            * **time\_per\_char** (*float*)

        Return type:
        :   None

    begin()[[source]](../_modules/manim/animation/creation.html#TypeWithCursor.begin)[¶](#manim.animation.creation.TypeWithCursor.begin "Link to this definition")
    :   Begin the animation.

        This method is called right as an animation is being played. As much
        initialization as possible, especially any mobject copying, should live in this
        method.

        Return type:
        :   None

    clean\_up\_from\_scene(*scene*)[[source]](../_modules/manim/animation/creation.html#TypeWithCursor.clean_up_from_scene)[¶](#manim.animation.creation.TypeWithCursor.clean_up_from_scene "Link to this definition")
    :   Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.

        This includes to [`remove()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
        [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.

        Parameters:
        :   **scene** ([*Scene*](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.

        Return type:
        :   None

    finish()[[source]](../_modules/manim/animation/creation.html#TypeWithCursor.finish)[¶](#manim.animation.creation.TypeWithCursor.finish "Link to this definition")
    :   Finish the animation.

        This method gets called when the animation is over.

        Return type:
        :   None