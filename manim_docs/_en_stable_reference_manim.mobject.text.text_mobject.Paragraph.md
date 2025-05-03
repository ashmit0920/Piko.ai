# Source: https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Paragraph[¶](#paragraph "Link to this heading")
===============================================

Qualified name: `manim.mobject.text.text\_mobject.Paragraph`

*class* Paragraph(*\*text*, *line\_spacing=-1*, *alignment=None*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/text/text_mobject.html#Paragraph)[¶](#manim.mobject.text.text_mobject.Paragraph "Link to this definition")
:   Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

    Display a paragraph of text.

    For a given [`Paragraph`](#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph") `par`, the attribute `par.chars` is a
    [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") containing all the lines. In this context, every line is
    constructed as a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") of characters contained in the line.

    Parameters:
    :   * **line\_spacing** (*float*) – Represents the spacing between lines. Defaults to -1, which means auto.
        * **alignment** (*str* *|* *None*) – Defines the alignment of paragraph. Defaults to None. Possible values are “left”, “right” or “center”.
        * **text** (*Sequence**[**str**]*)

    Examples

    Normal usage:

    ```
    paragraph = Paragraph(
        "this is a awesome",
        "paragraph",
        "With \nNewlines",
        "\tWith Tabs",
        "  With Spaces",
        "With Alignments",
        "center",
        "left",
        "right",
    )

    ```

    Remove unwanted invisible characters:

    ```
    self.play(Transform(remove_invisible_chars(paragraph.chars[0:2]),
                        remove_invisible_chars(paragraph.chars[3][0:3]))

    ```

    Methods

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

    \_change\_alignment\_for\_a\_line(*alignment*, *line\_no*)[[source]](../_modules/manim/mobject/text/text_mobject.html#Paragraph._change_alignment_for_a_line)[¶](#manim.mobject.text.text_mobject.Paragraph._change_alignment_for_a_line "Link to this definition")
    :   Function to change one line’s alignment to a specific value.

        Parameters:
        :   * **alignment** (*str*) – Defines the alignment of paragraph. Possible values are “left”, “right”, “center”.
            * **line\_no** (*int*) – Defines the line number for which we want to set given alignment.

        Return type:
        :   None

    \_gen\_chars(*lines\_str\_list*)[[source]](../_modules/manim/mobject/text/text_mobject.html#Paragraph._gen_chars)[¶](#manim.mobject.text.text_mobject.Paragraph._gen_chars "Link to this definition")
    :   Function to convert a list of plain strings to a VGroup of VGroups of chars.

        Parameters:
        :   **lines\_str\_list** (*list*) – List of plain text strings.

        Returns:
        :   The generated 2d-VGroup of chars.

        Return type:
        :   [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

    \_original\_\_init\_\_(*\*text*, *line\_spacing=-1*, *alignment=None*, *\*\*kwargs*)[¶](#manim.mobject.text.text_mobject.Paragraph._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **text** (*Sequence**[**str**]*)
            * **line\_spacing** (*float*)
            * **alignment** (*str* *|* *None*)

        Return type:
        :   None

    \_set\_all\_lines\_alignments(*alignment*)[[source]](../_modules/manim/mobject/text/text_mobject.html#Paragraph._set_all_lines_alignments)[¶](#manim.mobject.text.text_mobject.Paragraph._set_all_lines_alignments "Link to this definition")
    :   Function to set all line’s alignment to a specific value.

        Parameters:
        :   **alignment** (*str*) – Defines the alignment of paragraph. Possible values are “left”, “right”, “center”.

        Return type:
        :   [*Paragraph*](#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph")

    \_set\_all\_lines\_to\_initial\_positions()[[source]](../_modules/manim/mobject/text/text_mobject.html#Paragraph._set_all_lines_to_initial_positions)[¶](#manim.mobject.text.text_mobject.Paragraph._set_all_lines_to_initial_positions "Link to this definition")
    :   Set all lines to their initial positions.

        Return type:
        :   [*Paragraph*](#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph")

    \_set\_line\_alignment(*alignment*, *line\_no*)[[source]](../_modules/manim/mobject/text/text_mobject.html#Paragraph._set_line_alignment)[¶](#manim.mobject.text.text_mobject.Paragraph._set_line_alignment "Link to this definition")
    :   Function to set one line’s alignment to a specific value.

        Parameters:
        :   * **alignment** (*str*) – Defines the alignment of paragraph. Possible values are “left”, “right”, “center”.
            * **line\_no** (*int*) – Defines the line number for which we want to set given alignment.

        Return type:
        :   [*Paragraph*](#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph")

    \_set\_line\_to\_initial\_position(*line\_no*)[[source]](../_modules/manim/mobject/text/text_mobject.html#Paragraph._set_line_to_initial_position)[¶](#manim.mobject.text.text_mobject.Paragraph._set_line_to_initial_position "Link to this definition")
    :   Function to set one line to initial positions.

        Parameters:
        :   **line\_no** (*int*) – Defines the line number for which we want to set given alignment.

        Return type:
        :   [*Paragraph*](#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph")