from xml.etree import ElementTree


def find_cube_price(price, *seq_cub):
    if not seq_cub:
        return
    elements = []
    for cub in seq_cub:
        for element in cub:
            price_color[element.attrib["color"]] += price
            elements.append(element)
    return find_cube_price(price + 1, *elements)


root = ElementTree.fromstring(input())
price_color = {
    "red": 0,
    "green": 0,
    "blue": 0
}
price_color[root.attrib["color"]] += 1
find_cube_price(2, root)
print(*price_color.values(), sep=" ")
