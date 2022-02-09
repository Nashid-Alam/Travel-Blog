import React, { useEffect, useState } from "react"
import axios from "axios"
import BlogDetailCard from "../components/BlogDetailCard"
import DiscussionCard from "../components/DiscussionCard"
import PictureCard from "../components/PictureCard"

const BASE_URL = process.env.REACT_APP_BASE_URL

function Blogdetail(props) {
  const [BlogDetail, setBlogDetail] = useState([])
  const blog_id = props.match.params.post_id
  console.log(props)

  const getBlogInfo = async () => {
    const response = await axios.get(`${BASE_URL}/blog-api/posts/${blog_id}`)
    setBlogDetail(response.data)
  }

  useEffect(() => {
    getBlogInfo()
  }, [])
  console.log(BlogDetail)
  return (
    <div>
      <BlogDetailCard key={BlogDetail.id} blog={BlogDetail} />

<PictureCard key={BlogDetail.id} Picture={BlogDetail.pictures} />

       <DiscussionCard
        key={BlogDetail.id}
        discussion={BlogDetail.discussions}
      />  
    </div> 
  )
}

export default Blogdetail
