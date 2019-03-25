#!/usr/bin/env perl

use strict;
use warnings;
#use Readonly;
use Cwd;
use File::Path;
use File::Path 'rmtree';
use File::Basename;
use File::Copy qw/copy/;
use utf8;
use JSON;
use File::Slurp;
use File::Copy::Recursive qw/dircopy/;

my $TMP_DIR = "tmp";

my $TEMPLATE_FILE = "templates/html5_template.html";
my $METADATA_FILE = "templates/metadata.yaml";
my $MARKDOWN_DIR = "markdown";
my $SAMPLE_DIR = "sample";
my $IMAGE_DIR = "images";
my $FONT_DIR = "fonts";
my $SCSS_MAIN_FILE = "scss/style.scss";

if (@ARGV != 2) {
    die "Usage: build.pl <source directory> <release directory>\n";
}

my $SOURCE_DIR = $ARGV[0];
my $RELEASE_DIR = $ARGV[1];

sub get_dir_list {
    my ($dir, $dir_list_ref) = @_;

    push(@$dir_list_ref, $dir);

    my @files = glob("$dir/*");
    foreach my $file (@files) {
        get_dir_list($file, $dir_list_ref) if -d $file;
    }
}

sub get_markdown_file_list {
    my ($dir, $file_list_ref) = @_;

    my @files = glob("$dir/*");
    foreach my $file (@files) {
        if (-d $file) {
            get_markdown_file_list($file, $file_list_ref);
        } else {
            my ($base_name, $base_dir, $extension) = fileparse($file, ".md");
            push(@$file_list_ref, $file) unless !defined($extension) || ($extension ne ".md");
        }
    }
}


sub get_html_file_list {
    my ($dir, $file_list_ref) = @_;

    my @files = glob("$dir/*");
    foreach my $file (@files) {
        if (-d $file) {
            get_html_file_list($file, $file_list_ref);
        } else {
            my ($base_name, $base_dir, $extension) = fileparse($file, ".html");
            push(@$file_list_ref, $file) unless !defined($extension) || ($extension ne ".html");
        }
    }
}


sub create_temporary_directories {
    my @dirs = ();
    my $md_dir = "$SOURCE_DIR/$MARKDOWN_DIR";
    get_dir_list($md_dir, \@dirs);

    foreach (@dirs) {
        s/$md_dir/$TMP_DIR/;
        my $tmp_dir = $_;
        mkpath($tmp_dir);
        print "  Created $tmp_dir\n";
    }
}

sub include_code {
    my ($src_file_path, $dst_file_path, $pass_count) = @_;

    open(my $src_fh, "<", $src_file_path) || die "Can't open < $src_file_path: $!";
    open(my $dst_fh, ">", $dst_file_path) || die "Can't open > $dst_file_path: $!";

    while (<$src_fh>) {
        my $line = $_;
        if ($line !~ /^\s*\[\@include-source\s+.*\]/) {
            print $dst_fh $line;
            next;
        }

        my $include_pattern = "";
        my $embbed_filepath = "";
        my $embbed_extention = "";
        my $embbed_block = "";

        if ($line =~ /pattern="(full|partial)"/) {
            $include_pattern = $1;
        } else {
            print "Not found item 'pattern'\n";
            exit(1);
        }
        if ($line =~ /filepath="([\.\w\/]+)"/) {
            my @suffix_list = qw/.py .yml/;
            $embbed_filepath = "$SOURCE_DIR/$SAMPLE_DIR/$1";
            my ($base_name, $base_dir, $extension) = fileparse($embbed_filepath, @suffix_list);
            $embbed_extention = $extension;
        } else {
            print "Not found item 'filepath'\n";
            exit(1);
        }
        if ($line =~ /block="(\w+)"/) {
            $embbed_block = $1;
        } else {
            if ($include_pattern eq "partial") {
                print "Not found item 'block'\n";
                exit(1);
            }
        }

        if ($embbed_extention eq ".py") {
            print $dst_fh "```python\n";
        } elsif ($embbed_extention eq ".yml") {
            print $dst_fh "```yml\n";
        } else {
            print "Not supported extention $embbed_extention\n";
            exit(1);
        }

        if ($include_pattern eq "full") {
            open(my $embbed_fh, "<", $embbed_filepath) || die "Can't open < $embbed_filepath: $!";
            while (<$embbed_fh>) {
                my $l = $_;
                next if $l =~ /^\s*#\s*\@include-source\s*start\s*\[.*\]/;
                next if $l =~ /^\s*#\s*\@include-source\s*end\s*\[.*\]/;
                print $dst_fh $l;
            }
            close($embbed_fh);
        } elsif ($include_pattern eq "partial") {
            open(my $embbed_fh, "<", $embbed_filepath) || die "Can't open < $embbed_filepath: $!";
            my $in_partial = 0;
            while (<$embbed_fh>) {
                my $l = $_;
                if ($l =~ /^\s*#\s*\@include-source\s*start\s*\[(.*)\]/) {
                    if ($1 eq $embbed_block) {
                        $in_partial = 1;
                    }
                    next;
                } elsif ($l =~ /^\s*#\s*\@include-source\s*end\s*\[(.*)\]/) {
                    if ($1 eq $embbed_block) {
                        $in_partial = 0;
                    }
                    next;
                }
                print $dst_fh $l if $in_partial;
            }
            if ($in_partial) {
                print "'# \@include-source end' not found\n";
                exit(1);
            }
            close($embbed_fh);
        } else {
            print "Not supported pattern $include_pattern\n";
            exit(1);
        }

        print $dst_fh "```\n";
    }

    close($src_fh);
    close($dst_fh);

    print "    [Pass $pass_count] Include Code\n";
}


