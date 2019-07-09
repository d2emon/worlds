

def world_helper(
    title,
    slug,
    image=None,
    loader=None,
    **data,
):
    if image is not None:
        image = "{}/{}".format(slug, image)
    return {
        'title': title,
        'image': image,
        'slug': slug,
        'wiki': "{}/index.md".format(slug),
        'loader': loader,
        'data': data,
    }


def table_row(*cols):
    return "|{}|".format("|".join(cols))


def table_header(*titles):
    return [
        table_row(*titles),
        table_row(*["-" * len(title) for title in titles]),
    ]


def table(*rows, header=None):
    if len(rows) < 1:
        return ""

    if header is None:
        header = (" " * len(row) for row in rows[0])

    return "\n".join(table_header(*header) + [table_row(*row) for row in rows])


def show_book(book_data):
    if book_data is None:
        return ""

    field_names = {
        "year": "Выпуск:         ",
        "isbn": "ISBN:           ",
        "pages": "Страниц:        ",
        "author": "Автор:          ",
        "series": "Серия:          ",
        "language": "Язык оригинала: ",
        "publisher": "Издательство:   ",
        "book_type": "Носитель:       ",
    }
    return table(*[
        (
            field_names.get(field),
            "{:32}".format(value),
        )
        for field, value in book_data.items()
        if field_names.get(field)
    ]) + "\n"


def show_facts(facts):
    if facts is None:
        return ""
    return "## Интересные факты\n\n{}\n".format(
        "\n".join(["* {}".format(fact) for fact in facts])
    )


def show_planets(planets):
    if planets is None:
        return ""
    return "\n".join([
        "### {}\n{}\n".format(planet.title, planet.description)
        for planet in planets
    ])
