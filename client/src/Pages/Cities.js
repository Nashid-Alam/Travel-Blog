import React, { useEffect, useState } from "react"
import CityCard from "../components/CityCard"

function Cities(props) {
  const [cities, setCities] = useState([])

  const getAllCities = () => {
    const response = [
      {
        _id: "1",
        name: "New York",
        country: "United States",
      },
      {
        _id: "2",
        name: "San Francisco",
        country: "United States",
      },
      {
        _id: "3",
        name: "Miami",
        country: "United States",
      },
    ]
    setCities(response)
  }

  useEffect(() => {
    getAllCities()
  }, [])

  return (
    <div>
      {cities.map((city) => {
        return (
          <CityCard
            onClick={() => props.history.push(`/blogs/${city._id}`)}
            key={city._id}
            city={city}
          />
        )
      })}
    </div>
  )
}

export default Cities
