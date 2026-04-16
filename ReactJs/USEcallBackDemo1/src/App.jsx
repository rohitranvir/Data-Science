  import React, { useCallback, useMemo, useState } from 'react'
  import Child from './child'
  function App() {
    const[x,setx]=useState(0)
    const handleclick=useCallback(()=>console.log("Button Clicked"),[]);  
    const counterfunct=useMemo(()=>{
      let p=1
      for (let i=1;i<=10;i++){
        p=i*p               
      }
      console.log(p);
       
    } ,[] )
    return (
      <div>
          <h1>{x}</h1>          
          <button onClick={counterfunct}>counter funct</button>
          <button onClick={()=>setx(x+1)} >click</button>
          <Child clickfn={handleclick}/>
      </div>
    )
  }

  export default App
