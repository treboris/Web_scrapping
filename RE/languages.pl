#!/usr/bin/perl -l
use Class::CSV;
use warnings;
use strict;


sub main
{
  my $file = 'technologiak.txt';
  open(FH, $file) or die ('File not found!');


  while (my $String = <FH>)
  {
      if($String =~ /GIT/)
      {
          print('$String \n');


      }

  }
  close(FH)





}
main();
