import React, { useState } from 'react'
import Child from './child'
function App() {
  const[x,setx]=useState(0)
  const handleclick=()=>console.log("Button Clicked");
  
  return (
    <div>
        <h1>{x}</h1>
        <button onClick={()=>setx(x+1)} >click</button>
        <Child clickfn={handleclick}/>
    </div>
  )
}

export default App
