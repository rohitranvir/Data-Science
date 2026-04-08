  import './App.css'
  import { useState } from 'react';
  // function App()
  // {
  //   // const[count,statecount]=useState(0)
  //   // function increse(){
  //   //   statecount(count+1)
  //   // }
  //   // function decrese(){
  //   //   statecount(count-1)
  //   // }
  //   const[text,statetext]=useState("")
  //    const[inp,stateinp]=useState("")
  //   function enter(){
  //     statetext(inp)
  //   }
    
  //   //  console.log(count);
  //   return(
  //     <>

  //     <input type="text" value={inp} onChange={(e)=>stateinp(e.target.value)}/>
  //     <h1>You have entered : {text}</h1>
  //       {/* <p>{count}</p> */}
      
  //             {/* <button onClick={increse}>Increse</button>
  //             <button onClick={decrese}>Decrease</button> */}
  //             <button onClick={enter}>You have</button>
        
  //     </>
  //   )
  // }
  // export default App



// function App(){
//   const[val,state]=useState(0)
//   function increase(){
//     state(val+1)
//   }
//   function decrease(){
//     state(val-1)
//   }
//   return (
//     <>
//     <h1>{val}</h1>
//     <button onClick={increase}>Increase</button>
//     <button onClick={decrease}>decrease</button>
//     </>
//   )
// }


function App(){
  const[text,statext]=useState("")
  const[inp,stateinp]=useState("")
  function enter(){
      statext(inp)
  }
  return (
    <>
     <input type="text" value={inp} onChange={(e)=>stateinp(e.target.value)} />
     <h1>You have entered : {text}</h1>
     <button type="button" onClick={enter}>Enter</button>
    </>
  )

}


export default App