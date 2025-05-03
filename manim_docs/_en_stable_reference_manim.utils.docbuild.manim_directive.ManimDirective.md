# Source: https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ManimDirective[¶](#manimdirective "Link to this heading")
=========================================================

Qualified name: `manim.utils.docbuild.manim\_directive.ManimDirective`

*class* ManimDirective(*name*, *arguments*, *options*, *content*, *lineno*, *content\_offset*, *block\_text*, *state*, *state\_machine*)[[source]](../_modules/manim/utils/docbuild/manim_directive.html#ManimDirective)[¶](#manim.utils.docbuild.manim_directive.ManimDirective "Link to this definition")
:   Bases: `Directive`

    The manim directive, rendering videos while building
    the documentation.

    See the module docstring for documentation.

    Methods

    |  |  |
    | --- | --- |
    | `run` |  |

    Attributes

    |  |  |
    | --- | --- |
    | [`final_argument_whitespace`](#manim.utils.docbuild.manim_directive.ManimDirective.final_argument_whitespace "manim.utils.docbuild.manim_directive.ManimDirective.final_argument_whitespace") | May the final argument contain whitespace? |
    | [`has_content`](#manim.utils.docbuild.manim_directive.ManimDirective.has_content "manim.utils.docbuild.manim_directive.ManimDirective.has_content") | May the directive have content? |
    | [`option_spec`](#manim.utils.docbuild.manim_directive.ManimDirective.option_spec "manim.utils.docbuild.manim_directive.ManimDirective.option_spec") | Mapping of option names to validator functions. |
    | [`optional_arguments`](#manim.utils.docbuild.manim_directive.ManimDirective.optional_arguments "manim.utils.docbuild.manim_directive.ManimDirective.optional_arguments") | Number of optional arguments after the required arguments. |
    | [`required_arguments`](#manim.utils.docbuild.manim_directive.ManimDirective.required_arguments "manim.utils.docbuild.manim_directive.ManimDirective.required_arguments") | Number of required directive arguments. |

    final\_argument\_whitespace *= True*[¶](#manim.utils.docbuild.manim_directive.ManimDirective.final_argument_whitespace "Link to this definition")
    :   May the final argument contain whitespace?

    has\_content *= True*[¶](#manim.utils.docbuild.manim_directive.ManimDirective.has_content "Link to this definition")
    :   May the directive have content?

    option\_spec *= {'hide\_source': <class 'bool'>, 'no\_autoplay': <class 'bool'>, 'quality': <function ManimDirective.<lambda>>, 'ref\_classes': <function ManimDirective.<lambda>>, 'ref\_functions': <function ManimDirective.<lambda>>, 'ref\_methods': <function ManimDirective.<lambda>>, 'ref\_modules': <function ManimDirective.<lambda>>, 'save\_as\_gif': <class 'bool'>, 'save\_last\_frame': <class 'bool'>}*[¶](#manim.utils.docbuild.manim_directive.ManimDirective.option_spec "Link to this definition")
    :   Mapping of option names to validator functions.

    optional\_arguments *= 0*[¶](#manim.utils.docbuild.manim_directive.ManimDirective.optional_arguments "Link to this definition")
    :   Number of optional arguments after the required arguments.

    required\_arguments *= 1*[¶](#manim.utils.docbuild.manim_directive.ManimDirective.required_arguments "Link to this definition")
    :   Number of required directive arguments.