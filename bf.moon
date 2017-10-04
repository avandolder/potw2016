-- Moonscript is cool little scripting language that compiles to Lua.
-- It's essentially Coffeescript but for Lua instead of Javascript.
-- It has an online compiler/interpreter that can be accessed at
-- http://moonscript.org/compiler/.

bf = (code) ->
    code ..= " " -- Append a space to the end of the code to remove issues of
                 -- the last character being skipped.
    mem = {0}
    mem_ptr = 1
    output = ""
    ip = 1
    while ip < code\len!
        -- Get the current operation from the code.
        op = code\sub(ip, ip)

        if op == "+"
            -- Increment the current mem cell.
            mem[mem_ptr] += 1

        elseif op == "-"
            -- Decrement the current mem cell.
            mem[mem_ptr] -= 1

        elseif op == ">"
            -- Move the memory pointer ahead, initializing the cell if it hasn't
            -- been used before.
            mem_ptr += 1
            if mem[mem_ptr] == nil then mem[mem_ptr] = 0

        elseif op == "<"
            -- Move the memory pointer back, initializing the cell if it hasn't
            -- been used before.
            mem_ptr -= 1
            if mem[mem_ptr] == nil then mem[mem_ptr] = 0

        elseif op == "["
            if mem[mem_ptr] == 0
                -- Go to the character after the matching ]
                inner_brackets = 0
                while true
                    ip += 1
                    if code\sub(ip, ip) == "["
                        inner_brackets += 1
                    elseif code\sub(ip, ip) == "]"
                        if inner_brackets > 0
                            inner_brackets -= 1
                        else
                            break

        elseif op == "]"
            if mem[mem_ptr] != 0
                -- Loop back to the matching [
                inner_brackets = 0
                while true
                    ip -= 1
                    if code\sub(ip, ip) == "]"
                        inner_brackets += 1
                    elseif code\sub(ip, ip) == "["
                        if inner_brackets > 0
                            inner_brackets -= 1
                        else
                            break

        elseif op == "."
            output ..= string.char(mem[mem_ptr])

        --elseif curr_char == ","
            -- No way to handle input at this time.

        ip += 1

    output

print bf(io.read())
