import React from 'react'

function Book({title,price,cart,setcart}) {
  return (
    <div className='p-3 rounded-2xl  gap-2 bg-amber-200'>
        <h1>Book name : {title}</h1>
        <h2>Price : {price}</h2>
        <button className='btn btn-primary bg-black text-white rounded-3xl py-1 px-5 text-center'onClick={()=>{setcart(cart+1)}}>Add to cart</button>
    </div>
  )
}

export default Book
