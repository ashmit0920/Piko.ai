# Source: https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

module\_parsing[¶](#module-manim.utils.docbuild.module_parsing "Link to this heading")
======================================================================================

Read and parse all the Manim modules and extract documentation from them.

Type Aliases

*class* AliasInfo[¶](#manim.utils.docbuild.module_parsing.AliasInfo "Link to this definition")
:   ```
    dict[str, str]

    ```

    Dictionary with a definition key containing the definition of
    a `TypeAlias` as a string, and optionally a doc key containing
    the documentation for that alias, if it exists.

*class* AliasCategoryDict[¶](#manim.utils.docbuild.module_parsing.AliasCategoryDict "Link to this definition")
:   ```
    dict[str, AliasInfo]
    ```

    Dictionary which holds an [`AliasInfo`](#manim.utils.docbuild.module_parsing.AliasInfo "manim.utils.docbuild.module_parsing.AliasInfo") for every alias name in a same
    category.

*class* ModuleLevelAliasDict[¶](#manim.utils.docbuild.module_parsing.ModuleLevelAliasDict "Link to this definition")
:   ```
    dict[str, AliasCategoryDict]
    ```

    Dictionary containing every `TypeAlias` defined in a module,
    classified by category in different [`AliasCategoryDict`](#manim.utils.docbuild.module_parsing.AliasCategoryDict "manim.utils.docbuild.module_parsing.AliasCategoryDict") objects.

*class* ModuleTypeVarDict[¶](#manim.utils.docbuild.module_parsing.ModuleTypeVarDict "Link to this definition")
:   ```
    dict[str, str]

    ```

    Dictionary containing every `TypeVar` defined in a module.

*class* AliasDocsDict[¶](#manim.utils.docbuild.module_parsing.AliasDocsDict "Link to this definition")
:   ```
    dict[str, ModuleLevelAliasDict]
    ```

    Dictionary which, for every module in Manim, contains documentation
    about their module-level attributes which are explicitly defined as
    `TypeAlias`, separating them from the rest of attributes.

*class* DataDict[¶](#manim.utils.docbuild.module_parsing.DataDict "Link to this definition")
:   ```
    dict[str, list[str]]

    ```

    Type for a dictionary which, for every module, contains a list with
    the names of all their DOCUMENTED module-level attributes (identified
    by Sphinx via the `data` role, hence the name) which are NOT
    explicitly defined as `TypeAlias`.

*class* TypeVarDict[¶](#manim.utils.docbuild.module_parsing.TypeVarDict "Link to this definition")
:   ```
    dict[str, ModuleTypeVarDict]
    ```

    A dictionary mapping module names to dictionaries of `TypeVar` objects.

Functions

parse\_module\_attributes()[[source]](../_modules/manim/utils/docbuild/module_parsing.html#parse_module_attributes)[¶](#manim.utils.docbuild.module_parsing.parse_module_attributes "Link to this definition")
:   Read all files, generate Abstract Syntax Trees from them, and
    extract useful information about the type aliases defined in the
    files: the category they belong to, their definition and their
    description, separating them from the “regular” module attributes.

    Returns:
    :   * **ALIAS\_DOCS\_DICT** ([`AliasDocsDict`](#manim.utils.docbuild.module_parsing.AliasDocsDict "manim.utils.docbuild.module_parsing.AliasDocsDict")) – A dictionary containing the information from all the type
          aliases in Manim. See [`AliasDocsDict`](#manim.utils.docbuild.module_parsing.AliasDocsDict "manim.utils.docbuild.module_parsing.AliasDocsDict") for more information.
        * **DATA\_DICT** ([`DataDict`](#manim.utils.docbuild.module_parsing.DataDict "manim.utils.docbuild.module_parsing.DataDict")) – A dictionary containing the names of all DOCUMENTED
          module-level attributes which are not a `TypeAlias`.
        * **TYPEVAR\_DICT** ([`TypeVarDict`](#manim.utils.docbuild.module_parsing.TypeVarDict "manim.utils.docbuild.module_parsing.TypeVarDict")) – A dictionary containing the definitions of `TypeVar` objects,
          organized by modules.

    Return type:
    :   tuple[[*AliasDocsDict*](#manim.utils.docbuild.module_parsing.AliasDocsDict "manim.utils.docbuild.module_parsing.AliasDocsDict"), [*DataDict*](#manim.utils.docbuild.module_parsing.DataDict "manim.utils.docbuild.module_parsing.DataDict"), [*TypeVarDict*](#manim.utils.docbuild.module_parsing.TypeVarDict "manim.utils.docbuild.module_parsing.TypeVarDict")]