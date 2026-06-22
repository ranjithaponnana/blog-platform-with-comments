import React,{useState} from "react";
import axios from "axios";


function Comments({postId}){


const [comment,setComment]=useState("");



function addComment(){


const token =
localStorage.getItem("token");



axios.post(

"http://127.0.0.1:5000/comments",

{
post_id:postId,
comment:comment
},

{
headers:{
Authorization:`Bearer ${token}`
}
}

)

.then(()=>{

alert("Comment added");

});


}



return(

<div>


<h3>
Comments
</h3>


<input

placeholder="Write comment"

onChange={
e=>setComment(e.target.value)
}

/>


<button onClick={addComment}>
Comment
</button>


</div>

)

}


export default Comments;
