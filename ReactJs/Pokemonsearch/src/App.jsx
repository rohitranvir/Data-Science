import './App.css'
import { useState,useEffect } from 'react'
function App(){
const [name1,setName]=useState("")
const[pokdetails,setPokdetails]=useState({})
console.log(pokdetails);

const[error,setError]=useState('')
useEffect(()=>{
async function fetchdata() {   
  if (name1!=""){
  try {
    const res=await fetch(`https://pokeapi.co/api/v2/pokemon/${name1}`)
  const data= await res.json()  
  setPokdetails(data)

  } catch (error) {
    setError(error)
  }
  }
}
fetchdata()
},[name1])


return(
      <>
        <header className='bg-gray-600 text-2xl text-white flex justify-between py-3 px-5'>
          <h2 className='text-4xl'>Poke<span className='text-blue-500'>DEX</span></h2>
          <div className='border border-white rounded-2xl p-1'>
          <input type="text" placeholder=" Enter the pokemon name" name=""className="border-0 focus:outline-0" id='na' value={name1} onChange={(e)=>setName(e.target.value) }/>
          </div>
        </header>
          <main className='h-screen flex justify-center items-center'>
            {pokdetails.sprites && (           
              <>
              <img src={pokdetails.sprites.front_default} alt={pokdetails.name} className='h-96' />
              <div>
              <h1 className='text-3xl'>{pokdetails.name}</h1>
              <p className='text-2xl'>{pokdetails.height}</p>
              <p className='text-2xl'>{pokdetails.weight}</p>
              </div>
            
              </>
              ) }
          </main>
          <footer className='text-3xl bg-gray-600  text-center py-2'>This site belongs to XYZ @copy;2026 </footer>
      </>
  )
}
export default App