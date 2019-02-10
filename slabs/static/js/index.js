
const play = (type,name) => {
  if ((type === "join" && name !== "") || type === "watch") {
    $.post("/join",{type:type, name: name}).done((data)=>{
      $('#content').html(data);
    });
  }
}


const selectCard = (id) => {
  for(var i = 0; i <= 3; i++){
    if(i == id){
      $("#"+id).removeClass("grey").addClass("green");
      $("#"+id+" > i").html("check")
    }
    else{
      $("#"+i).removeClass("green").addClass("grey");
      $("#"+i+" > i").html("")
    }
  }

}

const submitCard = () =>{
  for(var i = 0; i <= 3; i++){
    if($("#"+i).hasClass("green")){
      console.log(i);
      return false;
    }
  }

}
