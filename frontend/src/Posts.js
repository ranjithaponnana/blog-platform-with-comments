import React,{useEffect,useState} from "react";
import axios from "axios";


function Posts(){


const [posts,setPosts]=useState([]);



function getPosts(){

axios.get(
"http://127.0.0.1:5000/posts"
)

.then(res=>{

setPosts(res.data);

});

}



useEffect(()=>{

getPosts();

},[]);




function deletePost(id){


const token =
localStorage.getItem("token");


axios.delete(

`http://127.0.0.1:5000/posts/${id}`,

{
headers:{
Authorization:`Bearer ${token}`
}
}

)

.then(()=>{

alert("Post deleted");

getPosts();

});


}





function updatePost(id){


let title =
prompt("Enter new title");


let content =
prompt("Enter new content");



const token =
localStorage.getItem("token");



axios.put(

`http://127.0.0.1:5000/posts/${id}`,

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

.then(()=>{

alert("Post updated");

getPosts();

});


}





return(

<div>

<h2>
All Blog Posts
</h2>


{

posts.map(post=>(

<div key={post[0]}>


<h3>
{post[2]}
</h3>


<p>
{post[3]}
</p>



<button
onClick={()=>updatePost(post[0])}
>
Edit
</button>



<button
onClick={()=>deletePost(post[0])}
>
Delete
</button>


</div>


))

}


</div>

)

}


export default Posts;
