const Cartoon=({imgLink,name1})=>{
    return (
    <div className="p-5 border border-black-300 rounded rounded-3xl flex flex-col gap-2">
        <img src={imgLink} />
        <h2>{name1}</h2>
    </div>
    )
}
export default Cartoon