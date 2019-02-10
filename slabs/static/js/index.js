
const play = (type,name) => {
  if ((type === "join" && name !== "") || type === "watch") {
    $.post("/join",{type:type, name: name}).done((data)=>{
      console.log("here");
      console.log(data);
    });
  }
}
