# Source: https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

simple\_functions[¶](#module-manim.utils.simple_functions "Link to this heading")
=================================================================================

A collection of simple functions.

TypeVar’s

*class* ComparableT[¶](#manim.utils.simple_functions.ComparableT "Link to this definition")
:   ```
    TypeVar('ComparableT', bound=Comparable)

    ```

Classes

|  |  |
| --- | --- |
| [`Comparable`](manim.utils.simple_functions.Comparable.html#manim.utils.simple_functions.Comparable "manim.utils.simple_functions.Comparable") |  |

Functions

binary\_search(*function*, *target*, *lower\_bound*, *upper\_bound*, *tolerance=0.0001*)[[source]](../_modules/manim/utils/simple_functions.html#binary_search)[¶](#manim.utils.simple_functions.binary_search "Link to this definition")
:   Searches for a value in a range by repeatedly dividing the range in half.

    To be more precise, performs numerical binary search to determine the
    input to `function`, between the bounds given, that outputs `target`
    to within `tolerance` (default of 0.0001).
    Returns `None` if no input can be found within the bounds.

    Examples

    Consider the polynomial \(x^2 + 3x + 1\) where we search for
    a target value of \(11\). An exact solution is \(x = 2\).

    ```
    >>> solution = binary_search(lambda x: x**2 + 3*x + 1, 11, 0, 5)
    >>> bool(abs(solution - 2) < 1e-4)
    True
    >>> solution = binary_search(lambda x: x**2 + 3*x + 1, 11, 0, 5, tolerance=0.01)
    >>> bool(abs(solution - 2) < 0.01)
    True

    ```

    Searching in the interval \([0, 5]\) for a target value of \(71\)
    does not yield a solution:

    ```
    >>> binary_search(lambda x: x**2 + 3*x + 1, 71, 0, 5) is None
    True

    ```

    Parameters:
    :   * **function** (*Callable**[**[**float**]**,* *float**]*)
        * **target** (*float*)
        * **lower\_bound** (*float*)
        * **upper\_bound** (*float*)
        * **tolerance** (*float*)

    Return type:
    :   float | None

choose(*n*, *k*)[[source]](../_modules/manim/utils/simple_functions.html#choose)[¶](#manim.utils.simple_functions.choose "Link to this definition")
:   The binomial coefficient n choose k.

    \(\binom{n}{k}\) describes the number of possible choices of
    \(k\) elements from a set of \(n\) elements.

    References

    * <https://en.wikipedia.org/wiki/Combination>
    * <https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.comb.html>

    Parameters:
    :   * **n** (*int*)
        * **k** (*int*)

    Return type:
    :   int

clip(*a*, *min\_a*, *max\_a*)[[source]](../_modules/manim/utils/simple_functions.html#clip)[¶](#manim.utils.simple_functions.clip "Link to this definition")
:   Clips `a` to the interval [`min_a`, `max_a`].

    Accepts any comparable objects (i.e. those that support <, >).
    Returns `a` if it is between `min_a` and `max_a`.
    Otherwise, whichever of `min_a` and `max_a` is closest.

    Examples

    ```
    >>> clip(15, 11, 20)
    15
    >>> clip('a', 'h', 'k')
    'h'

    ```

    Parameters:
    :   * **a** ([*ComparableT*](#manim.utils.simple_functions.ComparableT "manim.utils.simple_functions.ComparableT"))
        * **min\_a** ([*ComparableT*](#manim.utils.simple_functions.ComparableT "manim.utils.simple_functions.ComparableT"))
        * **max\_a** ([*ComparableT*](#manim.utils.simple_functions.ComparableT "manim.utils.simple_functions.ComparableT"))

    Return type:
    :   [*ComparableT*](#manim.utils.simple_functions.ComparableT "manim.utils.simple_functions.ComparableT")

sigmoid(*x*)[[source]](../_modules/manim/utils/simple_functions.html#sigmoid)[¶](#manim.utils.simple_functions.sigmoid "Link to this definition")
:   Returns the output of the logistic function.

    The logistic function, a common example of a sigmoid function, is defined
    as \(\frac{1}{1 + e^{-x}}\).

    References

    * <https://en.wikipedia.org/wiki/Sigmoid_function>
    * <https://en.wikipedia.org/wiki/Logistic_function>

    Parameters:
    :   **x** (*float*)

    Return type:
    :   float