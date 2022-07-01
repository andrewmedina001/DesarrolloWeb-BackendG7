class CamelCasePivot:
    def humpPivot(texto):
        txtPivot=texto.split(" ")
        txtP=""
        v=len(txtPivot)
        for a in range(len(txtPivot)):
            txtP+=txtPivot[a].capitalize()
            if a!=(v-1):
                txtP+=" "
        texto=txtP
        return texto