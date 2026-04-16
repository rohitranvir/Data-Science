import React from 'react'
import Book from './Book'
import { useState } from 'react'

function App() {
  const[cart,statecart]=useState(0)
  return (
    <>
      <h1 className='text-center text-5xl my-2'>Parent Component : {cart}</h1>
      <button onClick={()=>{statecart(cart+1)}}>ADD product</button>
      <div className='mx-auto max-w-5xl grid grid-cols-3 gap-3'>
        <Book className='' title="Attack on titne" price='200'/>
        <Book title="Got" price='300'/>
        <Book title="Homelander" price='500'/>
      </div>
    </>
  )
}

export default App
