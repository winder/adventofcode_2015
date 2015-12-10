#!/usr/bin/perl -w

use strict;
use warnings;

use List::Util qw( min max sum product );

sub getAreaForBox {
  my ($l, $w, $h) = @_;

  my @side_area = (($l*$w), ($l*$h), ($w*$h));

  my $sas = sum @side_area;
  my $min = min @side_area;
  print "l: $l w: $w h: $h, area: $sas min: $min\n";

  return 2 * $sas + $min;
}

sub getLengthForRibbon {
  my ($l, $w, $h) = @_;

  print "not sort: $_[0], $_[1], $_[2]\n";
  my @sorted = sort { $a <=> $b } @_;
  print "    sort: $sorted[0], $sorted[1], $sorted[2]\n";
  my $bow = product @sorted;
  my $perim = 2*$sorted[0] + 2*$sorted[1];

  return $bow + $perim;
}

my $num_args = $#ARGV + 1;
if ($num_args != 1) {
  print "\nUsage: name.pl first_name last_name\n";
  exit;
}

my $input_file=$ARGV[0];

my $count = 0;
my $area_sum = 0;
my $ribbon_len_sum = 0;

open(my $fh, '<:encoding(UTF-8)', $input_file)
  or die "Could not open file '$input_file' $!";

while( my $line = <$fh>)  {   
  chomp($line);

  my @box = split /x/, $line;

  my $area += getAreaForBox @box;
  $area_sum += $area;

  my $len = getLengthForRibbon @box;
  $ribbon_len_sum += $len;
  print "Ribbon length: $len\n";

  #last if ++$count == 2;
}

print "Hello, $input_file, area_sum: $area_sum ribbon_len_sum: $ribbon_len_sum\n"
