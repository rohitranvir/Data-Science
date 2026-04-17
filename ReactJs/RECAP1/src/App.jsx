import React, { useEffect } from 'react'
import Book from './Book'
import { useState } from 'react'

function App() {
  const[cart,setcart]=useState(0)
  const[books,setbooks]=useState([])
  useEffect(()=>{
    fetch("http://localhost:3001/books")
    .then((res)=>res.json())
    .then((data)=>setbooks(data))
    .catch((err)=>{console.log(err);
    })
  },[])
  const someValue=()=>{
    
  }
  return (
    <>
      <h1 className='text-center text-5xl my-2'>Parent Component : {cart}</h1>
      <button onClick={()=>{statecart(cart+1)}}>ADD product</button>
      <div className='mx-auto max-w-5xl grid grid-cols-3 gap-3'>
        {/* <Book className='' title="Attack on titne" price='200' setcart={setcart} cart={cart}/> */}
        {books.map((e)=>(<Book id={e.id} title={e.title} image={e.cover_image} pages={e.pages} />))}
      </div>
    </>
  )
}

export default App
