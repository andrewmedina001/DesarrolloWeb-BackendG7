from pkg01.camelcasePivot import CamelCasePivot

c=CamelCasePivot

parrafo="aa ee ii oo uu"
print("before:  {} ".format(parrafo))
result=c.humpPivot(parrafo)
print("after:   {}".format(result))