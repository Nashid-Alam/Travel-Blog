import React from "react"

function CityCard(props) {
  return (
    <div>
      <h4>
        {props.city.name}, {props.city.country}
      </h4>
    </div>
  )
}

export default CityCard
