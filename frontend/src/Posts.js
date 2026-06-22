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


</div>


))

}



</div>

)

}


export default Posts;
