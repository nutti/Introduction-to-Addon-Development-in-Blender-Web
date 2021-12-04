use strict;
use warnings;

if (@ARGV != 2) {
    print "embed_ad.pl <input> <pattern>\n";
    exit(1);
}

my $input_file = $ARGV[0];
my $pattern_file = $ARGV[1];

open(FINPUT, "< $input_file") or die "$!";
open(FPATTERN, "< $pattern_file") or die "$!";

my %patterns = ();
while (<FPATTERN>) {
    if ($_ =~ m/^\s*([0-9a-zA-Z_]+)=(.+)/) {
        $patterns{$1} = $2;
    }
}

while (<FINPUT>) {
    my $line = $_;
    my $embed_key = "";
    my $embed_value = "";
    my $embed_spacer = "";
    foreach my $key (keys(%patterns)) {
        my $value = $patterns{$key};
        if ($line =~ m/^(\s*)<!--\s+embed_ad=$key\s+-->/) {
            $embed_key = $key;
            $embed_value = $value;
            $embed_spacer = $1;
            last;
        }
    }
    if ($embed_key ne "") {
        print $embed_spacer . "<!-- EMBEDDED AD START (embed_ad=$embed_key) -->\n";
        print $embed_spacer . $embed_value . "\n";
        print $embed_spacer . "<!-- EMBEDDED AD END (embed_ad=$embed_key) -->\n";
    } else {
        print $line;
    }
}

close(FINPUT);
close(FPATTERN);
