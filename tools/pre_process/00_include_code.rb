require 'fileutils'

if ARGV.size != 2 then
    puts "Usage: 00_include_code.rb <source> <target>"
end

src_path = ARGV[0]
tgt_path = ARGV[1]

# make clean source
src_file = File.open(src_path, 'r')
tgt_file = File.open(tgt_path, 'w')
src_file.each_line do |line|
    if /^\s*\[@include-source\s+.*\]/ !~ line then
        tgt_file.puts(line)
        next line
    end

    include_pattern = ""
    embbed_filepath = ""
    embbed_extention = ""
    embbed_block = ""

    if /pattern="(full|partial)"/ =~ line then
        include_pattern = $1
    else
        puts("Not found item 'pattern'")
        exit 1
    end
    if /filepath="([\.\w\/]+)"/ =~ line then
        embbed_filepath = File.dirname(src_path) + "/" + $1
        embbed_extention = File.extname(embbed_filepath)
    else
        puts("Not found item 'filepath'")
        exit 1
    end
    if /block="(\w+)"/ =~ line then
        embbed_block = $1
    else
        if include_pattern == "partial" then
            puts("Not found item 'block'")
            exit 1
        end
    end

    if embbed_extention == ".py" then
        tgt_file.puts("```python")
    else
        puts("Not supported extention " + embbed_extention)
        exit 1
    end

    if include_pattern == "full" then
        embbed_file = File.open(embbed_filepath, 'r')
        embbed_file.each_line do |l|
            next l if /^\s*#\s*@include-source\s*start\s*\[.*\]/ =~ l
            next l if /^\s*#\s*@include-source\s*end\s*\[.*\]/ =~ l
            tgt_file.puts(l)
        end
    elsif include_pattern == "partial" then
        embbed_file = File.open(embbed_filepath, 'r')
        in_partial = false
        embbed_file.each_line do |l|
            if /^\s*#\s*@include-source\s*start\s*\[(.*)\]/ =~ l then
                if $1 == embbed_block then
                    in_partial = true
                end
                next l
            elsif /^\s*#\s*@include-source\s*end\s*\[(.*)\]/ =~ l then
                if $1 == embbed_block then
                    in_partial = false
                end
                next l
            end
            if in_partial then
                tgt_file.puts(l)
            end
        end
        if in_partial then
            puts("'# @include-source end' not found")
            exit 1
        end
    else
        puts("Not supported pattern " + include_pattern)
        exit 1
    end

    tgt_file.puts("```")
end

exit 0
