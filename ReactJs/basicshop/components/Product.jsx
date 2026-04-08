import { useState } from 'react';

function Product({ title, image, price,counterFn,countFn}) {
    const[val,currstate]=useState(0)
  return (
    <div className="flex flex-col justify-between gap-2 p-3 rounded-2xl shadow-2xl shadow-blue-300">
      <img src={image} alt={title} />
      <h2>{title}</h2>
      <p>Price : ₹{price}</p>
      <button className='bg-black text-2xl py-2 text-center text-white rounded-3xl' onClick={() => counterFn(countFn + 1)}>Add to cart</button>
    </div>
  );
}

export default Product;
