# convert gds to svg

import nazca as nd
inputfile = 'cover_circuit_post.gds'
print(f'Processing {inputfile}')
cells = nd.load_gds(inputfile, asdict=True)
print(f'cells.keys(): {cells.keys()}')
export_cells = cells['cover_circuit']
nd.export_svg(export_cells)