sub pre_process {
    my @md_files = ();
    my $md_dir = "$SOURCE_DIR/$MARKDOWN_DIR";
    get_markdown_file_list($md_dir, \@md_files);

    my @passes = (\&include_code);

    foreach my $md_file (@md_files) {
        $_ = $md_file;
        s/$md_dir\//$TMP_DIR\//;
        s/\.md$/-tmp\.md/;
        my $md_file_tmp = $_;

        my $pass_count = 0;
        copy($md_file, $md_file_tmp . "-tmp-" . $pass_count);
        foreach my $pass_fn (@passes) {
            my $src = $md_file_tmp . "-tmp-" . $pass_count;
            my $dst = $md_file_tmp . "-tmp-" . ($pass_count + 1);

            &$pass_fn($src, $dst, $pass_count);
            $pass_count += 1;
        }
        copy($md_file_tmp . "-tmp-" . $pass_count, $md_file_tmp);

        print "  Pre-processed ${md_file} -> ${md_file_tmp}\n";
    }
}


sub include_toc {
    my ($orig_file_path, $src_file_path, $dst_file_path, $pass_count) = @_;

    open(my $src_fh, "<", $src_file_path) || die "Can't open < $src_file_path: $!";
    open(my $dst_fh, ">", $dst_file_path) || die "Can't open > $dst_file_path: $!";

    while (<$src_fh>) {
        my $l = $_;
        if ($l !~ /<!--\s+\@include-toc\s+-->/) {
            print $dst_fh $l;
            next;
        }
        my $toc_file_path = "$SOURCE_DIR/templates/toc.json";
        my $data = File::Slurp::read_file($toc_file_path);
        my $json_data = JSON::decode_json($data);

        print $dst_fh "<ul>\n";
        if (exists($json_data->{"\@pre"})) {
            print $dst_fh "  <ul>\n";
            my $chapter_body = $json_data->{"\@pre"};
            foreach my $section (sort keys %$chapter_body) {
                my $url = get_relative_path($orig_file_path, $RELEASE_DIR . "/" . $chapter_body->{$section});
                my $section_body = $section;
                if ($section =~ /\@[0-9]+:(.+)/) {
                    $section_body = $1;
                }
                print $dst_fh "    <li><a href=\"$url\">$section_body</a></li>\n";
            }
            print $dst_fh "  </ul>\n";
        }
        print $dst_fh "</ul>\n";
        print $dst_fh "<ul>\n";
        foreach my $chapter (sort keys %$json_data) {
            if ($chapter eq "\@pre" || $chapter eq "\@post") {
                next;
            }
            my $chapter_body = $json_data->{$chapter};
            if (exists($chapter_body->{"\@title"})) {
                my $url = get_relative_path($orig_file_path, $RELEASE_DIR . "/" . $chapter_body->{"\@title"});
                print $dst_fh "  <li><a href=\"$url\">$chapter</a></li>\n";
            } else {
                print $dst_fh "  <li>$chapter</li>\n";
            }
            print $dst_fh "  <ul>\n";
            foreach my $section (sort keys %$chapter_body) {
                if ($section eq "\@title") {
                    next;
                }
                my $url = get_relative_path($orig_file_path, $RELEASE_DIR . "/" . $chapter_body->{$section});
                my $section_body = $section;
                if ($section =~ /\@[0-9]+:(.+)/) {
                    $section_body = $1;
                }
                print $dst_fh "    <li><a href=\"$url\">$section_body</a></li>\n";
            }
            print $dst_fh "  </ul>\n";
        }
        print $dst_fh "</ul>\n";
        print $dst_fh "<ul>\n";
        if (exists($json_data->{"\@post"})) {
            print $dst_fh "  <ul>\n";
            my $chapter_body = $json_data->{"\@post"};
            foreach my $section (sort keys %$chapter_body) {
                my $url = get_relative_path($orig_file_path, $RELEASE_DIR . "/" . $chapter_body->{$section});
                my $section_body = $section;
                if ($section =~ /\@[0-9]+:(.+)/) {
                    $section_body = $1;
                }
                print $dst_fh "    <li><a href=\"$url\">$section_body</a></li>\n";
            }
            print $dst_fh "  </ul>\n";
        }
        print $dst_fh "</ul>\n";
    }

    close($src_fh);
    close($dst_fh);

    print "    [Pass $pass_count] Include Code\n";
}


