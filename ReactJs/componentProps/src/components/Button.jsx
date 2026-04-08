const Button =({color,text,size})=>{
    return(
        <button style={{color:color, fontSize:size}}>
        {text}
        </button>
    )
}
export default Button