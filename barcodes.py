"""

"""
import barcode
from barcode.writer import ImageWriter
from barcode import ISBN13
from cairosvg import svg2png

isbn = '978-1-961343-01-6'
name = "Tensegrity"
barcode = ISBN13(isbn)
barcode.save(name)
svg = f'{name}.svg'

svg2png(url=svg, write_to=f"{name}.png")