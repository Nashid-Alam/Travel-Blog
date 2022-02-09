import React from 'react';

function DiscussionCard(props) {
  console.log(props)
  return <div>
    <h3>Discussions</h3>

{props.discussion.map((discorse) => {
        return (
         
         <p>{discorse.content}</p>
        )
      })}
    
  </div>;
}

export default DiscussionCard;
