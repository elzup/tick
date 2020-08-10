require 'time'

loop do
  sleep 1
  puts Time.now.iso8601()
end