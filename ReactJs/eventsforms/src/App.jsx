import React, { useState } from 'react'

function App() {
  const[top,setTop]=useState(50)
  const[left,setTop]=useState(50)
  function changeButtonPosition(e){
    console.log(e);
    e.clientX=Math.round(Math.random()*400)
    e.clientY=Math.round(Math.random()*400)
    setxpos(e.screenX)
  }
  return (
    <div>
      <header className='bg-gray-400 text-white text-5xl text-center py-3'>
        <h1>React events and forms</h1>
      </header>
      <div className='h-screen flex flex-col justify-center items-center'>
          <h2 className='text-green-800 text-7xl'>Do you like my classes</h2>
          <div  className='flex gap-3 m-4'>
            <button className='bg-black rounded-2xl p-3 text-2xl p-3 text-white'>Yes</button>
            <p>{xpos}</p>
            <button clientx={xpos} onMouseOver={changeButtonPosition} className='bg-black rounded-2xl p-3 text-2xl p-3 text-white'>No</button>
          </div>
      </div>
    </div>
  )
}

export default App
