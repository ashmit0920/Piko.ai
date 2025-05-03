# Source: https://docs.manim.community/en/stable/reference/manim.utils.iterables.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

iterables[¶](#module-manim.utils.iterables "Link to this heading")
==================================================================

Operations on iterables.

TypeVar’s

*class* T[¶](#manim.utils.iterables.T "Link to this definition")
:   ```
    TypeVar('T')

    ```

*class* U[¶](#manim.utils.iterables.U "Link to this definition")
:   ```
    TypeVar('U')

    ```

*class* F[¶](#manim.utils.iterables.F "Link to this definition")
:   ```
    TypeVar('F', np.float64, np.int_)
    ```

*class* H[¶](#manim.utils.iterables.H "Link to this definition")
:   ```
    TypeVar('H', bound=Hashable)

    ```

Functions

adjacent\_n\_tuples(*objects*, *n*)[[source]](../_modules/manim/utils/iterables.html#adjacent_n_tuples)[¶](#manim.utils.iterables.adjacent_n_tuples "Link to this definition")
:   Returns the Sequence objects cyclically split into n length tuples.

    See also

    [`adjacent_pairs`](#manim.utils.iterables.adjacent_pairs "manim.utils.iterables.adjacent_pairs")
    :   alias with n=2

    Examples

    ```
    >>> list(adjacent_n_tuples([1, 2, 3, 4], 2))
    [(1, 2), (2, 3), (3, 4), (4, 1)]
    >>> list(adjacent_n_tuples([1, 2, 3, 4], 3))
    [(1, 2, 3), (2, 3, 4), (3, 4, 1), (4, 1, 2)]

    ```

    Parameters:
    :   * **objects** (*Sequence**[*[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")*]*)
        * **n** (*int*)

    Return type:
    :   zip[tuple[[T](#manim.utils.iterables.T "manim.utils.iterables.T"), …]]

adjacent\_pairs(*objects*)[[source]](../_modules/manim/utils/iterables.html#adjacent_pairs)[¶](#manim.utils.iterables.adjacent_pairs "Link to this definition")
:   Alias for `adjacent_n_tuples(objects, 2)`.

    See also

    [`adjacent_n_tuples`](#manim.utils.iterables.adjacent_n_tuples "manim.utils.iterables.adjacent_n_tuples")

    Examples

    ```
    >>> list(adjacent_pairs([1, 2, 3, 4]))
    [(1, 2), (2, 3), (3, 4), (4, 1)]

    ```

    Parameters:
    :   **objects** (*Sequence**[*[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")*]*)

    Return type:
    :   zip[tuple[[T](#manim.utils.iterables.T "manim.utils.iterables.T"), …]]

all\_elements\_are\_instances(*iterable*, *Class*)[[source]](../_modules/manim/utils/iterables.html#all_elements_are_instances)[¶](#manim.utils.iterables.all_elements_are_instances "Link to this definition")
:   Returns `True` if all elements of iterable are instances of Class.
    False otherwise.

    Parameters:
    :   * **iterable** (*Iterable**[**object**]*)
        * **Class** (*type**[**object**]*)

    Return type:
    :   bool

batch\_by\_property(*items*, *property\_func*)[[source]](../_modules/manim/utils/iterables.html#batch_by_property)[¶](#manim.utils.iterables.batch_by_property "Link to this definition")
:   Takes in a Sequence, and returns a list of tuples, (batch, prop)
    such that all items in a batch have the same output when
    put into the Callable property\_func, and such that chaining all these
    batches together would give the original Sequence (i.e. order is
    preserved).

    Examples

    ```
    >>> batch_by_property([(1, 2), (3, 4), (5, 6, 7), (8, 9)], len)
    [([(1, 2), (3, 4)], 2), ([(5, 6, 7)], 3), ([(8, 9)], 2)]

    ```

    Parameters:
    :   * **items** (*Iterable**[*[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")*]*)
        * **property\_func** (*Callable**[**[*[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")*]**,* [*U*](#manim.utils.iterables.U "manim.utils.iterables.U")*]*)

    Return type:
    :   list[tuple[list[[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")], [*U*](#manim.utils.iterables.U "manim.utils.iterables.U") | None]]

concatenate\_lists(*\*list\_of\_lists*)[[source]](../_modules/manim/utils/iterables.html#concatenate_lists)[¶](#manim.utils.iterables.concatenate_lists "Link to this definition")
:   Combines the Iterables provided as arguments into one list.

    Examples

    ```
    >>> concatenate_lists([1, 2], [3, 4], [5])
    [1, 2, 3, 4, 5]

    ```

    Parameters:
    :   **list\_of\_lists** (*Iterable**[*[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")*]*)

    Return type:
    :   list[[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")]

hash\_obj(*obj*)[[source]](../_modules/manim/utils/iterables.html#hash_obj)[¶](#manim.utils.iterables.hash_obj "Link to this definition")
:   Determines a hash, even of potentially mutable objects.

    Parameters:
    :   **obj** (*object*)

    Return type:
    :   int

list\_difference\_update(*l1*, *l2*)[[source]](../_modules/manim/utils/iterables.html#list_difference_update)[¶](#manim.utils.iterables.list_difference_update "Link to this definition")
:   Returns a list containing all the elements of l1 not in l2.

    Examples

    ```
    >>> list_difference_update([1, 2, 3, 4], [2, 4])
    [1, 3]

    ```

    Parameters:
    :   * **l1** (*Iterable**[*[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")*]*)
        * **l2** (*Iterable**[*[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")*]*)

    Return type:
    :   list[[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")]

list\_update(*l1*, *l2*)[[source]](../_modules/manim/utils/iterables.html#list_update)[¶](#manim.utils.iterables.list_update "Link to this definition")
:   Used instead of `set.update()` to maintain order,
    :   making sure duplicates are removed from l1, not l2.
        Removes overlap of l1 and l2 and then concatenates l2 unchanged.

    Examples

    ```
    >>> list_update([1, 2, 3], [2, 4, 4])
    [1, 3, 2, 4, 4]

    ```

    Parameters:
    :   * **l1** (*Iterable**[*[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")*]*)
        * **l2** (*Iterable**[*[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")*]*)

    Return type:
    :   list[[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")]

listify(*obj: str*) → list[str][[source]](../_modules/manim/utils/iterables.html#listify)[¶](#manim.utils.iterables.listify "Link to this definition")

listify(*obj: Iterable[[T](#manim.utils.iterables.T "manim.utils.iterables.T")]*) → list[[T](#manim.utils.iterables.T "manim.utils.iterables.T")]

listify(*obj: [T](#manim.utils.iterables.T "manim.utils.iterables.T")*) → list[[T](#manim.utils.iterables.T "manim.utils.iterables.T")]
:   Converts obj to a list intelligently.

    Examples

    ```
    >>> listify("str")
    ['str']
    >>> listify((1, 2))
    [1, 2]
    >>> listify(len)
    [<built-in function len>]

    ```

make\_even(*iterable\_1*, *iterable\_2*)[[source]](../_modules/manim/utils/iterables.html#make_even)[¶](#manim.utils.iterables.make_even "Link to this definition")
:   Extends the shorter of the two iterables with duplicate values until its
    :   length is equal to the longer iterable (favours earlier elements).

    See also

    [`make_even_by_cycling`](#manim.utils.iterables.make_even_by_cycling "manim.utils.iterables.make_even_by_cycling")
    :   cycles elements instead of favouring earlier ones

    Examples

    ```
    >>> make_even([1, 2], [3, 4, 5, 6])
    ([1, 1, 2, 2], [3, 4, 5, 6])

    >>> make_even([1, 2], [3, 4, 5, 6, 7])
    ([1, 1, 1, 2, 2], [3, 4, 5, 6, 7])

    ```

    Parameters:
    :   * **iterable\_1** (*Iterable**[*[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")*]*)
        * **iterable\_2** (*Iterable**[*[*U*](#manim.utils.iterables.U "manim.utils.iterables.U")*]*)

    Return type:
    :   tuple[list[[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")], list[[*U*](#manim.utils.iterables.U "manim.utils.iterables.U")]]

make\_even\_by\_cycling(*iterable\_1*, *iterable\_2*)[[source]](../_modules/manim/utils/iterables.html#make_even_by_cycling)[¶](#manim.utils.iterables.make_even_by_cycling "Link to this definition")
:   Extends the shorter of the two iterables with duplicate values until its
    :   length is equal to the longer iterable (cycles over shorter iterable).

    See also

    [`make_even`](#manim.utils.iterables.make_even "manim.utils.iterables.make_even")
    :   favours earlier elements instead of cycling them

    Examples

    ```
    >>> make_even_by_cycling([1, 2], [3, 4, 5, 6])
    ([1, 2, 1, 2], [3, 4, 5, 6])

    >>> make_even_by_cycling([1, 2], [3, 4, 5, 6, 7])
    ([1, 2, 1, 2, 1], [3, 4, 5, 6, 7])

    ```

    Parameters:
    :   * **iterable\_1** (*Collection**[*[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")*]*)
        * **iterable\_2** (*Collection**[*[*U*](#manim.utils.iterables.U "manim.utils.iterables.U")*]*)

    Return type:
    :   tuple[list[[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")], list[[*U*](#manim.utils.iterables.U "manim.utils.iterables.U")]]

remove\_list\_redundancies(*lst*)[[source]](../_modules/manim/utils/iterables.html#remove_list_redundancies)[¶](#manim.utils.iterables.remove_list_redundancies "Link to this definition")
:   Used instead of `list(set(l))` to maintain order.
    Keeps the last occurrence of each element.

    Parameters:
    :   **lst** (*Reversible**[*[*H*](#manim.utils.iterables.H "manim.utils.iterables.H")*]*)

    Return type:
    :   list[[*H*](#manim.utils.iterables.H "manim.utils.iterables.H")]

remove\_nones(*sequence*)[[source]](../_modules/manim/utils/iterables.html#remove_nones)[¶](#manim.utils.iterables.remove_nones "Link to this definition")
:   Removes elements where bool(x) evaluates to False.

    Examples

    ```
    >>> remove_nones(["m", "", "l", 0, 42, False, True])
    ['m', 'l', 42, True]

    ```

    Parameters:
    :   **sequence** (*Iterable**[*[*T*](#manim.utils.iterables.T "manim.utils.iterables.T") *|* *None**]*)

    Return type:
    :   list[[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")]

resize\_array(*nparray*, *length*)[[source]](../_modules/manim/utils/iterables.html#resize_array)[¶](#manim.utils.iterables.resize_array "Link to this definition")
:   Extends/truncates nparray so that `len(result) == length`.
    :   The elements of nparray are cycled to achieve the desired length.

    See also

    [`resize_preserving_order`](#manim.utils.iterables.resize_preserving_order "manim.utils.iterables.resize_preserving_order")
    :   favours earlier elements instead of cycling them

    [`make_even_by_cycling`](#manim.utils.iterables.make_even_by_cycling "manim.utils.iterables.make_even_by_cycling")
    :   similar cycling behaviour for balancing 2 iterables

    Examples

    ```
    >>> points = np.array([[1, 2], [3, 4]])
    >>> resize_array(points, 1)
    array([[1, 2]])
    >>> resize_array(points, 3)
    array([[1, 2],
           [3, 4],
           [1, 2]])
    >>> resize_array(points, 2)
    array([[1, 2],
           [3, 4]])

    ```

    Parameters:
    :   * **nparray** (*npt.NDArray**[*[*F*](#manim.utils.iterables.F "manim.utils.iterables.F")*]*)
        * **length** (*int*)

    Return type:
    :   npt.NDArray[[F](#manim.utils.iterables.F "manim.utils.iterables.F")]

resize\_preserving\_order(*nparray*, *length*)[[source]](../_modules/manim/utils/iterables.html#resize_preserving_order)[¶](#manim.utils.iterables.resize_preserving_order "Link to this definition")
:   Extends/truncates nparray so that `len(result) == length`.
    :   The elements of nparray are duplicated to achieve the desired length
        (favours earlier elements).

        Constructs a zeroes array of length if nparray is empty.

    See also

    [`resize_array`](#manim.utils.iterables.resize_array "manim.utils.iterables.resize_array")
    :   cycles elements instead of favouring earlier ones

    [`make_even`](#manim.utils.iterables.make_even "manim.utils.iterables.make_even")
    :   similar earlier-favouring behaviour for balancing 2 iterables

    Examples

    ```
    >>> resize_preserving_order(np.array([]), 5)
    array([0., 0., 0., 0., 0.])

    >>> nparray = np.array([[1, 2], [3, 4]])
    >>> resize_preserving_order(nparray, 1)
    array([[1, 2]])

    >>> resize_preserving_order(nparray, 3)
    array([[1, 2],
           [1, 2],
           [3, 4]])

    ```

    Parameters:
    :   * **nparray** (*npt.NDArray**[**np.float64**]*)
        * **length** (*int*)

    Return type:
    :   npt.NDArray[np.float64]

resize\_with\_interpolation(*nparray*, *length*)[[source]](../_modules/manim/utils/iterables.html#resize_with_interpolation)[¶](#manim.utils.iterables.resize_with_interpolation "Link to this definition")
:   Extends/truncates nparray so that `len(result) == length`.
    :   New elements are interpolated to achieve the desired length.

        Note that if nparray’s length changes, its dtype may too
        (e.g. int -> float: see Examples)

    See also

    [`resize_array`](#manim.utils.iterables.resize_array "manim.utils.iterables.resize_array")
    :   cycles elements instead of interpolating

    [`resize_preserving_order`](#manim.utils.iterables.resize_preserving_order "manim.utils.iterables.resize_preserving_order")
    :   favours earlier elements instead of interpolating

    Examples

    ```
    >>> nparray = np.array([[1, 2], [3, 4]])
    >>> resize_with_interpolation(nparray, 1)
    array([[1., 2.]])
    >>> resize_with_interpolation(nparray, 4)
    array([[1.        , 2.        ],
           [1.66666667, 2.66666667],
           [2.33333333, 3.33333333],
           [3.        , 4.        ]])
    >>> nparray = np.array([[[1, 2], [3, 4]]])
    >>> nparray = np.array([[1, 2], [3, 4], [5, 6]])
    >>> resize_with_interpolation(nparray, 4)
    array([[1.        , 2.        ],
           [2.33333333, 3.33333333],
           [3.66666667, 4.66666667],
           [5.        , 6.        ]])
    >>> nparray = np.array([[1, 2], [3, 4], [1, 2]])
    >>> resize_with_interpolation(nparray, 4)
    array([[1.        , 2.        ],
           [2.33333333, 3.33333333],
           [2.33333333, 3.33333333],
           [1.        , 2.        ]])

    ```

    Parameters:
    :   * **nparray** (*npt.NDArray**[*[*F*](#manim.utils.iterables.F "manim.utils.iterables.F")*]*)
        * **length** (*int*)

    Return type:
    :   npt.NDArray[[F](#manim.utils.iterables.F "manim.utils.iterables.F")]

stretch\_array\_to\_length(*nparray*, *length*)[[source]](../_modules/manim/utils/iterables.html#stretch_array_to_length)[¶](#manim.utils.iterables.stretch_array_to_length "Link to this definition")
:   Parameters:
    :   * **nparray** (*npt.NDArray**[*[*F*](#manim.utils.iterables.F "manim.utils.iterables.F")*]*)
        * **length** (*int*)

    Return type:
    :   npt.NDArray[[F](#manim.utils.iterables.F "manim.utils.iterables.F")]

tuplify(*obj: str*) → tuple[str][[source]](../_modules/manim/utils/iterables.html#tuplify)[¶](#manim.utils.iterables.tuplify "Link to this definition")

tuplify(*obj: Iterable[[T](#manim.utils.iterables.T "manim.utils.iterables.T")]*) → tuple[[T](#manim.utils.iterables.T "manim.utils.iterables.T")]

tuplify(*obj: [T](#manim.utils.iterables.T "manim.utils.iterables.T")*) → tuple[[T](#manim.utils.iterables.T "manim.utils.iterables.T")]
:   Converts obj to a tuple intelligently.

    Examples

    ```
    >>> tuplify("str")
    ('str',)
    >>> tuplify([1, 2])
    (1, 2)
    >>> tuplify(len)
    (<built-in function len>,)

    ```

uniq\_chain(*\*args*)[[source]](../_modules/manim/utils/iterables.html#uniq_chain)[¶](#manim.utils.iterables.uniq_chain "Link to this definition")
:   Returns a generator that yields all unique elements of the Iterables
    :   provided via args in the order provided.

    Examples

    ```
    >>> gen = uniq_chain([1, 2], [2, 3], [1, 4, 4])
    >>> from collections.abc import Generator
    >>> isinstance(gen, Generator)
    True
    >>> tuple(gen)
    (1, 2, 3, 4)

    ```

    Parameters:
    :   **args** (*Iterable**[*[*T*](#manim.utils.iterables.T "manim.utils.iterables.T")*]*)

    Return type:
    :   *Generator*[[*T*](#manim.utils.iterables.T "manim.utils.iterables.T"), None, None]