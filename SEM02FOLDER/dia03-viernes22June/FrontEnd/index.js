const RUTA_BACK="http://127.0.0.1:5000";

fetch(RUTA_BACK+"/state",{method:"GET"})
    .then((rpta)=>{
        return rpta.json();
    })
    .then((data)=>{
        console.log(data);
    })
    .catch((error)=>{
        console.error(error)
    })

fetch(RUTA_BACK+"/producto",{
    method:'POST',
    body:JSON.stringify({
        nombre:'Zanahoria',
        precio:4.50,
    }),
    headers:{
        "Content-Type":"application/json",
    }
})
    .then((rpta)=>{
        return rpta.json();
    })
    .then((data)=>{
        console.log(data);
    })
    .catch((error)=>{
        console.error(error)
    })