# Source: https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LogBase.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

LogBase[¶](#logbase "Link to this heading")
===========================================

Qualified name: `manim.mobject.graphing.scale.LogBase`

*class* LogBase(*base=10*, *custom\_labels=True*)[[source]](../_modules/manim/mobject/graphing/scale.html#LogBase)[¶](#manim.mobject.graphing.scale.LogBase "Link to this definition")
:   Bases: `_ScaleBase`

    Scale for logarithmic graphs/functions.

    Parameters:
    :   * **base** (*float*) – The base of the log, by default 10.
        * **custom\_labels** (*bool*) – For use with [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes"):
          Whether or not to include `LaTeX` axis labels, by default True.

    Examples

    ```
    func = ParametricFunction(lambda x: x, scaling=LogBase(base=2))

    ```

    Methods

    |  |  |
    | --- | --- |
    | [`function`](#manim.mobject.graphing.scale.LogBase.function "manim.mobject.graphing.scale.LogBase.function") | Scales the value to fit it to a logarithmic scale.``self.function(5)==10\*\*5`` |
    | [`get_custom_labels`](#manim.mobject.graphing.scale.LogBase.get_custom_labels "manim.mobject.graphing.scale.LogBase.get_custom_labels") | Produces custom [`Integer`](manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer") labels in the form of `10^2`. |
    | [`inverse_function`](#manim.mobject.graphing.scale.LogBase.inverse_function "manim.mobject.graphing.scale.LogBase.inverse_function") | Inverse of `function`. |

    function(*value*)[[source]](../_modules/manim/mobject/graphing/scale.html#LogBase.function)[¶](#manim.mobject.graphing.scale.LogBase.function "Link to this definition")
    :   Scales the value to fit it to a logarithmic scale.``self.function(5)==10\*\*5``

        Parameters:
        :   **value** (*float*)

        Return type:
        :   float

    get\_custom\_labels(*val\_range*, *unit\_decimal\_places=0*, *\*\*base\_config*)[[source]](../_modules/manim/mobject/graphing/scale.html#LogBase.get_custom_labels)[¶](#manim.mobject.graphing.scale.LogBase.get_custom_labels "Link to this definition")
    :   Produces custom [`Integer`](manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer") labels in the form of `10^2`.

        Parameters:
        :   * **val\_range** (*Iterable**[**float**]*) – The iterable of values used to create the labels. Determines the exponent.
            * **unit\_decimal\_places** (*int*) – The number of decimal places to include in the exponent
            * **base\_config** (*dict**[**str**,* *Any**]*) – Additional arguments to be passed to [`Integer`](manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").

        Return type:
        :   list[[Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")]

    inverse\_function(*value*)[[source]](../_modules/manim/mobject/graphing/scale.html#LogBase.inverse_function)[¶](#manim.mobject.graphing.scale.LogBase.inverse_function "Link to this definition")
    :   Inverse of `function`. The value must be greater than 0

        Parameters:
        :   **value** (*float*)

        Return type:
        :   float