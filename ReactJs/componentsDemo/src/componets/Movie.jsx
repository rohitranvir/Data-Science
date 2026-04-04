function Movie(param) {
return (
        <div className="Movie">
         <img src={param.imgLink}
         />
         <h2>{param.title}</h2>
         <p>Release Year : {param.year}</p>
    </div>
)
}
export default Movie