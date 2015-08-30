def char_counter(strarg):
    words = strarg.split(' ')
    for w in words:
        print ("{0} : {1} caracteres".format(w, len(w)))
    print ("Total: {0} \n".format(len(strarg)))

while True:
    user_input = input("Cadena: ")
    char_counter(user_input)
