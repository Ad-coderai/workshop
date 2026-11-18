function change()
{
    let heading = Document.getElementById("header");
    if(heading.style.colour == "black")
    {
        heading.style.color = "rgb(75, 2, 2)";
    }
    else
    {
         heading.style.color = "black";
    }
}