import React, { useEffect } from 'react'


function Child({clickfn}) {
    useEffect(()=>console.log("hii..."))
  return (
    <button onClick={clickfn}>
        Child Button
    </button>
  )
}

export default Child
