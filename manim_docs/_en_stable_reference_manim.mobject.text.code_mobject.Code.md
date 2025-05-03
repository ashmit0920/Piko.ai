# Source: https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Code[¶](#code "Link to this heading")
=====================================

Qualified name: `manim.mobject.text.code\_mobject.Code`

*class* Code(*code\_file=None*, *code\_string=None*, *language=None*, *formatter\_style='vim'*, *tab\_width=4*, *add\_line\_numbers=True*, *line\_numbers\_from=1*, *background='rectangle'*, *background\_config=None*, *paragraph\_config=None*)[[source]](../_modules/manim/mobject/text/code_mobject.html#Code)[¶](#manim.mobject.text.code_mobject.Code "Link to this definition")
:   Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    A highlighted source code listing.

    Examples

    Normal usage:

    ```
    listing = Code(
        "helloworldcpp.cpp",
        tab_width=4,
        formatter_style="emacs",
        background="window",
        language="cpp",
        background_config={"stroke_color": WHITE},
        paragraph_config={"font": "Noto Sans Mono"},
    )

    ```

    We can also render code passed as a string. As the automatic language
    detection can be a bit flaky, it is recommended to specify the language
    explicitly:

    Example: CodeFromString [¶](#codefromstring)

    ![../_images/CodeFromString-1.png](../_images/CodeFromString-1.png)

    ```
    from manim import *

    class CodeFromString(Scene):
        def construct(self):
            code = '''from manim import Scene, Square

    class FadeInSquare(Scene):
        def construct(self):
            s = Square()
            self.play(FadeIn(s))
            self.play(s.animate.scale(2))
            self.wait()'''

            rendered_code = Code(
                code_string=code,
                language="python",
                background="window",
                background_config={"stroke_color": "maroon"},
            )
            self.add(rendered_code)

    ```

    ```

    class CodeFromString(Scene):
        def construct(self):
            code = '''from manim import Scene, Square

    class FadeInSquare(Scene):
        def construct(self):
            s = Square()
            self.play(FadeIn(s))
            self.play(s.animate.scale(2))
            self.wait()'''

            rendered_code = Code(
                code_string=code,
                language="python",
                background="window",
                background_config={"stroke_color": "maroon"},
            )
            self.add(rendered_code)


    ```

    Parameters:
    :   * **code\_file** ([*StrPath*](manim.typing.html#manim.typing.StrPath "manim.typing.StrPath") *|* *None*) – The path to the code file to display.
        * **code\_string** (*str* *|* *None*) – Alternatively, the code string to display.
        * **language** (*str* *|* *None*) – The programming language of the code. If not specified, it will be
          guessed from the file extension or the code itself.
        * **formatter\_style** (*str*) – The style to use for the code highlighting. Defaults to `"vim"`.
          A list of all available styles can be obtained by calling
          [`Code.get_styles_list()`](#manim.mobject.text.code_mobject.Code.get_styles_list "manim.mobject.text.code_mobject.Code.get_styles_list").
        * **tab\_width** (*int*) – The width of a tab character in spaces. Defaults to 4.
        * **add\_line\_numbers** (*bool*) – Whether to display line numbers. Defaults to `True`.
        * **line\_numbers\_from** (*int*) – The first line number to display. Defaults to 1.
        * **background** (*Literal**[**'rectangle'**,* *'window'**]*) – The type of background to use. Can be either `"rectangle"` (the
          default) or `"window"`.
        * **background\_config** (*dict**[**str**,* *Any**]* *|* *None*) – Keyword arguments passed to the background constructor. Default
          settings are stored in the class attribute
          `default_background_config` (which can also be modified
          directly).
        * **paragraph\_config** (*dict**[**str**,* *Any**]* *|* *None*) – Keyword arguments passed to the constructor of the
          [`Paragraph`](manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph") objects holding the code, and the line
          numbers. Default settings are stored in the class attribute
          `default_paragraph_config` (which can also be modified
          directly).

    Methods

    |  |  |
    | --- | --- |
    | [`get_styles_list`](#manim.mobject.text.code_mobject.Code.get_styles_list "manim.mobject.text.code_mobject.Code.get_styles_list") | Get the list of all available formatter styles. |

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `default_background_config` |  |
    | `default_paragraph_config` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*code\_file=None*, *code\_string=None*, *language=None*, *formatter\_style='vim'*, *tab\_width=4*, *add\_line\_numbers=True*, *line\_numbers\_from=1*, *background='rectangle'*, *background\_config=None*, *paragraph\_config=None*)[¶](#manim.mobject.text.code_mobject.Code._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **code\_file** ([*StrPath*](manim.typing.html#manim.typing.StrPath "manim.typing.StrPath") *|* *None*)
            * **code\_string** (*str* *|* *None*)
            * **language** (*str* *|* *None*)
            * **formatter\_style** (*str*)
            * **tab\_width** (*int*)
            * **add\_line\_numbers** (*bool*)
            * **line\_numbers\_from** (*int*)
            * **background** (*Literal**[**'rectangle'**,* *'window'**]*)
            * **background\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            * **paragraph\_config** (*dict**[**str**,* *Any**]* *|* *None*)

    *classmethod* get\_styles\_list()[[source]](../_modules/manim/mobject/text/code_mobject.html#Code.get_styles_list)[¶](#manim.mobject.text.code_mobject.Code.get_styles_list "Link to this definition")
    :   Get the list of all available formatter styles.

        Return type:
        :   list[str]