# Source: https://docs.manim.community/en/stable/reference/manim.utils.config_ops.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

config\_ops[¶](#module-manim.utils.config_ops "Link to this heading")
=====================================================================

Utilities that might be useful for configuration dictionaries.

Classes

|  |  |
| --- | --- |
| [`DictAsObject`](manim.utils.config_ops.DictAsObject.html#manim.utils.config_ops.DictAsObject "manim.utils.config_ops.DictAsObject") |  |

Functions

merge\_dicts\_recursively(*\*dicts*)[[source]](../_modules/manim/utils/config_ops.html#merge_dicts_recursively)[¶](#manim.utils.config_ops.merge_dicts_recursively "Link to this definition")
:   Creates a dict whose keyset is the union of all the
    input dictionaries. The value for each key is based
    on the first dict in the list with that key.

    dicts later in the list have higher priority

    When values are dictionaries, it is applied recursively

    Parameters:
    :   **dicts** (*dict**[**Any**,* *Any**]*)

    Return type:
    :   dict[*Any*, *Any*]

update\_dict\_recursively(*current\_dict*, *\*others*)[[source]](../_modules/manim/utils/config_ops.html#update_dict_recursively)[¶](#manim.utils.config_ops.update_dict_recursively "Link to this definition")
:   Parameters:
    :   * **current\_dict** (*dict**[**Any**,* *Any**]*)
        * **others** (*dict**[**Any**,* *Any**]*)

    Return type:
    :   None