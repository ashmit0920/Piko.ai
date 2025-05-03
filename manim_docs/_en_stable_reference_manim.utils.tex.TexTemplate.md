# Source: https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

TexTemplate[¶](#textemplate "Link to this heading")
===================================================

Qualified name: `manim.utils.tex.TexTemplate`

*class* TexTemplate(*tex\_compiler='latex'*, *description=''*, *output\_format='.dvi'*, *documentclass='\\documentclass[preview]{standalone}'*, *preamble='\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}'*, *placeholder\_text='YourTextHere'*, *post\_doc\_commands=''*)[[source]](../_modules/manim/utils/tex.html#TexTemplate)[¶](#manim.utils.tex.TexTemplate "Link to this definition")
:   Bases: `object`

    TeX templates are used to create `Tex` and `MathTex` objects.

    Methods

    |  |  |
    | --- | --- |
    | [`add_to_document`](#manim.utils.tex.TexTemplate.add_to_document "manim.utils.tex.TexTemplate.add_to_document") | Adds text to the TeX template just after begin{document}, e.g. `\boldmath`. |
    | [`add_to_preamble`](#manim.utils.tex.TexTemplate.add_to_preamble "manim.utils.tex.TexTemplate.add_to_preamble") | Adds text to the TeX template's preamble (e.g. definitions, packages). |
    | [`copy`](#manim.utils.tex.TexTemplate.copy "manim.utils.tex.TexTemplate.copy") | Create a deep copy of the TeX template instance. |
    | [`from_file`](#manim.utils.tex.TexTemplate.from_file "manim.utils.tex.TexTemplate.from_file") | Create an instance by reading the content of a file. |
    | [`get_texcode_for_expression`](#manim.utils.tex.TexTemplate.get_texcode_for_expression "manim.utils.tex.TexTemplate.get_texcode_for_expression") | Inserts expression verbatim into TeX template. |
    | [`get_texcode_for_expression_in_env`](#manim.utils.tex.TexTemplate.get_texcode_for_expression_in_env "manim.utils.tex.TexTemplate.get_texcode_for_expression_in_env") | Inserts expression into TeX template wrapped in `\begin{environment}` and `\end{environment}`. |

    Attributes

    |  |  |
    | --- | --- |
    | [`body`](#manim.utils.tex.TexTemplate.body "manim.utils.tex.TexTemplate.body") | The entire TeX template. |
    | [`description`](#manim.utils.tex.TexTemplate.description "manim.utils.tex.TexTemplate.description") | A description of the template |
    | [`documentclass`](#manim.utils.tex.TexTemplate.documentclass "manim.utils.tex.TexTemplate.documentclass") | The command defining the documentclass, e.g. `\documentclass[preview]{standalone}`. |
    | [`output_format`](#manim.utils.tex.TexTemplate.output_format "manim.utils.tex.TexTemplate.output_format") | The output format resulting from compilation, e.g. `.dvi` or `.pdf`. |
    | [`placeholder_text`](#manim.utils.tex.TexTemplate.placeholder_text "manim.utils.tex.TexTemplate.placeholder_text") | Text in the document that will be replaced by the expression to be rendered. |
    | [`post_doc_commands`](#manim.utils.tex.TexTemplate.post_doc_commands "manim.utils.tex.TexTemplate.post_doc_commands") | Text (definitions, commands) to be inserted at right after `\begin{document}`, e.g. `\boldmath`. |
    | [`preamble`](#manim.utils.tex.TexTemplate.preamble "manim.utils.tex.TexTemplate.preamble") | The document's preamble, i.e. the part between `\documentclass` and `\begin{document}`. |
    | [`tex_compiler`](#manim.utils.tex.TexTemplate.tex_compiler "manim.utils.tex.TexTemplate.tex_compiler") | The TeX compiler to be used, e.g. `latex`, `pdflatex` or `lualatex`. |

    Parameters:
    :   * **tex\_compiler** (*str*)
        * **description** (*str*)
        * **output\_format** (*str*)
        * **documentclass** (*str*)
        * **preamble** (*str*)
        * **placeholder\_text** (*str*)
        * **post\_doc\_commands** (*str*)

    \_body*: str* *= ''*[¶](#manim.utils.tex.TexTemplate._body "Link to this definition")
    :   A custom body, can be set from a file.

    add\_to\_document(*txt*)[[source]](../_modules/manim/utils/tex.html#TexTemplate.add_to_document)[¶](#manim.utils.tex.TexTemplate.add_to_document "Link to this definition")
    :   Adds text to the TeX template just after begin{document}, e.g. `\boldmath`.

        Parameters:
        :   **txt** (*str*) – String containing the text to be added.

        Return type:
        :   Self

    add\_to\_preamble(*txt*, *prepend=False*)[[source]](../_modules/manim/utils/tex.html#TexTemplate.add_to_preamble)[¶](#manim.utils.tex.TexTemplate.add_to_preamble "Link to this definition")
    :   Adds text to the TeX template’s preamble (e.g. definitions, packages). Text can be inserted at the beginning or at the end of the preamble.

        Parameters:
        :   * **txt** (*str*) – String containing the text to be added, e.g. `\usepackage{hyperref}`.
            * **prepend** (*bool*) – Whether the text should be added at the beginning of the preamble, i.e. right after `\documentclass`.
              Default is to add it at the end of the preamble, i.e. right before `\begin{document}`.

        Return type:
        :   Self

    *property* body*: str*[¶](#manim.utils.tex.TexTemplate.body "Link to this definition")
    :   The entire TeX template.

    copy()[[source]](../_modules/manim/utils/tex.html#TexTemplate.copy)[¶](#manim.utils.tex.TexTemplate.copy "Link to this definition")
    :   Create a deep copy of the TeX template instance.

        Return type:
        :   Self

    description*: str* *= ''*[¶](#manim.utils.tex.TexTemplate.description "Link to this definition")
    :   A description of the template

    documentclass*: str* *= '\\documentclass[preview]{standalone}'*[¶](#manim.utils.tex.TexTemplate.documentclass "Link to this definition")
    :   The command defining the documentclass, e.g. `\documentclass[preview]{standalone}`.

    *classmethod* from\_file(*file='tex\_template.tex'*, *\*\*kwargs*)[[source]](../_modules/manim/utils/tex.html#TexTemplate.from_file)[¶](#manim.utils.tex.TexTemplate.from_file "Link to this definition")
    :   Create an instance by reading the content of a file.

        Using the `add_to_preamble` and `add_to_document` methods on this instance
        will have no effect, as the body is read from the file.

        Parameters:
        :   * **file** ([*StrPath*](manim.typing.html#manim.typing.StrPath "manim.typing.StrPath"))
            * **kwargs** (*Any*)

        Return type:
        :   Self

    get\_texcode\_for\_expression(*expression*)[[source]](../_modules/manim/utils/tex.html#TexTemplate.get_texcode_for_expression)[¶](#manim.utils.tex.TexTemplate.get_texcode_for_expression "Link to this definition")
    :   Inserts expression verbatim into TeX template.

        Parameters:
        :   **expression** (*str*) – The string containing the expression to be typeset, e.g. `$\sqrt{2}$`

        Returns:
        :   LaTeX code based on current template, containing the given `expression` and ready for typesetting

        Return type:
        :   `str`

    get\_texcode\_for\_expression\_in\_env(*expression*, *environment*)[[source]](../_modules/manim/utils/tex.html#TexTemplate.get_texcode_for_expression_in_env)[¶](#manim.utils.tex.TexTemplate.get_texcode_for_expression_in_env "Link to this definition")
    :   Inserts expression into TeX template wrapped in `\begin{environment}` and `\end{environment}`.

        Parameters:
        :   * **expression** (*str*) – The string containing the expression to be typeset, e.g. `$\sqrt{2}$`.
            * **environment** (*str*) – The string containing the environment in which the expression should be typeset, e.g. `align*`.

        Returns:
        :   LaTeX code based on template, containing the given expression inside its environment, ready for typesetting

        Return type:
        :   `str`

    output\_format*: str* *= '.dvi'*[¶](#manim.utils.tex.TexTemplate.output_format "Link to this definition")
    :   The output format resulting from compilation, e.g. `.dvi` or `.pdf`.

    placeholder\_text*: str* *= 'YourTextHere'*[¶](#manim.utils.tex.TexTemplate.placeholder_text "Link to this definition")
    :   Text in the document that will be replaced by the expression to be rendered.

    post\_doc\_commands*: str* *= ''*[¶](#manim.utils.tex.TexTemplate.post_doc_commands "Link to this definition")
    :   Text (definitions, commands) to be inserted at right after `\begin{document}`, e.g. `\boldmath`.

    preamble*: str* *= '\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}'*[¶](#manim.utils.tex.TexTemplate.preamble "Link to this definition")
    :   The document’s preamble, i.e. the part between `\documentclass` and `\begin{document}`.

    tex\_compiler*: str* *= 'latex'*[¶](#manim.utils.tex.TexTemplate.tex_compiler "Link to this definition")
    :   The TeX compiler to be used, e.g. `latex`, `pdflatex` or `lualatex`.