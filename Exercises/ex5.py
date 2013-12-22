i_name = 'Zed. A. Shaw'
i_age = 35 # not a lie
i_height = 74 # inches
i_height_cm = i_height * 2.54
i_weight = 180 # lbs
i_weight_kg = i_weight * 0.45
i_eyes = 'Blue'
i_teeth = 'White'
i_hair = 'Brown'

print "Let's talk about %s." % i_name
print "He's %d inches tall." % i_height
print "He's %d centimeters tall." % i_height_cm
print "He's %d pounds heavy." % i_weight
print "He's %d kilos heavy." % i_weight_kg
print "Acutally that's not too heavy."
print "He's got %s eyes and %s hair." % (i_eyes, i_hair)
print "His teeth are usually %s depending on the coffee." % i_teeth

#this line is tricky, try to get it exactly right
print "If i add %d, %d, and %d I get %d." % (i_age, i_height, i_weight, i_age + i_height + i_weight)