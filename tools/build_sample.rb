require 'fileutils'

if ARGV.size != 2 then
    puts "Usage: build_sample.rb <source> <target>"
end

raw_path = ARGV[0]
target_path = ARGV[1]

filelist = []
entry = Dir.glob(raw_path + '/**/**', File::FNM_DOTMATCH)
entry.each {|e|
    next e if File::ftype(e) == 'directory'
    filelist.push(e)
}

filelist.each {|filepath|
    next filepath if filepath.match(/^sample\//)
    next filepath if File.extname(filepath) != '.py' and File.extname(filepath) != '.yml'

    path = filepath.dup
    path.slice!(raw_path)

    # make clean source
    src_file = File.open(filepath, 'r')
    dest_file = File.open(target_path + path, 'w')
    src_file.each_line do |line|
        next line if /^\s*\/\/! \[.*\]/ =~ line
        dest_file.puts(line)
    end
    puts filepath + " -> " + target_path + path
}

exit 0
