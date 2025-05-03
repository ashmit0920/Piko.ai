# Source: https://docs.manim.community/en/stable/reference/manim.utils.docbuild.autoaliasattr_directive.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

autoaliasattr\_directive[¶](#module-manim.utils.docbuild.autoaliasattr_directive "Link to this heading")
========================================================================================================

A directive for documenting type aliases and other module-level attributes.

Classes

|  |  |
| --- | --- |
| [`AliasAttrDocumenter`](manim.utils.docbuild.autoaliasattr_directive.AliasAttrDocumenter.html#manim.utils.docbuild.autoaliasattr_directive.AliasAttrDocumenter "manim.utils.docbuild.autoaliasattr_directive.AliasAttrDocumenter") | Directive which replaces Sphinx's Autosummary for module-level attributes: instead, it manually crafts a new "Type Aliases" section, where all the module-level attributes which are explicitly annotated as `TypeAlias` are considered as such, for their use all around the Manim docs. |

Functions

setup(*app*)[[source]](../_modules/manim/utils/docbuild/autoaliasattr_directive.html#setup)[¶](#manim.utils.docbuild.autoaliasattr_directive.setup "Link to this definition")
:   Parameters:
    :   **app** (*Sphinx*)

    Return type:
    :   None

smart\_replace(*base*, *alias*, *substitution*)[[source]](../_modules/manim/utils/docbuild/autoaliasattr_directive.html#smart_replace)[¶](#manim.utils.docbuild.autoaliasattr_directive.smart_replace "Link to this definition")
:   Auxiliary function for substituting type aliases into a base
    string, when there are overlaps between the aliases themselves.

    Parameters:
    :   * **base** (*str*) – The string in which the type aliases will be located and
          replaced.
        * **alias** (*str*) – The substring to be substituted.
        * **substitution** (*str*) – The string which will replace every occurrence of `alias`.

    Returns:
    :   The new string after the alias substitution.

    Return type:
    :   str