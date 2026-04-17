import React, { useState } from 'react'
import Todos from './Todos'

function App() {

  return (
    <div>
      <header className='bg-gray-700 text-4xl text-white text-center py-3'>Simple ToDo Application</header>
      <Todos ></Todos>
      <footer className='border-t-2 border-black text-3xl'>This website is made by rohit &copy; 2026</footer>
    </div>
  )
}

export default App
