require 'fileutils'

raw_path = 'sample_raw/'
target_path = 'sample/'

filelist = []
entry = Dir.glob(raw_path + '**/**')
entry.each {|e|
    next e if File::ftype(e) == 'directory'
    filelist.push(e)
}

filelist.each {|filepath|
    next filepath if filepath.match(/^sample\//)
    next filepath if File.extname(filepath) != '.py'

    path = filepath.dup
    path.slice!(raw_path)

    # make clean source
    src_file = File.open(filepath, 'r')
    dest_file = File.open(target_path + path, 'w')
    src_file.each_line do |line|
        next line if /^\s*\/\/! \[.*\]/ =~ line
        dest_file.puts(line)
    end
}

exit 0
