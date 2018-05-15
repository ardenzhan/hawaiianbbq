name = 'Arden Zhan'
age = 12 # not a lie
height = 50 # inches
weight = 100 # lbs
eyes = 'Black'
teeth = 'White'
hair = 'Black'
CM_PER_INCH = 2.54
KG_PER_LB = 0.453592

puts "Let's talk about #{name}."
puts "He's #{height} inches tall."
puts "He's #{weight} pounds heavy."
puts "Actually that's not too heavy."
puts "He's got #{eyes} eyes and #{hair} hair."
puts "His teeth are usually #{teeth} depending on the coffee."

# this line is tricky, try to get it exactly right
puts "If I add #{age}, #{height}, and #{weight} I get #{age + height + weight}."

# Metric
puts "Height: #{height * CM_PER_INCH} centimeters."
puts "Weight: #{weight * KG_PER_LB} kilograms."
