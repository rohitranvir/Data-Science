import Products from '../components/Products'
import Product from '../components/Product';
import { ShoppingCart } from 'lucide-react';
import { useState } from 'react';
const App=()=>{
    const[count,setCount]=useState(0)
return (
    <>
    <header className=' bg-neutral-700 text-3xl text-white py-3 px-5 flex justify-between items-center'>
        <h2>
            Basic <span className='text-blue-500'>Shop</span>
        </h2>
        <div className='flex justify-center items-center'>
            <ShoppingCart /><span className='absolute top-1 right-3 text-red-500 '>{count}</span>
        </div>
    </header>
    <Products counterFn={setCount} countFn={count}/>
    <footer className='bg-neutral-700 text-2xl text-white text-center py-3'>
        This site belongs to Rohit&copy;2026. It is made with  ❤️ 
    </footer>
   </>
)
}
export default App

