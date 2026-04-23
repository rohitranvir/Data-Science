import { useEffect, useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from './assets/vite.svg'
// import heroImg from './assets/hero.png'
import './App.css'

function App() {

  const [books, setBooks] = useState([])
  const [title, settitle]=useState("")
  const [releaseyear,setreleaseyear]=useState(0)
  const[newtitle,setnewtitle]=useState("")
  useEffect(()=>{
    fetchBooks();
  },[])
  const fetchBooks=async()=>{
    try {
     const response= await fetch("http://127.0.0.1:8000/api/books/")
     const data=await response.json()
     setBooks(data)
     
    } catch (error) {
      console.log(error);
      
    }
  }
const addBook=async()=>{
const bookData={
  title:title,
  release_year:releaseyear
};
try {
const response=await fetch("http://127.0.0.1:8000/api/books/create",{
method:"POST",
headers:{
  'Content-Type':'application/json',

},
body:JSON.stringify(bookData)
});
const data=await response.json()
setBooks((prev)=>[...prev,data]);  

} catch (error) {
  console.log(error); 
  
}

}


const updateTitle=async(id,release_year)=>{
  const bookData={
    title:newtitle,
    release_year:release_year
  };
  try {
  const response=await fetch(`http://127.0.0.1:8000/api/books/${id}`,{
  method:"PUT",
  headers:{
    'Content-Type':'application/json',

  },
  body:JSON.stringify(bookData)
  });
  const data=await response.json()
  setBooks((prev)=>prev.map((book)=>{
    if (book.id===id){
      return data
    } else {
      return book;
    }
  }));  

  } catch (error) {
    console.log(error); 
    
  }

}
  return (
    < >
      <h1>Book Website</h1>
      <div className='container ' >
        <input type="text" placeholder='Enter a Book name..' onChange={(e)=>settitle(e.target.value)}/>
        <input type="number" placeholder='Release date...'onChange={(e)=>setreleaseyear(e.target.value)} />
        
        <button onClick={addBook}>Add Book</button>
        {books.map((book)=>(
          <div>
            <p>Title : {book.title}</p>
            <p>Release Year : {book.release_year}</p>
            <input type="text" placeholder='new Title...' onChange={(e)=>setnewtitle(e.target.value)}/>
            <button onClick={()=>updateTitle(book.id,book.release_year)}>Change Title</button>
          </div>))}
      </div>
    </>
  )
}

export default App