sub get_ordered_toc {
    my $toc_file_path = "$SOURCE_DIR/templates/toc.json";
    my $data = File::Slurp::read_file($toc_file_path);
    my $json_data = JSON::decode_json($data);

    my @ordered_toc = ();

    # @pre
    if (exists($json_data->{"\@pre"})) {
        my $chapter_body = $json_data->{"\@pre"};
        foreach my $section (sort keys %$chapter_body) {
            my $section_body = $section;
            if ($section =~ /\@[0-9]+:(.+)/) {
                $section_body = $1;
            }
            my @entry = ($section_body, $chapter_body->{$section});
            push(@ordered_toc, \@entry);
        }
    }

    foreach my $chapter (sort keys %$json_data) {
        if ($chapter eq "\@pre" || $chapter eq "\@post") {
            next;
        }

        # @title
        my $chapter_body = $json_data->{$chapter};
        if (exists($chapter_body->{"\@title"})) {
            my @entry = ($chapter, $chapter_body->{"\@title"});
            push(@ordered_toc, \@entry);
        }

        foreach my $section (sort keys %$chapter_body) {
            if ($section eq "\@title") {
                next;
            }
            my $section_body = $section;
            if ($section =~ /\@[0-9]+:(.+)/) {
                $section_body = $1;
            }
            my @entry = ($section_body, $chapter_body->{$section});
            push(@ordered_toc, \@entry);
        }
    }

    # @post
    if (exists($json_data->{"\@post"})) {
        my $chapter_body = $json_data->{"\@post"};
        foreach my $section (sort keys %$chapter_body) {
            my $section_body = $section;
            if ($section =~ /\@[0-9]+:(.+)/) {
                $section_body = $1;
            }
            my @entry = ($section_body, $chapter_body->{$section});
            push(@ordered_toc, \@entry);
        }
    }

    return @ordered_toc;
}


