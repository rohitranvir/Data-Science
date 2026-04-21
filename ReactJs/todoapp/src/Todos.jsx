import React, { useEffect } from 'react'
import { useState } from 'react'

function Todos() {
    // let temp=[]
  const[inputvalue,setInputvalue]=useState("")
  const[todoitems,setTodoitems]=useState([])
  const[isChecked,setischecked]=useState(false)
  function Addtodo(){
        setTodoitems([...todoitems,{text:inputvalue,isComplated:false}])
        fetch('https://ca92e8ccb499d7944dd9.free.beeceptor.com',{
          method:"POST",
          body:JSON.stringify([...todoitems,{text:inputvalue,isComplated:false}])
        }).then((res)=>console.log(res)        
        .catch((err)=>console.log(err)
        )
        )
       
        setInputvalue(" ")
  }
  function deletetodo(ind) {
    let newTodosItems=todoitems.filter((e,i)=>i!=ind)
    setTodoitems(newTodosItems)
  }

useEffect(()=>{
  fetch("https://ca92e8ccb499d7944dd9.free.beeceptor.com")

  .then((res)=>res.json())
  .then((res)=>console.log(res)  )
},[todoitems])
  
  return (
    <div className='mx-auto my-5 max-w-5xl flex flex-col gap-5 justify-center items-center'>
        <div className='flex gap-3'>
            <input type="text"  className='focus:outline-0 border-2 border-black rounded-2xl text-3xl p-3' placeholder='What you want to do today' onChange={(e)=>{setInputvalue(e.target.value)}}  value={inputvalue}/>
            <button className='bg-black text-white text-2xl rounded-2xl' onClick={Addtodo}>Add task</button>
        </div>
        <div className='flex flex-col gap-2  items'>
            {todoitems.map((e,i)=>(
              <div className='flex gap-2'>
                <input type="checkbox" className='h-10 w-5' checked={isChecked} onClick={()=>{e.isComplated=e.isComplated?false:true;
                  if(isChecked)
                    setischecked(false)
                  else
                    setischecked(true)
  
                }}/>
                <p className='text-2xl text-black font-bold' style={{color:e.isComplated?"green":"black"}}>{e.text}</p>
                <button className='bg-red-500 text-white rounded-2xl p-2' onClick={()=>deletetodo(i)}>Delete</button>
              </div>
                
            ))}
        </div>
      {/*  */}
    </div>
  )
}

export default Todos
