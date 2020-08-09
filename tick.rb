require 'time'

min1 = 60

loop do
  sleep min1
  puts Time.now.iso8601()
end