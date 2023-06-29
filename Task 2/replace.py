sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."
# Replacing the excalmation points with a space, will mean it also leaves a space between "dog" and the full stop.
# Stripped original full stop and sliced to remove final space and added a new full stop.
sentence = sentence.replace ("!"," ").strip(".")[:43]+"."
print (sentence)
# redefined the variable to include replacements to make next two stages simpler.
print (sentence.upper())
print (sentence.upper()[::-1])
# Final step asked to print the sentence in reverse. I took this to mean reprint where we were up to in reverse and not the original sentence.
# Initially had some issues with getting the upper function to work but I'd forgotten to add the brackets after upper.