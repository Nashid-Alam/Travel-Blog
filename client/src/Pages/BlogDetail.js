import React, { useEffect, useState } from "react"
import axios from "axios"
import BlogDetailCard from "../components/BlogDetailCard"
import DiscussionCard from "../components/DiscussionCard"
import PictureCard from "../components/PictureCard"

const BASE_URL = process.env.REACT_APP_BASE_URL

function Blogdetail(props) {
  const blog_id = props.match.params.post_id

  const [blogDetail, setBlogDetail] = useState({})
  const [pictures, setPictures] = useState([])
  const [discussions, setDiscussions] = useState([])

  const getBlogInfo = async () => {
    const response = await axios.get(`${BASE_URL}/blog-api/posts/${blog_id}`)
    setBlogDetail(response.data)
    if (blogDetail !== "") {
      setPictures(response.data.pictures)
      setDiscussions(response.data.discussions)
    }
  }

  useEffect(() => {
    getBlogInfo()
  }, [])

  return (
    <div>
      <BlogDetailCard blog={blogDetail} />
      <h1>Pictures</h1>
      {pictures.map((picture) => {
        return <PictureCard picture={picture} />
      })}

      <h1>Discussions</h1>
      {discussions.map((discussion) => {
        return <DiscussionCard discussion={discussion} />
      })}
    </div>
  )
}

export default Blogdetail
