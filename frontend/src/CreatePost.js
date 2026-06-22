import React,{useState} from "react";
import axios from "axios";


function CreatePost(){


const [title,setTitle]=useState("");

const [content,setContent]=useState("");




function createPost(){


const token =
localStorage.getItem("token");



axios.post(

"http://127.0.0.1:5000/posts",

{
title,
content
},

{
headers:{
Authorization:`Bearer ${token}`
}
}

)

.then(res=>{

alert(res.data.message);

});


}



return(

<div>

<h2>
Create New Post
</h2>



<input

placeholder="Post Title"

onChange={
e=>setTitle(e.target.value)
}

/>


<br/>


<textarea

placeholder="Post Content"

onChange={
e=>setContent(e.target.value)
}

/>


<br/>


<button onClick={createPost}>
Publish Post
</button>


</div>

)

}


export default CreatePost;
