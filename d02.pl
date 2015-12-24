#!/usr/bin/perl -w

use strict;
use warnings;

use List::Util qw( min max sum product );

sub getAreaForBox {
  my ($l, $w, $h) = @_;

  my @side_area = (($l*$w), ($l*$h), ($w*$h));

  my $sas = sum @side_area;
  my $min = min @side_area;

  return 2 * $sas + $min;
}

sub getLengthForRibbon {
  my ($l, $w, $h) = @_;

  my @sorted = sort { $a <=> $b } @_;
  my $bow = product @sorted;
  my $perim = 2*$sorted[0] + 2*$sorted[1];

  return $bow + $perim;
}

my $num_args = $#ARGV + 1;
if ($num_args != 1) {
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

  # Part 1
  my $area += getAreaForBox @box;
  $area_sum += $area;

  # Part 2
  my $len = getLengthForRibbon @box;
  $ribbon_len_sum += $len;
}

print "Wrapping paper required (part1): $area_sum\nFeet of ribbon required (part2): $ribbon_len_sum\n"
