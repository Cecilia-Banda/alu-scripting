#!/usr/bin/env ruby
# Only match the capital letters

puts ARGV[0].scan(/[A-Z]/).join
