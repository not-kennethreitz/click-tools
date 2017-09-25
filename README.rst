click-tools
===========

A collection of utilities (extracted from `clint <https://github.com/kennethreitz/clint>`_), for use with Click.

Examples
--------

Printing various colors::

    import click
    from click_tools import crayons

    click.echo(
        '{red}{blue}{green}'.format(
            red=crayon.red('red'),
            blue=crayon.blue('blue')
            green=crayon.green('green')
        )
    )


Identation::

    from click_tools import puts, indent

    puts('this is an example of text that is not indented')
    with indent(4):
        puts('This is indented text.')


Columns::

    >>> from click_tools import cols

    >>> a = (
            'a very long string that requires text-wrapping in order to be '
            'printed correctly.'
        )
    >>> b = 'this is other text\nothertext\nothertext'

    >>> click.echo(columns((a, 20), (b, 20), (b, None)))
    a very long string   this is other text   this is other text
    that requires        othertext            othertext
    text-wrapping in     othertext            othertext
    order to be printed
    correctly.
