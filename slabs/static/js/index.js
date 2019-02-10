console.log("asdf");


const play = (type,name) => {
  if ((type === "join" && name !== "") || type === "watch") {
    $.post("url",{type:type, name: name}).done((data)=>{
      console.log(data);
    });
  }
}
