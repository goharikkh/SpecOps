txt = open('2ex', 'r').read()
txt_new= open('2ex_new', 'w')
txt_titled = txt.title()
txt_new.write(txt_titled)