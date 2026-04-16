import React from 'react'

function Book(props) {
  return (
    <div className='p-3 rounded-2  gap-2 bg-amber-200'>
        <h1>Book name : {props.title}</h1>
        <h2>Price : {props.price}</h2>
    </div>
  )
}

export default Book
