import React from "react"

function DiscussionCard(props) {
  return (
    <div>
      <h3>{props.discussion.author}</h3>
      <p>{props.discussion.content}</p>
    </div>
  )
}

export default DiscussionCard
