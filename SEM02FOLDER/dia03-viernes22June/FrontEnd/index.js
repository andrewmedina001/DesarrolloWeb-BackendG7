const RUTA_BACK="http://127.0.0.1:5000";

fetch(RUTA_BACK+"/estado",{method:"GET"})
    .then((rpta)=>{
        return rpta.json();
    })
    .then((data)=>{
        console.log(data);
    })
    .catch((error)=>{
        console.error(error)
    })