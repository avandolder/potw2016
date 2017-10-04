-- POTW 2016 Week 15 - Spreadsheets
-- Adam Vandolder, 2017-01-25

string.split = (sep) =>
    -- string.split function from http://lua-users.org/wiki/SplitJoin.
    -- Works as a method on strings, splitting them into a series of substrings
    -- seperated by 'sep' charcters.
    sep, fields = sep or ":", {}
    pattern = string.format("([^%s]+)", sep)
    @gsub(pattern, ((c) -> fields[#fields+1] = c))
    return fields

process_cell = (cell) ->
    -- Takes the string representation of a Mexcel cell and converts it into
    -- either a numeric cell or a table containing the cells it needs to
    -- calculate it's sum.
    if tonumber(cell)
        -- If the cell contains a valid number, return it.
        return tonumber(cell)
    else
        cells_added = cell\split('+')
        cells = {}
        for c in *cells_added
            -- For each cell the sum needs, make a table containing its
            -- row and column in the spreadsheet in numeric form.
             cells[#cells + 1] = {c\byte(1,1) - 'A'\byte! + 1,
                                 c\byte(2,2) - 'A'\byte! + 1}

        return cells

n = tonumber(io.read!)

graph = {}  -- graph contains all of the cells that do not rely on another (i.e.
            -- numeric cells, and sum cells that have been fully processed).
sums = {}   -- sum contains all of the sums cells that need to be processed.

for row = 1,n
    -- Read in row of the spreadsheet and seperate it around the commas.
    row_text = io.read!
    row_cells = row_text\split(',')

    for column = 1,n
        -- For each cell in row, process it and put it in either the graph
        -- table or the sums table.
        cell = process_cell(row_cells[column])

        if type(cell) == 'number'
            graph[#graph + 1] = {pos: {row, column}, val: cell}
        else
            sums[#sums + 1] = {pos: {row, column}, depends: cell, val: 0}

-- The following while loop is an implementation of Khan's algorithm for
--topological sorting, as given on Wikipedia.
sorted_graph = {}
while #graph > 0
    -- Remove the top element of graph and append it to
    sorted_graph[#sorted_graph + 1] = graph[#graph]
    graph[#graph] = nil

    for i = #sums,1,-1
        for j = #sums[i].depends,1,-1
            -- d is a cell (in {row, column} form) that d[i] depends on.
            d = sums[i].depends[j]
            -- sg is the most recent element placed in the sorted_graph.
            sg = sorted_graph[#sorted_graph]

            if d[1] == sg.pos[1] and d[2] == sg.pos[2]
                -- If d depends on sg, add sg to d's sum, then remove the link
                -- connecting them.
                sums[i].val += sg.val
                table.remove(sums[i].depends, j)

                -- If d has no more dependencies, remove it from dependents and
                -- put it in graph.
                if #sums[i].depends == 0
                    graph[#graph + 1] = sums[i]
                    table.remove(sums, i)

spreadsheet = {}
for i = 1,#sorted_graph
    cell = sorted_graph[i]

    row, column = cell.pos[1], cell.pos[2]
    if not spreadsheet[row]
        -- If the row of the spreadsheet doesn't exist, create it.
        spreadsheet[row] = {}

    -- Take the numeric value of the cell in the graph and place it in the
    -- correct position of the spreadsheet.
    spreadsheet[row][column] = cell.val

for row = 1,n
    for column = 1,n
        -- Output the value of each cell of the spreadsheet.
        io.write spreadsheet[row][column]
        if column ~= n
            io.write ','
    io.write '\n'
