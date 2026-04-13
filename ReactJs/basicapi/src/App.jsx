import { useEffect,useState } from "react"
function App(){
  const[data,setdata]=useState([])
  useEffect(()=>
  {
    fetch('https://dummyjson.com/recipes')
    .then((res)=>res.json())
    .then((ans)=>setdata(ans.recipes))
    .catch((err)=>console.log(err))
  },[])
  console.log(data);
  
return (
  <div className="my-5 max-w-5xl mx-auto md:grid-cols-2 lg:grid-cols-3">
    <header className="bg-gray-600 text-white text-3xl text-center py-3">Basic Api</header>
    <main className="max-w-5xl mx-auto grid md:grid-cols-2 lg:grid-cols-3 gap-4 p-4">
      {data.map((r)=>{
        return (
        <div className="p-5 flex flex-col justify-between rounded-2xl
        shadow shadow-amber-200">
          <img src={r.image} alt={r.name} />
          <h2>{r.name}</h2>
          <p>{r.rating}/5</p>
        </div>
        )
      })} 
    </main>
    <footer className="bg-gray-600 text-white text-2xl text-center py-2">Basic Api Build with ❤️ ROHIT</footer>
  </div>
)
}
export default App