# Source: https://docs.manim.community/en/stable/reference/manim.utils.tex_templates.TexTemplateLibrary.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

TexTemplateLibrary[¶](#textemplatelibrary "Link to this heading")
=================================================================

Qualified name: `manim.utils.tex\_templates.TexTemplateLibrary`

*class* TexTemplateLibrary[[source]](../_modules/manim/utils/tex_templates.html#TexTemplateLibrary)[¶](#manim.utils.tex_templates.TexTemplateLibrary "Link to this definition")
:   Bases: `object`

    A collection of basic TeX template objects

    Examples

    Normal usage as a value for the keyword argument tex\_template of Tex() and MathTex() mobjects:

    ```
    ``Tex("My TeX code", tex_template=TexTemplateLibrary.ctex)``

    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | [`ctex`](#manim.utils.tex_templates.TexTemplateLibrary.ctex "manim.utils.tex_templates.TexTemplateLibrary.ctex") | An instance of the TeX template used by 3b1b when using the use\_ctex flag |
    | [`default`](#manim.utils.tex_templates.TexTemplateLibrary.default "manim.utils.tex_templates.TexTemplateLibrary.default") | An instance of the default TeX template in manim |
    | [`simple`](#manim.utils.tex_templates.TexTemplateLibrary.simple "manim.utils.tex_templates.TexTemplateLibrary.simple") | An instance of a simple TeX template with only basic AMS packages loaded |
    | [`threeb1b`](#manim.utils.tex_templates.TexTemplateLibrary.threeb1b "manim.utils.tex_templates.TexTemplateLibrary.threeb1b") | An instance of the default TeX template used by 3b1b |

    ctex *= TexTemplate(\_body='', tex\_compiler='xelatex', description='', output\_format='.xdv', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{lmodern}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{dsfont}\n\\usepackage{setspace}\n\\usepackage{tipa}\n\\usepackage{relsize}\n\\usepackage{textcomp}\n\\usepackage{mathrsfs}\n\\usepackage{calligra}\n\\usepackage{wasysym}\n\\usepackage{ragged2e}\n\\usepackage{physics}\n\\usepackage{xcolor}\n\\usepackage{microtype}\n\\usepackage[UTF8]{ctex}\n\\linespread{1}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexTemplateLibrary.ctex "Link to this definition")
    :   An instance of the TeX template used by 3b1b when using the use\_ctex flag

    default *= TexTemplate(\_body='', tex\_compiler='latex', description='', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{lmodern}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{dsfont}\n\\usepackage{setspace}\n\\usepackage{tipa}\n\\usepackage{relsize}\n\\usepackage{textcomp}\n\\usepackage{mathrsfs}\n\\usepackage{calligra}\n\\usepackage{wasysym}\n\\usepackage{ragged2e}\n\\usepackage{physics}\n\\usepackage{xcolor}\n\\usepackage{microtype}\n\\DisableLigatures{encoding = \*, family = \* }\n\\linespread{1}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexTemplateLibrary.default "Link to this definition")
    :   An instance of the default TeX template in manim

    simple *= TexTemplate(\_body='', tex\_compiler='latex', description='', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexTemplateLibrary.simple "Link to this definition")
    :   An instance of a simple TeX template with only basic AMS packages loaded

    threeb1b *= TexTemplate(\_body='', tex\_compiler='latex', description='', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{lmodern}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{dsfont}\n\\usepackage{setspace}\n\\usepackage{tipa}\n\\usepackage{relsize}\n\\usepackage{textcomp}\n\\usepackage{mathrsfs}\n\\usepackage{calligra}\n\\usepackage{wasysym}\n\\usepackage{ragged2e}\n\\usepackage{physics}\n\\usepackage{xcolor}\n\\usepackage{microtype}\n\\DisableLigatures{encoding = \*, family = \* }\n\\linespread{1}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexTemplateLibrary.threeb1b "Link to this definition")
    :   An instance of the default TeX template used by 3b1b