sub include_prev_next_url {
    my ($orig_file_path, $src_file_path, $dst_file_path, $pass_count) = @_;

    open(my $src_fh, "<", $src_file_path) || die "Can't open < $src_file_path: $!";
    open(my $dst_fh, ">", $dst_file_path) || die "Can't open > $dst_file_path: $!";

    my @ordered_toc = get_ordered_toc();
    my $own_url = $orig_file_path;
    my $prev_entry = undef;
    my $next_entry = undef;

    $own_url =~ s/$RELEASE_DIR\///;

    for (my $i = 0; $i < ($#ordered_toc + 1); $i++) {
        my $entry = $ordered_toc[$i];
        if ($$entry[1] eq $own_url) {
            if ($i != 0) {
                $prev_entry = $ordered_toc[$i - 1];
            }
            if ($i != $#ordered_toc) {
                $next_entry = $ordered_toc[$i + 1];
            }
            last;
        }
    }

    while (<$src_fh>) {
        my $l = $_;
        if ($l =~ /<!--\s+\@include-prev-url\s+-->/) {
            if (defined($prev_entry)) {
                my $title = $$prev_entry[0];
                my $url = $$prev_entry[1];
                my $rurl = get_relative_path($own_url, $url);
                my $body = "<a href=\"$rurl\">$title</a>";
                $l =~ s/<!--\s+\@include-prev-url\s+-->/$body/g;
            }
        }
        if ($l =~ /<!--\s+\@include-next-url\s+-->/) {
            if (defined($next_entry)) {
                my $title = $$next_entry[0];
                my $url = $$next_entry[1];
                my $rurl = get_relative_path($own_url, $url);
                my $body = "<a href=\"$rurl\">$title</a>";
                $l =~ s/<!--\s+\@include-next-url\s+-->/$body/g;
            }
        }

        print $dst_fh $l;
    }

    close($src_fh);
    close($dst_fh);

    print "    [Pass $pass_count] Include Prev Next URL\n";
}


sub replace_own_url {
    my ($orig_file_path, $src_file_path, $dst_file_path, $pass_count) = @_;

    open(my $src_fh, "<", $src_file_path) || die "Can't open < $src_file_path: $!";
    open(my $dst_fh, ">", $dst_file_path) || die "Can't open > $dst_file_path: $!";

    my $own_url = $orig_file_path;
    $own_url =~ s/$RELEASE_DIR\///;

    while (<$src_fh>) {
        my $l = $_;
        if ($l !~ /<!--\s+\@replace-own-url\s+-->/) {
            print $dst_fh $l;
            next;
        }
        $l =~ s/<!--\s+\@replace-own-url\s+-->/$own_url/g;
        print $dst_fh $l;
    }

    close($src_fh);
    close($dst_fh);

    print "    [Pass $pass_count] Replace Own URL\n";
}


sub post_process {
    my @html_files = ();
    my $html_dir = "$RELEASE_DIR";
    get_html_file_list($html_dir, \@html_files);

    my @passes = (\&include_toc, \&replace_own_url, \&include_prev_next_url);

    foreach my $html_file (@html_files) {
        $_ = $html_file;
        s/$html_dir\//$TMP_DIR\//;
        my $html_file_tmp = $_;

        my $pass_count = 0;
        copy($html_file, $html_file_tmp . "-tmp-" . $pass_count);
        foreach my $pass_fn (@passes) {
            my $src = $html_file_tmp . "-tmp-" . $pass_count;
            my $dst = $html_file_tmp . "-tmp-" . ($pass_count + 1);

            &$pass_fn($html_file, $src, $dst, $pass_count);
            $pass_count += 1;
        }
        copy($html_file_tmp . "-tmp-" . $pass_count, $html_file);

        print "  Post-processed $html_file\n";
    }
}


sub create_release_directories {
    my @dirs = ();
    my $md_dir = "$SOURCE_DIR/$MARKDOWN_DIR";
    my $html_dir = "$RELEASE_DIR";
    get_dir_list($md_dir, \@dirs);

    foreach (@dirs) {
        s/$md_dir\//$html_dir\//;
        my $rel_dir = $_;
        mkpath($rel_dir);
        print "  Created $rel_dir\n";
    }
}


sub get_release_css_path {
    my $scss_file = "$SOURCE_DIR/$SCSS_MAIN_FILE";

    $_ = $scss_file;
    s/$SOURCE_DIR\//$RELEASE_DIR\//;
    s/scss/css/g;

    return $_;
}


sub get_release_image_path {
    my $image_dir = "$SOURCE_DIR/$IMAGE_DIR";

    $_ = $image_dir;
    s/$SOURCE_DIR\//$RELEASE_DIR\//;

    return $_;
}


sub get_release_font_path {
    my $font_dir = "$SOURCE_DIR/$FONT_DIR";

    $_ = $font_dir;
    s/$SOURCE_DIR\//$RELEASE_DIR\//;

    return $_;
}

sub compile_scss {
    my $scss_file = "$SOURCE_DIR/$SCSS_MAIN_FILE";
    my $css_file = get_release_css_path();
    my ($base_name, $base_dir, $extension) = fileparse($css_file, ".css");

    mkpath($base_dir);
    print "  Created $base_dir\n";

    my $cmd = "sass $scss_file:$css_file";
    my $ret = system($cmd);
    if ($ret != 0) {
        print "Failed to compile scss";
        exit(1);
    }
    print "  Generated CSS File $scss_file -> $css_file\n";
}


sub copy_images {
    my $image_dir = "$SOURCE_DIR/$IMAGE_DIR";
    my $release_image_dir = get_release_image_path();

    my $num = dircopy($image_dir, $release_image_dir);

    print "  Copied Image Files $image_dir -> $release_image_dir\n";
}


sub copy_fonts {
    my $font_dir = "$SOURCE_DIR/$FONT_DIR";
    my $release_font_dir = get_release_font_path();

    my $num = dircopy($font_dir, $release_font_dir);

    print "  Copied Font Files $font_dir -> $release_font_dir\n";
}


sub get_relative_path {
    my ($path_1, $path_2) = @_;

    my @dir_list_1 = split(/\/+/, $path_1);
    my @dir_list_2 = split(/\/+/, $path_2);

    my $match_idx = 0;
    foreach my $dir1 (@dir_list_1) {
        my $dir2 = $dir_list_2[$match_idx];
        if ($dir1 ne $dir2) {
            last;
        }
        $match_idx++;
    }

    my $parent_level = $#dir_list_1 - $match_idx;

    my $rpath;
    if ($parent_level > 0) {
        $rpath = join("/", @dir_list_2[$match_idx..$#dir_list_2]);
        for (my $i = 0; $i < $parent_level; ++$i) {
            $rpath = "../$rpath";
        }
    } elsif ($parent_level == -1) {      # own
        $rpath = "";
    } elsif ($parent_level == 0) {
        if ($#dir_list_1 == $#dir_list_2) {
            $rpath = @dir_list_2[-1];
        } else {
            $rpath = join("/", @dir_list_2[$match_idx..$#dir_list_2]);
        }
    } else {
        print "Program Error: path_1=$path_1, path_2=$path_2, parent_level=$parent_level, rpath=$rpath";
        exit(1);
    }

    return $rpath;
}


sub generate_html_files {
    my $css_file = get_release_css_path();
    my @md_files = ();
    get_markdown_file_list($TMP_DIR, \@md_files);

    my $tmpl_file = "$SOURCE_DIR/$TEMPLATE_FILE";
    my $meta_file = "$SOURCE_DIR/$METADATA_FILE";
    my $html_dir = "$RELEASE_DIR";

    foreach my $md_file (@md_files) {
        $_ = $md_file;
        s/$TMP_DIR\//$html_dir\//;
        s/-tmp\.md$/\.html/;
        my $html_file = $_;

        my $rel_css_file = get_relative_path($html_file, $css_file);

        my $cmd = "pandoc -f markdown -t html5 --template=$tmpl_file $md_file -c $rel_css_file -o $html_file $meta_file";
        my $ret = system($cmd);
        if ($ret != 0) {
            print "Failed to generate $html_file";
            exit(1);
        }
        print "  Generated HTML File $md_file -> $html_file\n"
    }
}


sub clean_up {
    rmtree $TMP_DIR;
}


print "Creating Temporary Directories ...\n";
create_temporary_directories();

print "Pre-processing (Rewrite Markdown Files) ...\n";
pre_process();

print "Creating Release Directories ...\n";
create_release_directories();

print "Compiling scss ...\n";
compile_scss();

print "Copy Images ...\n";
copy_images();

print "Copy Fonts ...\n";
copy_fonts();

print "Generating HTML files ...\n";
generate_html_files();

print "Post-processing (Rewrite HTML Files) ...\n";
post_process();

print "Cleaning up ...\n";
clean_up();

print "Done!\n";
