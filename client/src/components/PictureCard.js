import React from "react"

function PictureCard(props) {
  console.log(props)
  return <div>
<h3>pictures</h3>

{props.Picture.map((pics) => {
        return (
         
         <img src={pics.url} alt="pics"/>
        )
      })}

  </div>
}

export default PictureCard;
