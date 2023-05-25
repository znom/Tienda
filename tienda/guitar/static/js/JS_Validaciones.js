var usuario = document.getElementById("nombreUsuario");
var correo = document.getElementById("correo");
var fecha_nac = document.getElementById("fechaNac");
var contra = document.getElementById("contra");
var confi_contra = document.getElementById("confi_contraseña");
var form = document.getElementById("form");
var men = document.getElementById("mensaje");



form.addEventListener("submit", e=>{

    

    let men = "";
    let espacios = false;
    let cont = 0;
    let entrar = false;
    let date_regex = /^(0[1-9]|1[0-2])\/(0[1-9]|1\d|2\d|3[01])\/(0[1-9]|1[1-9]|2[1-9])$/;
    let validar = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;


    if ( usuario.value.length < 5 ) {


        men += "Debe ingresar un usuario valido, y debe tener mas de 5 caracteres.<br>";
        entrar = true;

    } 

    if (validar.test(correo.value)){


    }else{

        men+="Debe ingresar un correo válido.<br>"
        entrar=true

    }

    if (date_regex.test(fecha_nac.value)){

        
    }else{

        men+= "Debe ingresar una fecha valida<br>"
        entrar = true

    }

    if(contra.value.length==0){

        men += "Debe ingresar una contraseña válida.<br>";
        entrar = true;
    }

    while (!espacios && (cont < contra.value.length)) {
        if (contra.value.charAt(cont) == " ")
          espacios = true;
        cont++;
      }
         
      if (espacios) {
        men += "La contraseña no puede tener espacios en blanco.<br>";
        entrar = true;
        

       
      }



    if (contra.value.length < 5 ){

        men += "Esta debe ser mayor a 5 caracteres.<br>";
        entrar = true;


    } 
    if(contra.value.match(/[a-z]/g)){


    }else{

        men += "Debe tener al menos 1 letra.<br>";
        entrar = true;

    }

    if (contra.value.match(/[$@$!%*?&#.]/g)){


    }else{
        men += "Debe tener al menos 1 caracter especial.<br>";
        entrar = true;


    }
   
    


    if (contra.value != confi_contra.value ){

        men += "Sus contraseñas deben coincidir."
        entrar = true

    }



    if(entrar){
        e.preventDefault();
        mensaje.innerHTML = men
        e.preventDefault();
        
    }else{


        
        mensaje.innerHTML = 'Validaciones cumplidas correctamente'
        
    }
    

} )

//Aqui terminan las del enzo  ↥ ↥ ↥ ↥ ↥ ↥ ↥ ↥

