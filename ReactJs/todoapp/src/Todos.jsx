import React from 'react'
import { useState } from 'react'

function Todos() {
    // let temp=[]
  const[inputvalue,setInputvalue]=useState("")
  const[todoitems,setTodoitems]=useState([])
  function Addtodo(){
        setTodoitems([...todoitems,{text:inputvalue,isComplated:false}])
        setInputvalue(" ")
  }
  return (
    <div className='mx-auto my-5 max-w-5xl flex flex-col gap-5 justify-center items-center'>
        <div className='flex gap-3'>
            <input type="text" onChange={(e)=>{setInputvalue(e.target.value)}}  value={inputvalue} className='focus:outline-0 border-2 border-black rounded-2xl text-3xl p-3' placeholder='What you want to do today'/>
            <button className='bg-black text-white text-2xl rounded-2xl' onClick={Addtodo}>Add task</button>
        </div>
        <div className='flex flex-col gap-2'>
            {todoitems.map((e)=>(
                <p >{e.text}</p>
            ))}
        </div>
      {/*  */}
    </div>
  )
}

export default Todos
